# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:05:29 2020

@author: Karthick Balaji
"""

from flask import Flask, redirect, request, render_template

app = Flask(__name__, template_folder = "template")


@app.route('/', methods = ['POST', 'GET'])
def Calc():
    if(request.method=='GET'):
        return render_template('calc.html')
    if(request.method=='POST'):
        Op1 = request.form['op1']
        Op2 = request.form['op2']
        Opr = request.form['opr']
        print(Op1,Opr,Op2)
        Res = float(Op1) + float(Op2)
        #return str(Res)
        return render_template('calc.html', op1=Op1, op2=Op2, opr=Opr, res=Res)
    

if __name__ == "__main__":
    app.run(port=1000)