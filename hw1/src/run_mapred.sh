cd $(dirname $0)/..

echo "Uploading files to docker"
docker exec namenode mkdir -p /opt/hw1
docker cp ./data/AB_NYC_2019.csv namenode:/opt/hw1/
for FNAME in ./src/mapred_*;
do
    docker cp $FNAME namenode:/opt/hw1/
done;

rm -f ./outputs/mapred.txt

mapreduce() {
    echo "Preparing files in hdfs for $1"
    docker exec namenode hdfs dfs -rm -r -f /hw1/{input_$1,output_$1}
    docker exec namenode hdfs dfs -mkdir -p /hw1/input_$1
    docker exec namenode hdfs dfs -put -f /opt/hw1/AB_NYC_2019.csv /hw1/input_$1/

    echo "Running mapreduce for $1"
    docker exec namenode mapred streaming \
        -D mapred.map.tasks=3 \
        -D stream.num.map.output.key.fields=0 \
        -files "/opt/hw1/mapred_$1_mapper.py,/opt/hw1/mapred_$1_reducer.py" \
        -input /hw1/input_$1 \
        -output /hw1/output_$1 \
        -mapper "/usr/bin/python mapred_$1_mapper.py" \
        -reducer "/usr/bin/python mapred_$1_reducer.py"

    docker exec namenode hdfs dfs -getmerge /hw1/output_$1 ./opt/hw1/output_$1.txt
    docker exec namenode cat ./opt/hw1/output_$1.txt >> outputs/mapred.txt
}

mapreduce mean
mapreduce variance
