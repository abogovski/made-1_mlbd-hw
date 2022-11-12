cd $(dirname $0)

docker exec namenode mkdir /hw2
docker cp ./data/artists.csv namenode:/hw2/artists.csv
docker exec namenode hadoop fs -mkdir -p /hw2
docker exec namenode hadoop fs -put /hw2/artists.csv /hw2/artists.csv
