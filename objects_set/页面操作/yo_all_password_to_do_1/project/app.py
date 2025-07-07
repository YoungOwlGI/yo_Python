from flask import Flask, render_template, request, redirect, url_for, session, flash 
from flask_mysqldb import MySQL 
from config import Config 
 
app = Flask(__name__)
app.config.from_object(Config) 
 
# MySQL配置 
app.config['MYSQL_CURSORCLASS']  = 'DictCursor'
mysql = MySQL(app)
 
# 模拟用户数据 - 实际应用中应该使用数据库存储用户信息 
USERS = {
    'admin': 'password123'
}
 
@app.route('/') 
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    cur = mysql.connection.cursor() 
    cur.execute("SELECT  * FROM yo_all_password")
    passwords = cur.fetchall() 
    cur.close() 
    return render_template('yo_all_password_crud.html',  passwords=passwords)
 
@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method  == 'POST':
        username = request.form['username'] 
        password = request.form['password'] 
        
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True 
            session['username'] = username 
            flash('登录成功!', 'success')
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误!', 'danger')
    
    return render_template('login.html') 
 
@app.route('/logout') 
def logout():
    session.pop('logged_in',  None)
    session.pop('username',  None)
    flash('您已成功登出', 'success')
    return redirect(url_for('login'))
 
@app.route('/add',  methods=['GET', 'POST'])
def add_password():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    if request.method  == 'POST':
        name = request.form['name'] 
        url = request.form['url'] 
        username = request.form['username'] 
        password = request.form['password'] 
        note = request.form['note'] 
        
        cur = mysql.connection.cursor() 
        cur.execute(""" 
            INSERT INTO yo_all_password (name, url, username, password, note)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, url, username, password, note))
        mysql.connection.commit() 
        cur.close() 
        
        flash('密码记录添加成功!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add.html') 
 
@app.route('/edit/<int:id>',  methods=['GET', 'POST'])
def edit_password(id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    cur = mysql.connection.cursor() 
    
    if request.method  == 'POST':
        name = request.form['name'] 
        url = request.form['url'] 
        username = request.form['username'] 
        password = request.form['password'] 
        note = request.form['note'] 
        
        cur.execute(""" 
            UPDATE yo_all_password 
            SET name = %s, url = %s, username = %s, password = %s, note = %s 
            WHERE id = %s 
        """, (name, url, username, password, note, id))
        mysql.connection.commit() 
        cur.close() 
        
        flash('密码记录更新成功!', 'success')
        return redirect(url_for('index'))
    
    cur.execute("SELECT  * FROM yo_all_password WHERE id = %s", (id,))
    password = cur.fetchone() 
    cur.close() 
    
    if not password:
        flash('记录未找到!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('edit.html',  password=password)
 
@app.route('/delete/<int:id>') 
def delete_password(id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    cur = mysql.connection.cursor() 
    cur.execute("DELETE  FROM yo_all_password WHERE id = %s", (id,))
    mysql.connection.commit() 
    cur.close() 
    
    flash('密码记录已删除!', 'success')
    return redirect(url_for('index'))
 
if __name__ == '__main__':
    app.secret_key  = Config.SECRET_KEY 
    app.run(debug=True)