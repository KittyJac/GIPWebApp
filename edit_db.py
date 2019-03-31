import sqlite3
import config
import os
import cgi
import leaderboard_db

def add_leaderboard(titleLeaderboardInput, descriptionInput, genreInput, authorInput):
    conn = sqlite3.connect(config.db_filename)
    
    c = conn.cursor()

    titleLeaderboard = titleLeaderboardInput
    description = descriptionInput
    genre = genreInput
    author = authorInput

    users = leaderboard_db.get_users()

    for user in users:
        if user.Username == author:
            c.execute("INSERT INTO Leaderboards(Name, User_Id, Description, Genre) VALUES('"+ titleLeaderboard +"', "+ user.User_Id +", "+ description +", "+ genre +")")
        else:
            c.execute("INSERT INTO Leaderboards(Name, User_Id, Description, Genre) VALUES('"+ titleLeaderboard +"', "+ (len(users) + 1) +", "+ description +", "+ genre +")")
 
    #c.execute("INSERT INTO Users(Username, Description, Password) VALUES('Kitty Jacobs','Student at Immaculata Institute', 'aaa')")

    conn.commit()
    c.close()