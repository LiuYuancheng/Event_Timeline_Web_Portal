#-----------------------------------------------------------------------------
# Name:        timelineApp.py
#
# Purpose:     The main monitor application to start other module, insert data 
#              to the score database and update the topology panel in Grafana. 
#              
# Author:      Yuancheng Liu
#
# Version:     v_0.1
# Created:     2023/04/27
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import os
import json

from flask import Flask, Response, request, render_template, jsonify
import appGlobal as gv
import Log

import dataManager

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

gv.iDataMgr = dataManager.DataManager(None, fetchMode=False)


#-----------------------------------------------------------------------------
# web home request handling functions.
@app.route('/')
def index():
    Log.info('/index.html is accessed from IP: %s' %str(request.remote_addr))
    return render_template('index.html')

@app.route('/timeline')
def show_timeline():
    timeLineList = gv.iDataMgr.getTimelineJson()
    return render_template("timeline.html", posts = timeLineList)

#-----------------------------------------------------------------------------
# Data post request handling 
@app.route('/dataPost/<string:uuid>', methods=('POST',))
def add_message(uuid):
    content = request.json
    gv.gDebugPrint("Get raw data from %s "%str(uuid), logType=gv.LOG_INFO)
    gv.gDebugPrint("Raw Data: %s" %str(content['rawData']), prt=False, logType=gv.LOG_INFO)
    gv.iDataMgr.updateRawData(uuid, json.loads(content['rawData']))
    return jsonify({"ok":True})

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,  debug=False, threaded=True)

