from flask import *
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'detail'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('form.html')
 
@app.route('/view', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Register into the community using book form available"
     
    if request.method == 'POST':
        name = request.form['name']
        book = request.form['book']
        author = request.form['author']
        cursor = mysql.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS detail")
        cursor.execute("USE detail")
        cursor.execute("CREATE TABLE IF NOT EXISTS information(name VARCHAR(100) NOT NULL PRIMARY KEY,book_name VARCHAR(100) NOT NULL,author VARCHAR(100) NOT NULL)")
        cursor.execute("INSERT INTO information VALUES(%s,%s,%s)",(name,book,author))
        mysql.connection.commit()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("Select name,book_name From information")
        rows=cursor.fetchall()

        return render_template('view.html',rows=rows)
 

if __name__ == '__main__':  
   app.run(host='0.0.0.0')  



#comment
#comment2
#comment
