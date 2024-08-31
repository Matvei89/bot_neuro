import sqlite3
def connect():
    con =sqlite3.connect('1.db')
    return con

def table():
    con = connect()
    cursor =con.cursor()
    cursor.execute('create table if not exists users(chat_id integer,balance integer default 5)')

def add_user(chat_id):
    con = connect()
    cursor = con.cursor()
    cursor.execute('select * from users where chat_id = ?',(chat_id,))
    if not cursor.fetchall():
        cursor.execute('insert into users (chat_id) values (?)',(chat_id,))
        con.commit()
def balance(chat_id):
    con = connect()
    cursor = con.cursor()
    cursor.execute('select balance from users where chat_id = ?', (chat_id,))
    return cursor.fetchone()[0]
def update_balance(balance,chat_id):
    con = connect()
    cursor = con.cursor()
    cursor.execute("UPDATE users SET balance = ? WHERE chat_id = ?", (balance, chat_id))
    con.commit()
    return balance