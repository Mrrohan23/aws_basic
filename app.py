from lib2to3.refactor import MultiprocessingUnsupported
from optparse import Values
from flask import Flask
from flask import render_template
from datetime import time
from flaskext.mysql import MySQL
import pymysql
import os

from requests import post


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'rohan'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def sn():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    legend = 'Montly Data'
    cursor.execute("SELECT labels FROM employee")
    labels=cursor.fetchall()
    # cursor.execute("SELECT * FROM employee")
    # values=cursor.fetchall()
    cursor.close()
    return render_template('chart.html',labels=labels,legend=legend)
# app.route('/chart')
# def chart():
#     conn = mysql.connect()
#     cursor = conn.cursor(pymysql.cursors.DictCursor)
#     legend= 'Monthly Data'
#     cursor.execute("SELECT labels,values FROM employee")
#     labels = cursor.fetchall()
   
#     return render_template('demo.html',  labels=labels, legend=legend)


# @app.route("/simple")
# def chart():
#     legend = 'Monthly Data'
#     labels = ["January", "February", "March", "April", "May"]
#     values = [10, 9, 8, 7, 6]
#     return render_template('chart.html', values=values, labels=labels, legend=legend)


@app.route("/l")
def line_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
             '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
             '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    return render_template('line_chart.html', values=temperatures, labels=times, legend=legend)


@app.route("/time_chaar_for react js")
if time.request.method == post
    time(hour=12,minute=23,second=34)
    time(second=23,hour=12,minute=34,microsecond=2345)
    get(time.timeframe=12,time=56)
    get user id of single user 
def time_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = [time(hour=11, minute=14, second=15),
             time(hour=11, minute=14, second=30),
             time(hour=11, minute=14, second=45),
             time(hour=11, minute=15, second=00),
             time(hour=11, minute=15, second=15),
             time(hour=11, minute=15, second=30),
             time(hour=11, minute=15, second=45),
             time(hour=11, minute=16, second=00),
             time(hour=11, minute=16, second=15),
             time(hour=11, minute=16, second=30),
             time(hour=11, minute=16, second=45),
             time(hour=11, minute=17, second=00),
             time(hour=11, minute=17, second=15),
             time(hour=11, minute=17, second=30),
             time(hour=11, minute=17, second=45),
             time(hour=11, minute=18, second=00),
             time(hour=11, minute=18, second=15),
             time(hour=11, minute=18, second=30)]
    return render_template('time_chart.html', values=temperatures, labels=times, legend=legend)
@app.route('line_graph')
def graph():
    if  request.method == post:
        time(hour=11,minute=14,second=15)
        spent(hour=12,MultiprocessingUnsupported=23.5)




if __name__ == "__main__":
    app.run(debug=True)
