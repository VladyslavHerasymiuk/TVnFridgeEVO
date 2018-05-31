from flask import Flask, render_template, request, json
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1111'
app.config['MYSQL_DB'] = 'Goods'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def signUp():
    return render_template('index.html')


@app.route('/list', methods=['POST'])
def signUpUser():
    cur = mysql.connection.cursor()
    category = request.form['category']
    cur.execute("select g.id, c.name, g.clicks_count, g.name from goods as g " 
                "inner join categories as c on c.id = g.category_id where c.id = '{}';".format(category))
    data = cur.fetchall()

    return json.dumps({'data': data}), 200, {'ContentType':'application/json'}

@app.route('/click', methods=['POST'])
def click():
    cur = mysql.connection.cursor()
    id = request.form['id']
    cur.execute("UPDATE goods SET clicks_count = clicks_count + 1 WHERE id = '{}';".format(id))
    mysql.connection.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/sorted_data', methods=['POST'])
def SortedData():
    cur = mysql.connection.cursor()
    id = request.form['category']
    cur.execute("select g.id, c.name, g.clicks_count, g.name from goods as g " 
                "inner join categories as c on c.id = g.category_id where c.id = '{}' ORDER BY g.clicks_count DESC;".format(id))
    data = cur.fetchall()

    return json.dumps({'data': data}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(debug=True)