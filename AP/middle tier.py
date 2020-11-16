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

@app.route('/')
def CalculationLogic():
    op1 = request.form['op1']
    op2 = request.form['op2']
    opr = request.form['opr']
    resp = Calculate(op1,op2,opr)
    jsonResp = json.dumps({'resp':resp})
    return jsonResp


if __name__ == "__main__":
    app.run(port=2000)