from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)
model = pickle.load(open("pickle.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
	return render_template("a1.html")



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
    	problemSolving = request.form["f1"]
    	programming = request.form["f2"]
    	coding = request.form["f3"]
    	daa = request.form["f4"]
    	cn = request.form["f5"]
    	maths = request.form["f6"]
    	ca = request.form["f7"]
    	se = request.form["f8"]
    	os = request.form["f9"]
    	dk = request.form["f10"]
    	ek = request.form["f11"]
    	cskills = request.form["f12"]
    	lskills = request.form["f13"]
    	isub = request.form["f14"]
    	if(isub=='i1'):

    		iot=1
    		imang =0
    		ise =0
    		icc=0
    		ide=0
    		ih=0
    		isn=0
    		ipc=0
    		ip=0
    	elif(isub=='i2'):
    		iot=0
    		imang =1
    		ise =0
    		icc=0
    		ide=0
    		ih=0
    		isn=0
    		ipc=0
    		ip=0
    	elif(isub=='i3'):
    		iot=0
    		imang =0
    		ise =1
    		icc=0
    		ide=0
    		ih=0
    		isn=0
    		ipc=0
    		ip=0
    	elif(isub=='i4'):
    		iot=0
    		imang =0
    		ise =0
    		icc=1
    		ide=0
    		ih=0
    		isn=0
    		ipc=0
    		ip=0
    	elif(isub=='i5'):
    		iot=0
    		imang =0
    		ise =0
    		icc=0
    		ide=1
    		ih=0
    		isn=0
    		ipc=0
    		ip=0
    	elif(isub=='i6'):
    		iot=0
    		imang =0
    		ise =0
    		icc=0
    		ide=0
    		ih=1
    		isn=0
    		ipc=0
    		ip=0
    	elif(isub=='i7'):
    		iot=0
    		imang =0
    		ise =0
    		icc=0
    		ide=0
    		ih=0
    		isn=1
    		ipc=0
    		ip=0
    	elif(isub=='i8'):
    		iot=0
    		imang =0
    		ise =0
    		icc=0
    		ide=0
    		ih=0
    		isn=0
    		ipc=1
    		ip=0
    	elif(isub=='i9'):
    		iot=0
    		imang =0
    		ise =0
    		icc=0
    		ide=0
    		ih=0
    		isn=0
    		ipc=0
    		ip=1
    	prediction = model.predict([[
    			os,daa,programming,se,cn,
    			ek,ca,maths,cskills,problemSolving,lskills,
    			dk,coding,iot,imang,ise,icc,ide,ih,isn,ipc,ip
    		]])
    	predictors =['Applications Developer','Business Intelligence Analyst','Business Systems Analyst','CRM Business Analyst',
    	'CRM Technical Developer','Data Architect','Database Administrator','Database Developer','Database Manager','Design & UX',
    	'E-Commerce Analyst','Information Security Analyst','Information Technology Auditor','Information Technology Manager',
    	'Mobile Applications Developer','Network Engineer','Network Security Administrator','Network Security Engineer',
    	'Portal Administrator','Programmer Analyst','Project Manager','Quality Assurance Associate','Software Developer',
    	'Software Engineer','Software Quality Assurance (QA) / Testing','Software Systems Engineer','Solutions Architect',
    	'Systems Analyst','Systems Security Administrator','Technical Engineer','Technical Services/Help Desk/Tech Support',
    	'Technical Support','UX Designer','Web Developer']
    	return render_template('output.html',output="Your career prediction is {}".format(predictors[int(prediction)]))


    return render_template("a1.html")






if __name__ == "__main__":
	app.run(debug=True)
