# -*- coding: utf-8 -*-
import pandas as pd
from flask import Flask, request
from flask_cors import CORS

head = ['StateAbbr','Lack of Health Insurance','Arthritis','Binge Drinking','High Blood Pressure','Blood Pressure Medication','Cancer','Asthma','Coronary Heart Disease','Annual Checkup','Cholesterol Screening','Colonoscopy','Chronic obstructive pulmonary disease','Preventive Services (Older Men)','Preventive Services (Older Women)','Smoking','Dental Visit','Diabetes','High Cholesterol','Kidney Disease','Physical Inactivity','Mammography','Poor Mental Health','Obesity','Cervical Cancer Screening','Poor Physical Health','Sleep < 7 hrs','Stroke','Teethlost']

def dataFormat():
    global head
    df = pd.read_csv('CDC_for_map.csv')
    df_state = df[head]
    return df_state


def formatData(sharch):
    global head
    data = dataFormat()

    arr = []

    for index in range(len(data)):
        obj = {}
        obj['address'] = data['StateAbbr'][index]

        obj['key'] = data[sharch][index]
        arr.append(obj)

    return arr


app = Flask(__name__)

# 127.0.0.1:5000
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    sharch = request.json.get("sharch")
    return formatData(sharch)


# 127.0.0.1:5000/list
@app.route('/list')
def list():
    return head


if __name__ == '__main__':
    #
    CORS(app, supports_credentials=True)
    app.run(debug=True, port=int("5000"))