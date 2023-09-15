from flask import Flask,render_template,url_for,request,redirect,session
import pickle
import os
import re
from newsapi import NewsApiClient

app=Flask(__name__)
    

@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template('index.html')


@app.route('/submit.html',methods=['POST','GET'])
def submit():
    return render_template('submit.html')


@app.route('/result',methods=['GET','POST'])
def Predict():
    if request.method =="POST":

        ID=request.form['ID']
        Gender=request.form['Gender']
        Age=request.form['Age']
        Height=request.form['Height(cm)']
        Weight=request.form['Weight(kg)']
        Eyesight_right=request.form['Eyesight (right)'] 
        Eyesight_left=request.form['Eyesight (left)']
        Hearing_right=request.form['Hearing (right)']
        Hearing_left=request.form['Hearing (left)'] 
        Waist=request.form['Waist(cm)']
        Hemoglobin=request.form['Hemoglobin']
        ALT=request.form['ALT']
        gtp=request.form['gtp']
        systolic=request.form['systolic']
        relaxation=request.form['relaxation']
        fasting_blood_sugar=request.form['fasting blood sugar']
        Cholesterol=request.form['Cholesterol']
        triglyceride=request.form[ 'triglyceride']
        urine_protein=request.form['urine protien'] 
        HDL=request.form['HDL']
        LDL=request.form['LDL']
        oral=request.form['oral']
        dental_caries=request.form['dental caries']
        serum_creatinine=request.form['serum creatinine']
        AST=request.form['AST']
        tartar=request.form['tartar']

    Pred = [[float (ID), float (Gender), float (Age), float (Height), float (Weight), float (Eyesight_right), float (Eyesight_left), float (Hearing_right),float(Hearing_left), float (Waist), float (Hemoglobin), float (ALT), float (gtp), float(systolic), float (relaxation), float (fasting_blood_sugar),float(Cholesterol),float(triglyceride),float(urine_protein), float (HDL), float(LDL), float (oral), float(dental_caries), float(serum_creatinine), float (AST),float(tartar)]]
    model = pickle.load(open('Estimating The Presence or Absence of Smoking Through Bio-Signals.pkl', 'rb'))
    species=model.predict(Pred)[0]
    return render_template('/result.html',Predict=species)
if __name__=='__main__':
    app.run(debug=True)