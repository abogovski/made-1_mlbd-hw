for NUM_FEATURES in 10 50 100 500 1000 5000 10000 50000 100000 500000 1000000 2000000 4000000; do
    python3 hw4.py htf $NUM_FEATURES
done
echo
for NUM_FEATURES in 5 10 15 20 25 30; do
    python3 hw4.py w2v $NUM_FEATURES
done
