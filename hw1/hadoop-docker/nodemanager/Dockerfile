FROM bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
