from flask import Flask,request, jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

import util

@app.route('/data_columns')
def get_data_columns():
    response=jsonify({
        'data_columns': util.get_data_columns()
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_heart_disease',methods=['POST'])
def predict_heart_disease():
    try:
       age=float(request.form['age'])
       sex=float(request.form['sex'])
       chestpain=float(request.form['chestpain'])
       resting_bp=float(request.form['resting_bp'])
       cholesterol=float(request.form['cholesterol'])
       fasting_bs=float(request.form['fasting_bs'])
       resting_ecg=float(request.form['resting_ecg'])
       maxhr=float(request.form['maxhr'])
       exercise_angina=float(request.form['exercise_angina'])
       oldpeak=float(request.form['oldpeak'])
       slope=float(request.form['slope'])

       prediction=util.get_prediction(age,sex,chestpain,resting_bp,cholesterol,fasting_bs,resting_ecg,maxhr,exercise_angina,oldpeak,slope)

       response=jsonify({
           'Prediction': prediction
       })
    
       response.headers.add('Access-Control-Allow-Origin','*')
       return response
    
    except Exception as e:
        return jsonify({'error': str(e)})        

if __name__=='__main__':
    print('Starting server....')
    util.load_saved_artifacts()
    app.run()
