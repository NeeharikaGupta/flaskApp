from flask import *
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'detail'
 
mysql = MySQL(app)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        book = request.form['book']
        cursor = mysql.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS detail")
        cursor.execute("USE detail")
        cursor.execute("CREATE TABLE IF NOT EXISTS info_table(name VARCHAR(100) NOT NULL PRIMARY KEY,book_name VARCHAR(100))")
        cursor.execute("INSERT INTO info_table VALUES(%s,%s)",(name,book))
        mysql.connection.commit()
        cursor.close()
        return f"Added successfully"
 

if __name__ == '__main__':  
   app.run(host='0.0.0.0')  




