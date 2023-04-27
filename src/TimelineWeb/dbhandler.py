#-----------------------------------------------------------------------------
# Name:        dbBaseHandler.py
#
# Purpose:     This program is used to reset the dataBase and test the querys.
#              
# Author:      Yuancheng Liu 
#
# Version:     v_0.2
# Created:     2023/04/20
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import os
import json
import time
from random import randint
from werkzeug.security import generate_password_hash

from appGlobal import DB_PATH, SQL_PATH, dirpath, gRaw_TimelineTB
from databaseHandler import Sqlite3Cli

connection = Sqlite3Cli(DB_PATH, databaseName = "Raw_DataBase")

def addEventInfo():
    timelineExampleJson = os.path.join(dirpath, 'timeLineExample.json')
    with open(timelineExampleJson, 'r') as f:
        evtJsonList = json.load(f)
        for item in evtJsonList:
            print("Insert test data.")
            evtTitle = item['evtTitle']
            dayNum = int(item['dayNum'])
            evtType = item['evtType']
            teamName = item['teamName']
            teamType = item['teamType']
            evtState = item['evtState']
            querStr = 'INSERT INTO %s (evtTitle, dayNum, evtType, teamName, teamType, evtState) VALUES (?, ?, ?, ?, ?, ?)' %str(gRaw_TimelineTB)
            paramters = (evtTitle, dayNum, evtType, teamName, teamType, evtState)
            connection.executeQuery(querStr, paramList=paramters)
            time.sleep(randint(5, 10))

def addUsers():
    usersList = [
        ('admin', '123', 0, 0 ),
        ('BlackTeam', '123', 0, 1),
        ('GreenTeam', '123', 1, 2),
        ('GreenTeam', '123', 2, 3),
        ('BlueTeam01', '123', 2, 4),
        ('BlueTeam02', '123', 2, 4),
        ('BlueTeam03', '123', 2, 4),
    ]    
    for item in usersList:
        userName = item[0]
        pwdHash = generate_password_hash(str(item[1]), method='sha256')
        authority = int(item[2])
        userType = int(item[3])
        querStr = 'INSERT INTO users (userName, pwdHash, authority, userType) VALUES (?, ?, ?, ?)'
        paramters = (userName, pwdHash, authority, userType)
        connection.executeQuery(querStr, paramList=paramters)

def testCase(mode):
    print('Mode: %s' %str(mode))
    if mode == 0:
        print("Reset DB and test insert data")
        connection.executeScript(SQL_PATH)
    elif mode == 1:
        print("Reset DB and test insert data")
        connection.executeScript(SQL_PATH)
        print('Add user and team')
        addUsers()
        print('Add the event info.')
        addEventInfo()
    elif mode == 2:
        querStr = 'SELECT * FROM %s ORDER BY updateT DESC LIMIT 10' %str(gRaw_TimelineTB)
        connection.executeQuery(querStr)
        result = connection.getCursor().fetchall()
        print(result)
    else:
        pass
        # Add your test code here and change the mode part to active it.
    connection.close()

if __name__ == '__main__':
    mode = 1
    testCase(mode)
