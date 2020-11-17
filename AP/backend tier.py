# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cvYKam7yxToFQPhxtXu6T77tiWft8ark
"""

from flask import Flask, request
import json

List=[[]]*0

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Storing():
    req = json.loads(request.json)
    List.append(req)
    print(req)

@app.route('/view', methods=['GET', 'POST'])
def View():
    if(len(List)==0):
        return "No Previous Calculation"
    if(len(List)<5):
        return str(List[::-1][:len(List)])
    return str(List[::-1][:5])


    
if __name__ == "__main__":
  app.run(port=3000)