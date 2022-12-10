import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import Tokenizer, HashingTF, IDF, Word2Vec
from pyspark.ml.classification import LogisticRegression

import argparse
import os
import sys


DATA_PATH = os.path.join(os.path.dirname(sys.argv[0]), 'data/train.csv')

SEED=123
IDF_MIN_DF=10


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('method', type=str, choices=['htf', 'w2v'])
    parser.add_argument('num_features', type=int)
    return parser.parse_args()


def get_or_create_spark_session():
    return (SparkSession.builder
        .master('local[1]')
        .appName('HTF-IDF')
        .config('spark.driver.memory', '12g')
        .config('spark.executor.memory', '12g')
    .getOrCreate())


def load_csv_via_workaround(spark):
    # TODO: find a way not to treate unscaped commas inside quotes as delimiters
    #
    # Falied approaches:
    #   - using com.databricks.spark.csv
    #   - specifying quote option
    #   - specifying quote & escape option

    pandas_df = pd.read_csv(DATA_PATH)[['comment_text', 'toxic']].rename(columns={'toxic': 'label'})
    return spark.createDataFrame(pandas_df.dropna())


def load_train_val(spark):
    return load_csv_via_workaround(spark).randomSplit([0.7, 0.3], seed=SEED)


def build_htf_pipeline(num_features):
    return Pipeline(stages=[
        Tokenizer(inputCol='comment_text', outputCol='tokens'),
        HashingTF(inputCol='tokens', outputCol='htf', numFeatures=num_features),
        IDF(inputCol='htf', outputCol='features', minDocFreq=IDF_MIN_DF),
        LogisticRegression().setMaxIter(10).setRegParam(0.01).setFamily('binomial')
    ])


def build_w2v_pipeline(num_features):
    return Pipeline(stages=[
        Tokenizer(inputCol='comment_text', outputCol='tokens'),
        Word2Vec(vectorSize=num_features, minCount=0, inputCol='tokens', outputCol='features', seed=SEED),
        LogisticRegression().setMaxIter(10).setRegParam(0.01).setFamily('binomial')
    ])


def evaluate(model, df_val):
    predictions = model.transform(df_val)
    evaluator = BinaryClassificationEvaluator(metricName='areaUnderPR')
    return evaluator.evaluate(predictions)


def main():
    args = parse_args()
    build_pipeline = build_htf_pipeline if args.method == 'htf' else build_w2v_pipeline

    spark = get_or_create_spark_session()
    df_train, df_val = load_train_val(spark)

    pipeline = build_pipeline(args.num_features)
    model = pipeline.fit(df_train)

    print(args.method, args.num_features, evaluate(model, df_val))


if __name__ == '__main__':
    main()
