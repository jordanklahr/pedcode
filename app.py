#from flask import Flask, render_template, redirect, url_for, request
#from datetime import datetime, timedelta
#import json
#import os

#app = Flask(__name__)

#@app.route('/')
#def hello():
#     return 'Hello World!'



# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():


    response = {}


    # Return the response in json format
    return jsonify(response)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
