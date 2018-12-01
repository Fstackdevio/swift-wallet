from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)

from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
from functools import wraps
from flask import Flask, jsonify, request, abort, current_app, session, url_for
from config import config as config
from functions import iohandler
from flask_cors import CORS
from flask_inputs.validators import JsonSchema
from functions import fstack_json_schema
import json
import hashlib


connection = config.connection()
mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
dbconn = connection.startConnection()
handler = iohandler.Ioapi()
api = Api(app)
cursor = dbconn.cursor()

 
class logout(Resource):
    def logout():
        session.pop('regno', None)
        session.pop('userid', None)
        return jsonify({'status' : '200', 'message':'logged Out'})

class Authenticate(Resource):
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno','password']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'status' : '200', 'Missing field': missing})
            __regno = req_data['regno']
            __password = req_data['password']


            if __regno in session:
                return jsonify({'status' : '200', 'message':'sessionActive'})

            cursor.execute("SELECT COUNT(1) FROM custormers WHERE regno = {};".format(__regno))

            if not cursor.fetchone()[0]:
                raise Exception('Invalid username')


            cursor.execute("SELECT userid, password FROM custormers WHERE regno = {};".format(__regno))
            

            for row in cursor.fetchall():
                # if hashlib.md5(__password).hexdigest()  == row[1]:
                if __password  == row[1]:
                    session['regno'] = __regno
                    session['userid'] = row[0]
                    return jsonify({'status' : '200', 'message':'successfull', 'sessionId':session['userid'], "sessionRegno":session['regno']})

            raise Exception('Invalid password')
        
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})


class GetAllTrans(Resource):
    def post(self):
        try: 
            req_data = request.get_json(force=True)
            _userId = req_data['id']

            # conn = mysql.connect()
            cursor = dbconn.cursor()
            cursor.callproc('student',(_userId,))
            data = cursor.fetchall()

            items_list=[];
            for item in data:
                i = {
                    'Id':item[0],
                    'Item':item[1]
                }
                items_list.append(i)

            # return {'StatusCode':'200','Items':items_list}
            return jsonify({'StatusCode' : '200', 'Items':items_list})

        except Exception as e:
            # return {'error': str(e)}
            return jsonify({'error': str(e)})        
                

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            # parser = reqparse.RequestParser()
            # parser.add_argument('email', type=str, help='Email address to create user')
            # parser.add_argument('password', type=str, help='Password to create user')
            # args = parser.parse_args()
            req_data = request.get_json(force=True)
            _userEmail = req_data['email']
            _userPassword = req_data['password']

            # conn = mysql.connect()
            cursor = dbconn.cursor()
            cursor.callproc('spCreateUser',(_userEmail,_userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                # return {'StatusCode':'200','Message': 'User creation success'}
                return jsonify({'StatusCode':'200','Message': 'User creation success'})
            else:
                # return {'StatusCode':'1000','Message': str(data[0])}
                return jsonify({'StatusCode':'1000','Message': str(data[0])})

        except Exception as e:
            # return {'error': str(e)}
            return jsonify({'error': str(e)})

class Test(Resource):
    def post(self):
        return jsonify({'success': "working"})

class ReturnResponse(Resource):
    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('name', type=str, help='input your name')
        # parser.add_argument('keyword', type=str, help='input your keyword')
        # args = parser.parse_args()

        # args is use to get from url search = request.args.get("search")
        # email = request.form.get('email') form is use to get form input 

        req_data = request.get_json(force=True)
        # data = request.data     is already depreciated

        __name = req_data['name']
        __keyword = req_data['keyword']

        return jsonify({'success' : 'true', 'name' : __name, 'keyword' : __keyword})

class newData(Resource):
    def post(self):
        req_data = request.get_json(force=True)
        fn = req_data['firstName']
        ln = req_data['lastName']
        pn = req_data['phoneNumber']
        nn = req_data['nickName']


        query = handler.insert('datas', fn, ln, pn, nn)

        if (query == "success"):
            return jsonify({'success' : 'true', 'message' : 'data inserted'})
            # return query
        else:
            return jsonify({'success' : 'false', 'message' : 'data not inserted'})
            # return "error inserting"

class newInsert(Resource):
    def post(self):
        req_data = request.get_json(force=true)

        query = handler.insertArr(arrayVal, arrayTable, 'datas')

        if (query == "success"):
            return jsonify({'success' : 'true', 'message' : 'data inserted'})
            # return query
        else:
            return jsonify({'success' : 'false', 'message' : 'data not inserted'})
            # return "error inserting"

        
        
        