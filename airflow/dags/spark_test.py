from datetime import datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
		'owner': 'Moon',
		'start_date': datetime(2022, 3, 4),
}

# Instantiate a DAG object
dag = DAG('hello_spark_dag',
		default_args=default_args,
		description='SparkSubmitOperator DAG',
		schedule_interval='@once',
		catchup=False,
		tags=['example, spark']
)

start_task = DummyOperator(
    task_id='start_task',
    dag=dag
    )

submit_job = SparkSubmitOperator(
    conn_id="spark_default",
    java_class="org.apache.spark.examples.SparkPi",
    application="/opt/airflow/dags/jars/spark-examples_2.12-3.2.1.jar", # deploy-mode : client
    #application="/opt/bitnami/spark/examples/jars/spark-examples_2.12-3.2.1.jar", # deploy-mode : cluster -> does not work
    task_id="submit_job",
    application_args=["1"],
    verbose=True,
    name='SparkPi',
    executor_cores=2,
    num_executors=2,
    driver_memory="600m",
    executor_memory="600m",
    dag=dag
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag
    )

start_task >> submit_job >> end_task
