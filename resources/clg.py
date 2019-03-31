import numpy as np
import pandas as pd
import sqlite3
from werkzeug.security import safe_str_cmp
from flask_restful import Resource, reqparse
from models.user import UserModel

class CollegeData(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('caste',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('university',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('department',
        type=str,
        required=True,
        help="This field cannot be blank."
    )   

    parser.add_argument('merit',
        type=int,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('gender',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def get(self):
        df = pd.read_csv('pict_comp.csv')
        return{"data" :df['GOPENH'].to_json(orient='values')}


    


    def post(self):
        data = CollegeData.parser.parse_args()
        df = pd.read_csv('data.csv')
        cb =pd.read_csv('combine.csv')
        category = ''
        
        if data and safe_str_cmp(data.gender, 'male'):
            category = 'G'
        if data and safe_str_cmp(data.gender, 'female'):
            category = 'L'
        category = category + data['caste']

        if data and safe_str_cmp(data.university, 'home'):
            category = category + 'H'
        if data and safe_str_cmp(data.university, 'other'):
            category = category + 'O'
        # return {'data': category}

        merit= data['merit']
        years=[2013,2014,2015,2016,2017,2018]
        ndf=df[(df[category]>merit) & (df['Branch Name']==data['department'])].head(10)
        ndf=ndf[['Code','Name','Branch No.',category]].sort_values(by=category)

        y1=[]
        for y in years:
            for x in ndf['Branch No.']:
                y1.append(int(cb[category][(cb['Branch No.']==x )& (cb['Year']==y)]))

        
        for x,y in zip(range(0,60,10),years):
            ndf[y]=y1[x:x+10]

        ndf.rename(columns={category:'2019'})

        return{'data': ndf.to_json(orient='records')}
        
