from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta
from daglibs.etl_job import post_tweet, stage_tweets, commit_tweets
from daglibs.topic_tweet import delete_all_tweets
import sys
import os

sys.path.append(os.path.dirname(__file__))

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'vijay',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 2),
    'email': ['vjgupta57@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}
    

dag = DAG('PostTweet',schedule_interval=timedelta(hours=8), default_args=default_args)


# This dag will stage all the tweets to the csv file
t1 = PythonOperator(
    task_id='stage_tweets',
    python_callable=stage_tweets,
    dag=dag)


#This Dag will commit all the tweets to the csv file
t2 = PythonOperator(
    task_id='commit_tweets',
    python_callable=commit_tweets,
    dag=dag)

# # This dag is used to send the tweets to twitter
# t3 = PythonOperator(
#     task_id='post_status',
#     python_callable=post_tweet,
#     dag=dag)

# Backup all the files and tweets to google drive
# t4 = PythonOperator(
#     task_id='task_4',
#     python_callable='echo "Hello World from Task 4"',
#     dag=dag)


t1.set_downstream(t2)
