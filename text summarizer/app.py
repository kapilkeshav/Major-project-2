import requests 
from flask import Flask, render_template, url_for
from flask import request as req
from Summarizer import summarizer
from ai import ai_sum

app = Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def Index():
    return render_template("index.html")

    
@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if 'b1' in req.form:
        data=req.form["data"]
        output = summarizer(data)
    if 'b2' in req.form:
        data=req.form["data"]
        output = ai_sum(data)
    return render_template("index.html", result=output)
        
    

if __name__ == '__main__':
    app.debug=True
    app.run()
