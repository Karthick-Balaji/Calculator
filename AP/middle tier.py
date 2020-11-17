# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:02:38 2020

@author: Karthick Balaji
"""

from flask import Flask, request
import requests,json

def Calculate(op1,op2,opr):
    op1 = float(op1)
    op2 = float(op2)
    if(opr == '+'):
        res = op1+op2
    elif(opr == '-'):
        res = op1-op2
    elif(opr == '*'):
        res = op1*op2
    elif(opr == '/'):
        res = op1/op2
    return res

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def CalculationLogic():
    req = json.loads(request.json)
    op1 = req['op1']
    op2 = req['op2']
    opr = req['opr']
    result = Calculate(op1,op2,opr)
    print(result)
    req = {'op1': op1,'opr' : opr,'op2' : op2}
    requests.post('http://localhost:3000/', json=request.json)
    return str(result)

@app.route('/view', methods=['GET', 'POST'])
def View():
    response = requests.post('http://localhost:3000/view')
    resp = response.text
    return resp
    


if __name__ == "__main__":
    app.run(port=2000)
