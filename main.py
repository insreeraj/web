### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)

model = pickle.load(open('model.pkl','rb'))


@app.route('/')


def welcome():
    return render_template('index.html')

# @app.route('/submit',methods=['POST','GET'])
# def submit():
#     total_score=0
#     if request.method=='POST':
#         science=float(request.form['science'])
#         maths=float(request.form['maths'])
#         c=float(request.form['c'])
#         data_science=float(request.form['datascience'])
#         total_score=(science+maths+c+data_science)/4

#         output = model.predict()
#     res=""
#     return redirect(url_for('success',score=total_score))


@app.route('/index',methods=['POST'])
def predict():
    total_score=0
    if request.method=='POST':
        ##age, job, marital, education, default, 
        # balance, housing, loan, contact, day, month, 
        # duration, campaign, pdays, previous, poutcome
        custmername = request.form['Name']
        age = float(request.form['Age'])
        job = float(request.form['Job'])
        marital = float(request.form['MartialStatus'])
        education = float(request.form['Education'])
        default = float(request.form['Loandefault'])
        balance = float(request.form['Balance'])
        housing = float(request.form['Housing'])
        loan = float(request.form['AnyOtherLoans'])
        contact = float(request.form['Contact'])
        day = float(request.form['Day'])
        month = float(request.form['Month'])
        duration = float(request.form['Duration'])
        campaign = float(request.form['NoOfCampaigns'])
        pdays = float(request.form['DaysAfterPreviouscampaign'])
        previous = float(request.form['NoOfPreviousContacts'])
        poutcome = float(request.form['PreviousOutcome'])

        input_variables = pd.DataFrame([[age, job, marital, education, default, 
        balance, housing, loan, contact, day, month, 
        duration, campaign, pdays, previous, poutcome]],
        columns=['age','job','marital','education','default', 
        'balance','housing','loan','contact','day','month', 
        'duration','campaign','pdays','previous','poutcome'], dtype=float, index=['input'])    
        prediction = model.predict(input_variables)  
        prediction = prediction[0] 
        result =" "
        if prediction==1:
            result="Customer {name}  will take Term Loan!!! ".format(name = custmername)
        else:
            result="Customer {name}  will not Take Term Loan!!! ".format(name = custmername)  
    
    return redirect(url_for('.pred',result=result))

@app.route('/index/<string:result>',methods=['GET'])
def pred(result):
    # res=""
    # if result==1:
    #     res="SUCCESS"
    # else:
    #     res="FAIL"
    return render_template('index.html',result=result)


@app.route('/result/<int:score>')
def success(score):
    res=""
    if score==1:
        res="SUCCESS"
    else:
        res="FAIL"

    return render_template('result.html',result=res)







@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4

        output = model.predict()
    res=""
    return redirect(url_for('success',score=total_score))

    



if __name__=='__main__':
    app.run(debug=True)