from dotenv import load_dotenv
import os
import mysql.connector
from flask import Flask, render_template

# .envファイルを読み込む
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),  # 環境変数からDBのホストを取得
            user=os.getenv('DB_USER'),  # 環境変数からDBのユーザー名を取得
            password=os.getenv('DB_PASSWORD'),  # 環境変数からDBのパスワードを取得
            database=os.getenv('DB_NAME')  # 環境変数からDBのデータベース名を取得
        )
        print("Database connection established")
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise

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

# メインプログラム
if __name__ == '__main__':
    app.run(debug=True)
