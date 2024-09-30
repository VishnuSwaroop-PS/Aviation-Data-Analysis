from flask import Flask, render_template, jsonify, send_file
import os
import mysql.connector
from data_analysis import generate_plots

app = Flask(__name__)

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="aviation_data"
    )
    return conn


@app.route('/')
def index():
    generate_plots()
    return render_template('index.html')

@app.route('/plot/<plot_name>')
def plot(plot_name):
    plot_path = os.path.join('plots', f'{plot_name}.png')
    return send_file(plot_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)