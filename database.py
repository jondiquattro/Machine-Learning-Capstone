import mysql.connector
                    
mydb = mysql.connector.connect(
  host="localhost",
  user="jonathan",
  passwd="JD#six6",
  database = "NFL"
)

mycursor = mydb.cursor()

year = 1980

for year in range(year, 1981):
    filePath = "/home/jonathan/python/"+ "Team_"+str(year)+".csv"  

# end = " \"\\n\""

  #creat table
    tableName = "Team_year_"+str(year)
    # tableString = "CREATE TABLE "+tableName+ " (Name VARCHAR(50),Team VARCHAR(50),Attempts INT(5),AttemptsPerGame DECIMAL(4,2),TotalYards INT(5),YardsPerCarry DECIMAL(3,2),Yards_Per_Game DECIMAL(6,2),TouchDowns INT(2))"
    
    # filePathString = str("LOAD DATA LOCAL INFILE \""+filePath+"\" INTO TABLE "+tableName+" FIELDS TERMINATED BY \",\" LINES TERMINATED BY" + " \"\\n\"")

##########################  for receiver files####################################
##############################################################################################################
    # tableString = "CREATE TABLE "+tableName+ " (Name VARCHAR(50),Receptions INT(5),Yards INT(5), TDs INT(5))"

    # filePathString = str("LOAD DATA LOCAL INFILE \""+filePath+"\" INTO TABLE "+tableName+" FIELDS TERMINATED BY \",\" LINES TERMINATED BY" + " \"\\n\"")
################################################################################################################


    tableString = "CREATE TABLE "+tableName+ " (Name VARCHAR(50), Team VARCHAR(50),Completions INT(5),Yards INT(5), Attempts DECIMAL(4,2),Yards_Per_Game DECIMAL(6,2),TDs INT(2))"

    filePathString = str("LOAD DATA LOCAL INFILE \""+filePath+"\" INTO TABLE "+tableName+" FIELDS TERMINATED BY \",\" LINES TERMINATED BY" + " \"\\n\"")
    delete = "DELETE FROM "+tableName+ " WHERE Team = 'Team'"

    # query = "",delete,""

    mycursor.execute(tableString)
    print(filePathString)
# mycursor.execute(filePathString)





    # print(query)