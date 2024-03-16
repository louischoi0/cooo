import redis
import psycopg2
import json
from time import sleep
from coofunc import _item_schedule_func
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

def get_redis_connection():
    host = '43.202.45.111'
    port = 6379
    return redis.Redis(host=host, port=port, decode_responses=True, password='a02040608')

def get_db_connection():
    DB_HOST = "wwhale-on-gpt.cg6x7yqwsa6m.ap-northeast-2.rds.amazonaws.com"
    DB_USER = "postgres"
    DB_PASS = "a!02040608"
    DB_NAME = "pangtimo"

    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
    )

def push_itemlog_schedule(cursor, redis):
    sql = """
    select id, uuid, citem_id, keyword from itemlog_schedules;
    """

    cursor.execute(sql)
    data = cursor.fetchall()

    for d in data:
        k = '#'.join( str(x) for x in d )
        print('push: ', k)
        redis.rpush('cqueue', k)

def get_itemlog_schedule(redis):
    d = redis.lrange('cqueue',0, 10)
    print(d)

def _worker(cursor, redis):
    interval = 10

    while True:     
        task = redis.lpop('cqueue')
        print(task)

        if task is None:
            sleep(interval)
            continue

        _id, uuid, citem_id, keyword = task.split('#')
        _item_schedule_func(keyword=keyword, item_id=citem_id)

        sleep(interval)

def produce_dag_func():
    con = get_db_connection()
    cursor = con.cursor()
    redis = get_redis_connection()
    push_itemlog_schedule(cursor, redis)
    con.close()
    redis.close()

with DAG(   
        dag_id='coupang_viewhistory_curltask', 
        schedule_interval=timedelta(minutes=5),
        start_date=datetime(2023, 3, 16, 9, 30),
        catchup=False
    ) as dag:

    python_task = PythonOperator(
        task_id='run_my_function',
        python_callable=produce_dag_func,  
        dag=dag,
    )
