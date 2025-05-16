import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        os.environ["SUPABASE_URL"],
        sslmode="require"
    )

def execute_sql(query):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            if cur.description:
                return cur.fetchall()
            return None
    finally:
        conn.close()
