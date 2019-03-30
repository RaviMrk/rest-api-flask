# import numpy as np
# import pandas as pd
# import sqlite3
# from werkzeug.security import safe_str_cmp
# from flask_restful import Resource, reqparse
# from models.user import UserModel

# class CollegeData(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('caste',
#         type=str,
#         required=True,
#         help="This field cannot be blank."
#     )

#     parser.add_argument('university',
#         type=str,
#         required=True,
#         help="This field cannot be blank."
#     )

#     parser.add_argument('department',
#         type=str,
#         required=True,
#         help="This field cannot be blank."
#     )   

#     parser.add_argument('merit',
#         type=int,
#         required=True,
#         help="This field cannot be blank."
#     )

#     parser.add_argument('gender',
#         type=str,
#         required=True,
#         help="This field cannot be blank."
#     )



#     def get(self):
#         df = pd.read_csv('pict_comp.csv')
#         return{"data" :df['GOPENH'].to_json(orient='values')}


#     def post(self):
#         caste = ''
#         data = CollegeData.parser.parse_args()
#         if data and safe_str_cmp(data.gender, 'male'):
#             caste = 'G'
#         if data and safe_str_cmp(data.gender, 'female'):
#             caste = 'L'
#         caste = caste + data['caste']

#         if data and safe_str_cmp(data.university, 'home'):
#             caste = caste + 'H'
    

#         return{'data': caste}
        
