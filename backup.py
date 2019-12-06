import mysql.connector





try:
    cnx = mysql.connector.connect(
        user='token_a2ef',
        host='127.0.0.1',
        database='jab0629_NBA',
        password = 'oTGVlYROiXumBDOk'
    )

    cursor = cnx.cursor()
    response = 1
    print ("")
    print ("Welcome to NBA database client")
    while (response > 0):
        print ("")
        print ("Main Menu:")
        print ("Press 1 to see all teams")
        print ("Press 2 to see all players on a specific team")
        print ("Press 3 to see information about the tallest or heaviest players")
        print ("Press 0 to exit")


        completedItemNumber = 0 ###updates with each completion

        num = int(input("Please select an option: "))
        

        if num==1:
            print ("")             
            cursor.execute("""SELECT team.team_name FROM team""")

            for (team_name) in cursor:
                print(f'{team_name}')
                            
        elif num==2:
            print ("")
            teamName = input("Please enter a team name to view: ")
            print("")
            cursor.execute("""SELECT Player.fname, Player.lname, team.team_name 
                            FROM team
                            INNER JOIN Player on team.id = Player.team_id
                            WHERE team.team_name = %s""", (teamName,))

            for (fname,lname,team_name) in cursor:
                print(f'{fname} {lname}')


        elif num==3:
            print ("")
            choose = input("Please enter either height or weight to see the three tallest or heaviest players: ")
            if choose=='height':
                cursor.execute("""SELECT Player.fname, Player.lname, Player.heightInCm, Player.weightInLbs, team.team_name 
                            FROM team
                            INNER JOIN Player on team.id = Player.team_id
                            ORDER BY heightInCm DESC limit 3;""")
                for (fname,lname,heightInCm, weightInLbs,team_name) in cursor:
                    print("")
                    print(f'{fname} {lname} of the {team_name } stands tall at: {heightInCm} cm weighing: {weightInLbs} lbs')

            elif choose=='weight':
                cursor.execute("""SELECT Player.fname, Player.lname, Player.heightInCm, Player.weightInLbs, team.team_name 
                            FROM team
                            INNER JOIN Player on team.id = Player.team_id
                            ORDER BY weightInLbs DESC limit 3;""")
                for (fname,lname,heightInCm, weightInLbs,team_name) in cursor:
                    print("")
                    print(f'{fname} {lname} of the {team_name } stands tall at: {heightInCm} cm weighing: {weightInLbs} lbs')
        
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
