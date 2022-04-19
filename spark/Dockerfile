FROM bitnami/spark:3.2.1

USER root

RUN apt-get update \
  && apt-get install -y openjdk-11-jdk \
  && apt-get install -y ant \
  && apt-get install -y vim \
  && apt-get install -y --no-install-recommends \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME; need Java to run Spark. Make sure this version matches the one on Airflow
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=/opt/bitnami/python/bin:/usr/lib/jvm/java-11-openjdk-amd64:/opt/bitnami/spark/bin:/opt/bitnami/spark/sbin:/opt/bitnami/common/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN export JAVA_HOME && \
    echo 'JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> /etc/environment && \
    echo 'JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> /opt/bitnami/spark/conf/spark-env.sh

RUN chown 1001 -R /etc/environment && \
    chown 1001 -R /opt/bitnami/spark/conf/spark-env.sh
