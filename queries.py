import mysql.connector
                    
mydb = mysql.connector.connect(
  host="localhost",
  user="jonathan",
  passwd="JD#six6",
  database = "NFL"
)

year =1980

###############needs work
def teamTableMaker(year):
    for year in range(year, 2018):

        tableName = "WR_Year_"+str(year)               #''Name','Receptions','Yards', 'ReceivingTDs'       
        tableString = "CREATE TABLE "+tableName+ " (Name VARCHAR(50),Team VARCHAR(50), Receptions INT(5), Yards INT(5), TDs INT(2))"
        mycursor = mydb.cursor()

        mycursor.execute(tableString)

        mydb.commit()
teamTableMaker(year)


def populateTeamData(year):


    for year in range(year, 2018):
        filePath = "/home/jonathan/python/"+"RECEIVER"+str(year)+".csv" 
          
        tableName = "WR_Year_"+str(year)

        filePathString = str("LOAD DATA LOCAL INFILE \""+filePath+"\" INTO TABLE "+tableName+" FIELDS TERMINATED BY \",\" LINES TERMINATED BY" + " \"\\n\"")
        

        mycursor = mydb.cursor()

        mycursor.execute(filePathString)

        mydb.commit()
        # print(filePathString)
populateTeamData(year)

def sortQB(year):

    for year in range(year, 1983):
        length = 0
        tableName = "QB_year_"+str(year)

        mycursor = mydb.cursor()
        print(tableName)
        
        mycursor.execute("SELECT Name, Completions, team FROM "+tableName+ " ORDER BY Completions DESC")

        myresult = mycursor.fetchall()

        while (length < 10):
            print(myresult[length])
            length += 1

# sortQB(year)

def sortRB(year):

    for year in range(year, 1983):
        length = 0
        tableName = "year_"+str(year)

        mycursor = mydb.cursor()
        print(tableName)
        
        mycursor.execute("SELECT Name, Team, TotalYards, TouchDowns FROM "+tableName+ " ORDER BY TotalYards DESC")

        myresult = mycursor.fetchall()

        while (length < 10):
            print(myresult[length])
            length += 1
# sortRB(year)

def sortTeam(year):
        for year in range(year, 1983):
            length = 0
            tableName = "Team_year_"+str(year)

            mycursor = mydb.cursor()
            print(tableName)
            mycursor.execute("SELECT Team, TotalYards FROM "+tableName)
            
            # mycursor.execute("SELECT Team, TotalYards, AttemptsPerGame, YardsPerCarry, TDs FROM "+tableName+ " ORDER BY YardsPerCarry DESC")

            myresult = mycursor.fetchall()

            while (length < 10):
                print(myresult[length])
                length += 1
# sortTeam(year)



# def pointCalculator(rushyards, touchDowns):
#     rushYardsPoints = rushyards / 10
#     touchDownPoints = touchDowns * 6
#     # pointsOffreception = receptionYards / 20
#     totalPoints = rushYardsPoints + touchDownPoints
#     print(totalPoints)
#     return totalPoints
# pointCalculator(yards, td)


def deleteTableContents(year):
    for year in range(year, 2018):

        tableName = "Te_Year_"+str(year)                     
        tableString = "DROP TABLE "+tableName
        mycursor = mydb.cursor()

        mycursor.execute(tableString)

        mydb.commit()
# deleteTableContents(year)