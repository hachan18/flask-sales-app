from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/')
def show_sales():
    # 売上一覧を表示
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='alechansumo13',  # 実際に設定しているパスワード
        database='sales_management'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('sales_list.html', sales=rows)

@app.route('/new', methods=['GET', 'POST'])
def new_sale():
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        price = request.form['price']
        sale_date = request.form['sale_date']

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='alechansumo13',
            database='sales_management'
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sales (product_name, quantity, price, sale_date)
            VALUES (%s, %s, %s, %s)
        """, (product_name, quantity, price, sale_date))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('show_sales'))

    # GETメソッドならフォーム表示
    return render_template('new_sale.html')

if __name__ == '__main__':
    app.run(debug=True)
