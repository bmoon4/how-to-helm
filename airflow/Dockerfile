FROM apache/airflow:2.2.4

RUN pip install apache-airflow-providers-apache-spark

USER root

ENV AIRFLOW_HOME=/opt/airflow \
    AIRFLOW_DAGS=/opt/airflow/dags \
    AIRFLOW_SPARK_JARS=/opt/airflow/jars

RUN mkdir -p $AIRFLOW_SPARK_JARS

# Install java-11
RUN apt-get update \
  && apt-get install -y openjdk-11-jdk \
  && apt-get install -y ant \
  && apt-get install -y vim \
  && apt-get install -y --no-install-recommends \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copy sample .jar and .py dag files into $AIRFLOW_DAGS , $AIRFLOW_SPARK_JARS
COPY dags/spark_test.py $AIRFLOW_DAGS/spark_test.py
COPY dags/test.py $AIRFLOW_DAGS/test.py
COPY jars/spark-examples_2.12-3.2.1.jar $AIRFLOW_SPARK_JARS/spark-examples_2.12-3.2.1.jar

# Set JAVA_HOME; need Java to run Spark. Make sure this version matches the one on Spark
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
RUN export JAVA_HOME && \
    echo 'JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> /etc/environment && \
    source /etc/environment

USER airflow
