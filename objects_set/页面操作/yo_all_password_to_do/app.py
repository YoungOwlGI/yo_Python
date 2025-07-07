# app.py  
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# 数据库配置 
db_config = {
    'user': 'root',
    'password': 'xiaomty',
    'host': 'localhost',
    'database': 'youngowl',
    'raise_on_warnings': True
}


def get_db_connection():
    """建立数据库连接"""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"数据库连接错误: {e}")
        return None


@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT  * FROM yo_all_password")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', data=data)
    return "数据库连接失败"


@app.route('/add', methods=['POST'])
def add():
    data = request.form
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = """
                INSERT INTO yo_all_password
                    (cn_name, name, url, username, password, note)
                VALUES (%s, %s, %s, %s, %s, %s) \
                """
        values = (
            data['cn_name'],
            data['name'],
            data['url'],
            data['username'],
            data['password'],
            data['note']
        )
        try:
            cursor.execute(query, values)
            conn.commit()
        except Error as e:
            conn.rollback()
            print(f"插入错误: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        data = request.form
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = """
                    UPDATE yo_all_password
                    SET cn_name=%s, \
                        name=%s, \
                        url=%s, \
                        username=%s, \
                        password=%s, \
                        note=%s
                    WHERE id = %s \
                    """
            values = (
                data['cn_name'],
                data['name'],
                data['url'],
                data['username'],
                data['password'],
                data['note'],
                id
            )
            try:
                cursor.execute(query, values)
                conn.commit()
            except Error as e:
                conn.rollback()
                print(f"更新错误: {e}")
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('index'))
    else:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT  * FROM yo_all_password WHERE id=%s", (id,))
            data = cursor.fetchone()
            cursor.close()
            conn.close()
            return render_template('edit.html', data=data)
        return "数据库连接失败"


@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE  FROM yo_all_password WHERE id=%s", (id,))
            conn.commit()
        except Error as e:
            conn.rollback()
            print(f"删除错误: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True) 