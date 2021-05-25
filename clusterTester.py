from os import ctermid
from neo4j import GraphDatabase
from ctInitialise import CT_PROMPT, CT_MENU, ctInit

def main():
    dbConnectDefMap = {}
    dbConnectInputMap = {}

    sel = "1"
    dbConnectDefMap = ctInit()
    dbConnectInputMap = dbConnectDefMap.copy()
    helpString = CT_MENU + CT_PROMPT

    sel = input (helpString)
   
    while sel != "0":
        if sel == "1":
            inputData = input("Insert URI (nothing to use default): ")
            if (inputData != ""): 
                    dbConnectInputMap['uri'] = inputData
            inputdata = input ("Insert the database name (nothing to use default): ")
            if (inputData != ""): 
                    dbConnectInputMap['database'] = inputData
            inputData = input ("Insert the username (nothing to use default): ")
            if (inputData != ""):
                dbConnectInputMap['username'] = inputData
            inputData = input ("Insert password (nothing for default): ")
            if (inputData != ""):
                dbConnectInputMap['password'] = inputData
            try:
                driver = GraphDatabase.driver(dbConnectInputMap['uri'], auth=( dbConnectInputMap['username'] , dbConnectInputMap['password']))
            except Exception as driverExcObj:
                print (">>>>>> Error connecting to the database : ", str(driverExcObj))

        elif sel == "2":
                print ("Disconnecting from ")
        elif sel == "3":
                print ("Initiate RO Transaction")
        elif sel == "4":
                print ("Initiate RW Transaction")
        elif sel == "5":
                print ("Committing")
        elif sel == "6":
                print ("Rollback")
        elif sel == "7":
                print ("Insert your query")
        print (" You selected ", sel)    
        sel = input (helpString )


    print ("Bye")
    driver.close()
main()
