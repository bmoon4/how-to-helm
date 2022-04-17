FROM apache/airflow:2.2.4

#User root
USER root

# Install OpenJDK-11
# You need to install java to avoid error: `JAVA_HOME is not set`
# Ref: https://stackoverflow.com/questions/67554074/airflow-trigger-spark-in-different-docker-container
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

# User airflow
USER airflow

# Install Spark
RUN pip install apache-airflow-providers-apache-spark --no-cache-dir

WORKDIR /opt/airflow
