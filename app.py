import os
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

# データベース接続関数
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'db4free.net'),  # 環境変数から取得
            user=os.getenv('DB_USER', 'salesuseranachan'),
            password=os.getenv('DB_PASSWORD', 'your-db-password'),
            database=os.getenv('DB_NAME', 'salesdbanachan')
        )
        print("Database connection established")
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise

# ホームページ: 売上一覧を表示
@app.route('/')
def show_sales():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('sales_list.html', sales=rows)
    except mysql.connector.Error as err:
        return f"Database query error: {err}"

# デバッグ: 接続テスト関数
def test_db_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        print(f"Connected to database: {db_name}")
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(f"Table: {table}")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error during database test: {err}")

# メインプログラム
if __name__ == '__main__':
    # デバッグ用のDB接続テスト
    test_db_connection()
    # Flaskアプリケーションの起動
    app.run(debug=True)
