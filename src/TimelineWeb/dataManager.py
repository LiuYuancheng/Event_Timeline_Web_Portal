#-----------------------------------------------------------------------------
# Name:        dataManager.py
#
# Purpose:     This module the manager module to process and archive all the 
#              incoming data. 
#              
# Author:      Yuancheng Liu
#
# Version:     v0.1
# Created:     2023/03/15
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import os
import time
import json
import threading
from random import randint
from datetime import datetime

import appGlobal as gv
from databaseHandler import Sqlite3Cli

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class DataManager(object):
    """ The data manager is a module running parallel with the main thread to 
        handle the data-IO with dataBase and the monitor hub's data fetching/
        changing request.
    """
    def __init__(self, parent, fetchMode=True, timeInterval=30) -> None:
        #threading.Thread.__init__(self)
        self.parent = parent
        self.rawDBhandler = Sqlite3Cli(gv.DB_PATH, databaseName = gv.gRawDBName, threadSafe=False)

    #-----------------------------------------------------------------------------
    def getTimelineJson(self):
        querStr = 'SELECT * FROM %s ORDER BY updateT DESC LIMIT 10' %str(gv.gRaw_TimelineTB)
        self.rawDBhandler.executeQuery(querStr)
        reuslt = self.rawDBhandler.getCursor().fetchall()
        timelintList = []
        for item in reuslt:
            eventJson = {
                'title' : "Day%02d:%s" %(item[3], str(item[1])),
                'tagSide': 'right',
                'timeStr': item[2],
                'evtType': item[4],
                'team':item[5],
                'teamType': item[6],
                'contents': item[7],
                'htmlStr': None
            }
            timelintList.append(eventJson)
        return timelintList
