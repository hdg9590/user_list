import pymysql
import os
import json

def lambda_handler(event, context):
    connection = pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        connect_timeout=5
    )

    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, username, coupons FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()

        users = []
        for row in results:
            users.append({
                "id": row[0],
                "username": row[1],
                "coupons": row[2]
            })

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(users)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
    finally:
        connection.close()
