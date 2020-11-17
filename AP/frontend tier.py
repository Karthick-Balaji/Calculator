# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:05:29 2020

@author: Karthick Balaji
"""

from flask import Flask, request, render_template, redirect
import requests,json

app = Flask(__name__, template_folder = "template")


@app.route('/', methods = ['POST', 'GET'])
def CalculationUI():
    if(request.method=='GET'):
        return render_template('calc.html')
    
    if(request.method=='POST'):
        if(request.form['submit']=='Submit'):
            Op1 = request.form['op1']
            Op2 = request.form['op2']
            Opr = request.form['opr']
            req = {'op1': Op1,'opr' : Opr,'op2' : Op2}
            jsonReq = json.dumps(req)
            response = requests.post('http://localhost:2000/', json=jsonReq)
            resp = response.text
            return render_template('calc.html', op1=Op1, op2=Op2, opr=Opr, res=resp)
        
        if(request.form['submit']=='View'):
            return redirect('http://localhost:1000/view')

@app.route('/view', methods = ['POST', 'GET'])
def View():
    response = requests.post('http://localhost:2000/view')
    resp = response.text
    return resp


if __name__ == "__main__":
    app.run(port=1000)
