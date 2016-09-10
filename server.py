import os
import sqlite3
from flask import Flask,redirect, render_template, request
app = Flask(__name__)

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS short_routes (id INTEGER PRIMARY KEY AUTOINCREMENT, alias text, url text)")
conn.commit()
#users_map = {"/bea" => "https://www.messenger.com/t/bea.subion"}

@app.route('/')
def index(): 
    return render_template('mini_routes.html')

@app.route('/add_new_route', methods=['GET', 'POST'])
def add_new_route():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    alias = request.form['alias']
    url = request.form['url']
    c.execute("INSERT INTO short_routes (alias, url) VALUES (?,?)",(alias, url))
    conn.commit()
    return redirect('/', code = 302)

@app.route('/bea')
def bea():
    return redirect("https://www.messenger.com/t/bea.subion", code = 302)

@app.route('/<alias>')
def redir(alias):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    redirect_url = c.execute("SELECT url FROM short_routes WHERE alias=?", (alias,)).fetchone()
    return redirect('%s' % redirect_url, code = 302)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
