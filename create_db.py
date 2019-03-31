import sqlite3
import config
import os

def create_db():
    conn = sqlite3.connect(config.db_filename)
    
    c = conn.cursor()
    
    # parsed data

    c.execute("CREATE TABLE Users(User_Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username text, Description text, Password text)")
    c.execute("CREATE TABLE Leaderboards(Lb_Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, User_Id INTEGER , Name text, Description text, Genre text , FOREIGN KEY (User_Id) REFERENCES Users(User_Id))")
    c.execute("CREATE TABLE Ranking(Ranking_Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Lb_Id INTEGER , Name text, Score text, FOREIGN KEY (Lb_Id) REFERENCES Leaderboards(Lb_Id))")

    # user test data

    c.execute("INSERT INTO Users(Username, Description, Password) VALUES('Kitty Jacobs','Student at Immaculata Institute', 'aaa')")
    # c.execute("INSERT INTO Users VALUES(2, 'Peeters', 'Willy')")
    c.execute("INSERT INTO Leaderboards(Name, User_Id, Description, Genre) VALUES('MoviesLeaderboard', 1, 'haha', 'Movies1')")
    # c.execute("INSERT INTO Antwoorden VALUES(2, 1, '5.1.1', 'We weten nu dat een relationele databank een verzameling is van tabellen met relaties tussen.', '2019-03-13')")
    # c.execute("INSERT INTO Antwoorden VALUES(3, 2, '5.1.1', 'Een relationele databank is een verzameling van tabellen met relaties tussen.', '2019-03-13')")

    conn.commit()
    c.close()
    