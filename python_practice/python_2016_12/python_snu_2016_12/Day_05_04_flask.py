# Day_05_04_flask.py
from flask import Flask, render_template
import random
import Day_04_03_sqlite

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, python'

def makeRandoms(count, limit):
    return [random.randrange(limit) for _ in range(count)]

@app.route('/randoms')
def randoms():
    return str(makeRandoms(10, 100))

@app.route('/randoms/<int:count>')
def randomsCount(count):
    return str(makeRandoms(count, 100))

@app.route('/html')
def html():
    ns = makeRandoms(5, 1000)
    return render_template('randoms.html', numbers=ns)

@app.route('/kma')
def kma():
    pusan = Day_04_03_sqlite.fetchWhere('Data/kma.sqlite', '부산')
    return render_template('kma.html',
                           kma=pusan)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# API : Application Programming Interface
# static, templates











