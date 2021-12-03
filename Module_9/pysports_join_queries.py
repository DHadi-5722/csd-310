import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "root",
    "password": "Flammenwerfer1994",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
    cursor = db.cursor()
    cursor.execute('SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ')
   

    players= cursor.fetchall()
    
    #cursor.execute('SELECT team_id, team_name, mascot FROM team')
    #teams = cursor.fetchall()
    #cursor.execute('SELECT player_id, first_name, last_name, team_id FROM player')
    #players = cursor.fetchall()
    #print("--DISPLAYING TEAM RECORDS--")
    #for team in teams:
        #print('Team ID:  {}'
        #.format(team[0]))
        #print('Team Name: {}'
        #.format(team[1]))
        #print('Mascot: {}'
        #.format(team[2]))
        #print()
    print("--DISPLAYING PLAYER RECORDS--")
    for member in players:
        print('Player ID:  {}'
        .format(member[0]))
        print('First Name: {}'
        .format(member[1]))
        print('Last Name: {}'
        .format(member[2]))
        print('Team Name: {}'
        .format(member[3]))
        print()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
        db.close()      
