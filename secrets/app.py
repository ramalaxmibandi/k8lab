import os
from flask import Flask, request, render_template, mysql

app = Flask(__name__)

color = 'red'
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PWD =os.environ.get('DB_PWD')
@app.route("/")
def main():
    mysql.connector.connect(host=DB_HOST, database='mysql', user=DB_USER, password=DB_PWD)
    return render_template('render.html', color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
