from datetime import timedelta, datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
		'owner': 'Moon',
		'start_date': datetime(2022, 3, 4),
		'retries': 3,
		'retry_delay': timedelta(minutes=1)
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

hello_spark_task = SparkSubmitOperator(
    task_id="spark",
    conn_id="spark_default",
    java_class="org.apache.spark.examples.SparkPi",
    application="/opt/bitnami/spark/examples/jars/spark-examples_2.12-3.2.1.jar",
    application_args=["5"],
    dag=dag
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag
    )

start_task >> hello_spark_task >> end_task
