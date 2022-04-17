
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['sex'])
   inputs.append(request.form['cp'])    
   inputs.append(request.form['fbs'])
   inputs.append(request.form['restecg'])
   
   sex = request.form['sex']
   cp = request.form['cp'] 
   fbs = request.form['fbs']
   restecg = request.form['restecg']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Have Heart Disease"
   if prediction[0] == 0:
        categorical_array = "Not Have Heart Disease"
    
   result= categorical_array
   if sex=="1":
       sex = "Male"
   if sex=="0":
       sex = "Female"
       
   if cp=="0":
       cp = "Typical Angina"
   if cp=="1":
       cp = "Atypical Angina"
   if cp=="2":
       cp = "non-Anginal Pain"
   if cp=="3":
       cp = "Asymptomatic"
     
   if fbs=="1":
       fbs = "True"
   if fbs=="0":
       fbs = "False"
       
   if restecg=="0":
       restecg = "Normal"
   if restecg=="1":
       restecg = "Having ST-T wave abnormality"
   if restecg=="2":
       restecg = "Showing Probable"
       
   return render_template('Home.html', prediction_text1=result, sex11 = sex, cp1=cp, fbs1=fbs, restecg1=restecg)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)