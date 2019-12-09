wimport mysql.connector


try:
    cnx = mysql.connector.connect(
        user='token_2a45',
        host='127.0.0.1',
        database='jab0629_todo',
        password = 'FUyhsk7DV9adpJpV'
    )

    cursor = cnx.cursor()
    response = 1
    print ("Welcome to statistical calculator")
   # while (response > 0):
       
   #     print ("to do items:")
   #     query = f"""SELECT id, name, description
   #                 FROM todo
   #         """
   #     cursor.execute(query)
       
   #
   #     for (id, name, description) in cursor:
   #         print(f'{id} - {name} : {description}')
        

    print ("Main Menu:")
    print ("Press 1 to show the team with the best field goal percentage")
    print (" ")
    print ("")
    print ("")
        #query from completed table
    print ("Press 5 to show statistics")
    print ("Press 0 to exit")
    num = int(input("Please select an option :"))
        
    if num==1:
        itemName = input("THE <enter team name> : ")
        
        cursor.execute("""SELECT team.name, team.fgPercentage
                        FROM player"""
        for (player.first, player.last, player.position, player.team) in cursor:
            print(f'{first} {last} {position} {team}')i
        
    if num==2:
        pointsScored = f"""SELECT player.first, player.last, games.pointsScored
                        FROM  player
                        INNER JOIN games
                        ON games.playedInID = player.id
                        ORDER BY games.pointsScored
                    """
    cursor.execute(pointsScored)


    for (player.first, player.last, games.pointsScored) in cursor:
            print(f'{first} {last} max points scored: {pointsScored}')
    if num==3:
        print ("Most shots blocked in a single game:")

        pointsScored = f"""SELECT player.first, player.last, games.shotsBlocked
                        FROM player
                        INNER JOIN games
                        ON games.playedInID = player.id
                        ORDER BY games.shotsBlocked DESC LIMIT 1
                    """
    cursor.execute(pointsScored)
    for (player.first, player.last, games.pointsScored) in cursor:
    print(f'{first} {last} {position} {team}')



    elif num==0:
        response=0
    else:
        print ("no such menu option")



#break
except mysql.connector.Error as err:
print(err)
else:   
# Invoked if no exception was thrown
cnx.close()
