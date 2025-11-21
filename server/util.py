import numpy as np
import pickle
import json

__data_columns=None
__model=None
__scaler=None


def get_data_columns():
    return __data_columns

def get_prediction(age,sex,cp,resting_bp,cholesterol,fasting_bs,resting_ecg,maxhr,exercise_angina,oldpeak,slope):
    input_data=np.array([[age,sex,cp,resting_bp,cholesterol,fasting_bs,resting_ecg,maxhr,exercise_angina,oldpeak,slope]])
    scaleing_input=__scaler.transform(input_data)
    prediction =__model.predict(scaleing_input)

    if prediction[0] > 0.5:
        return "The Person Is Having Heart Disease"
    else:
        return "The Person Does Not Have Heart Disease"

def load_saved_artifacts():
    print('Loading saved artifacts...start')

    global __data_columns
    global __model
    global __scaler

   
    with open('./artifactes/Heart_Disease_columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']

    with open('./artifactes/Heart_Disease.pickle','rb')as f:
        __model=pickle.load(f)

    with open('./artifactes/HD_scaler.pickle','rb') as f:
        __scaler=pickle.load(f)

    print('Loading saved artifacts...done')

if __name__=='__main__':
    load_saved_artifacts()
    print(get_data_columns())