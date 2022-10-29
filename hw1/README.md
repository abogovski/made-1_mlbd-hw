# Homework 1

Local stats calculation
```bash
./src/calc_stats.py ./data/AB_NYC_2019.csv > ./outputs/local.txt
```

Hadoop stats calculation
```
# ./hadoop-docker/start.sh
./src/run_mapred.sh # stores result in ./outputs/mapred.
```
