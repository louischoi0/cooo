from curltask import _worker, get_db_connection, get_redis_connection

if __name__ == "__main__":
    con = get_db_connection()
    cursor = con.cursor()
    redis = get_redis_connection()

    _worker(cursor, redis)