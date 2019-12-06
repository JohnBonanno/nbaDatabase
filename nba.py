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
        print ("Press 4 to filter players by position ")
        print ("Press 0 to exit")


        completedItemNumber = 0                                 ##updates with each completion

        num = int(input("Please select an option: "))            ##reads choice for menu option
        

        if num==1: 
            print ("")      

            cursor.execute("""SELECT team.team_name FROM team""")  ##see all team names

            for (team_name) in cursor:                              ##print all team names
                print(f'{team_name}')
                            
        elif num==2: #see all players on team read from stdin
            print ("")
            teamName = input("Please enter a team name to view: ")              
            print("")
                                                                        #select all team names of name : <input>, display player and team name
            cursor.execute("""SELECT Player.fname, Player.lname, team.team_name 
                            FROM team
                            INNER JOIN Player on team.id = Player.team_id
                            WHERE team.team_name = %s""", (teamName,))

            for (fname,lname,team_name) in cursor:
                print(f'{fname} {lname}')


        elif num==3:
            print ("")                                                       #show name ht, wt, team name of heaviest or tallest players
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
        
        elif num==4:
            print ("")
                
            choose = input("Please enter the position of the players you wish to see: ")
                                                                                            #selects player,team name, jersey no, and home state of player 
            cursor.execute("""SELECT Player.fname,Player.lname,team.team_name,Player.jersey_num, Player.home_state 
                        FROM team
                        INNER JOIN Player on team.id = Player.team_id
                        WHERE Player.position = %s""", (choose,))

            for (fname,lname,team_name,jersey_num,home_state) in cursor:
                print("")
                print(f'{fname} {lname} of the {team_name } wearing jersey number {jersey_num} of {home_state}')




        elif num==0:
            response=0
        else:
            print ("no such menu option")
            print ("no such menu option")



    #break
except mysql.connector.Error as err:
    print(err)
else:   
    # Invoked if no exception was thrown
    cnx.close()
