import sqlite3
import config
import models
from flask import g

db_filename = config.db_filename

def get_db():
    if 'conn' not in g:
        g.conn = sqlite3.connect(db_filename)    
    return g.conn

def get_users():
    conn = get_db()
    cs = []
    for row in conn.execute("SELECT * FROM Users"):
        c = models.Leaderboard()
        c.User_Id = row[0]
        c.Username = row[1]
        c.Description = row[2]
        c.Password = row[3]
        cs.append(c)
    return cs

def get_leaderboards():
    conn = get_db()
    cs = []
    for row in conn.execute("SELECT * FROM Leaderboards"):
        c = models.Leaderboard()
        c.Lb_Id = row[0]
        c.User_Id = row[1]
        c.Name = row[2]
        c.Description = row[3]
        c.Genre = row[4]
        cs.append(c)
    return cs