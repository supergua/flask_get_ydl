from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = "D:/pythonproj/bs/ydl.db"


def connect_db():
    return sqlite3.connect(DATABASE)


@app.route('/')
def hello_world():
    cx = connect_db()
    last5 = cx.execute("select time,cl2 from o2table order by id DESC limit 5").fetchall()
    cx.close()
    return render_template("index.html", last5=last5)


if __name__ == '__main__':
    app.run()