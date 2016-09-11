import os
import sqlite3
from flask import Flask,redirect, render_template, request
app = Flask(__name__)

conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS short_routes (id INTEGER PRIMARY KEY AUTOINCREMENT, alias text, url text)")
#c.execute("DROP TABLE short_routes")
c.execute("CREATE TABLE IF NOT EXISTS short_routes (id INTEGER PRIMARY KEY AUTOINCREMENT, alias text UNIQUE, url text)")
conn.commit()

@app.route('/')
def index():

    con = sqlite3.connect("example.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from short_routes")

    rows = cur.fetchall();
    return render_template('mini_routes.html', rows = rows)

@app.route('/add_new_route', methods=['GET', 'POST'])
def add_new_route():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    alias = request.form['alias']
    url = request.form['url']
    c.execute("INSERT OR REPLACE INTO short_routes (alias) VALUES (?)", (alias,))
    c.execute("UPDATE short_routes SET url=? WHERE alias=?", (url, alias))
    conn.commit()
    return redirect('/', code = 302)


@app.route('/<alias>')
def redir(alias):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    redirect_url = c.execute("SELECT url FROM short_routes WHERE alias=?", (alias,)).fetchone()
    return redirect('%s' % redirect_url, code = 302)

@app.route('/delete/<entry>')
def delete(entry):
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    cur.execute("DELETE FROM short_routes WHERE alias = ?", (entry,))
    con.commit()
    return redirect('/', code = 302)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = 80)
