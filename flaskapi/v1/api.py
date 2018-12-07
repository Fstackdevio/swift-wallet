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
import netifaces
# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
import requests

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


connection = config.connection()
mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
dbconn = connection.startConnection()
handler = iohandler.Ioapi()
api = Api(app)
cursor = dbconn.cursor()

class Test(Resource):
    def post(self):
        return jsonify({'success': "working"})

class logout(Resource):
    def post(self):
        session.pop('regno', None)
        session.pop('userid', None)
        return jsonify({'StatusCode' : '200', 'message':'logged Out'})

class Authenticate(Resource):
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno','password']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']
            __password = req_data['password']

            gws=netifaces.gateways()
            loginLocation = gws['default'].values()[0][0]

            if __regno in session:
                return jsonify({'StatusCode' : '200', 'message':'sessionActive'})

            cursor.execute("SELECT COUNT(1) FROM custormers WHERE regno = {};".format(__regno))

            if not cursor.fetchone()[0]:
                return jsonify({'StatusCode' : '201', 'message':'Invalid username'})



            cursor.execute("SELECT userid, password FROM custormers WHERE regno = {};".format(__regno))
            

            for row in cursor.fetchall():
                # if hashlib.md5(__password).hexdigest()  == row[1]:
                if __password  == row[1]:
                    session['regno'] = __regno
                    session['userid'] = row[0]
                    arrayVal = str([loginLocation,loginLocation,1])
                    arrayTable = ['routerIp','userIp','loginStatus']
                    valType = [%s,%s,%s]
                    query = handler.insertArr(arrayVal, arrayTable, valType,'TraceLogin')

                    return jsonify({'StatusCode' : '200', 'message':'successfull', 'sessionId':session['userid'], "sessionRegno":session['regno']})

                else:
                    arrayVal = [loginLocation,loginLocation,0]
                    arrayTable = ['routerIp','userIp','loginStatus']
                    valType = [%s,%s,%s]
                    query = handler.insertArr(arrayVal, arrayTable, valType, 'TraceLogin')

                    return jsonify({'StatusCode':'201', 'message':'Invalid password'})
        
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'StatusCode' : '400', 'message':'Invalid json input'})

        
class Auth2(Resource):
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno','password']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']
            __password = req_data['password']

            url = 'https://att.lmu.edu.ng/login/login' # Set destination URL here
            data = {'username': __regno, 'password':__password}     # Set POST fields here
            request = Request(url, urlencode(data).encode())
            json = urlopen(request).read().decode()
            # print(json)
            if json.data == True:
                session['regno'] = __regno
                session['userid'] = json.userid
                return jsonify({'StatusCode' : '200', 'message':json.message, 'sessionId':session['userid'], "sessionRegno":session['regno']})
            else:
                return jsonify({'StatusCode' : '201', 'message':json.message})
                
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'StatusCode' : '400', 'message':'Invalid json input'})


class spendingHistory(Resource):
    """docstring for depositHistory"""
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']

            cursor.execute("SELECT locationId,amount,userId,merchantiD,dateCreated FROM spending WHERE userid = {};".format(__regno))
            data = cursor.fetchall()

            if not data:
                return jsonify({'StatusCode' : '200', 'message':'NO record for this user'})


            items=[];
            for item in data:
                i = {
                    'locationId':item[0],
                    'amount':item[1],
                    'userId':item[2],
                    'merchantiD':item[3],
                    'dateCreated':item[4]
                }
                items.append(i)

            # return {'StatusCode':'200','Items':items_list}
            return jsonify({'StatusCode' : '200', 'Items':items})
            

            
        
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})


class transferHistory(Resource):
    """docstring for depositHistory"""
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']

            cursor.execute("SELECT amount,fromWho,toWho,isCrime,approved,dateTransferd FROM transfers WHERE userid = {};".format(__regno))
            data = cursor.fetchall()

            if not data:
                return jsonify({'StatusCode' : '200', 'message':'NO record for this user'})


            items=[];
            for item in data:
                i = {
                    'amount':item[0],
                    'fromWho':item[1],
                    'toWho':item[2],
                    'isCrime':item[3],
                    'approved':item[4],
                    'dateTransferd':item[5]
                }
                items.append(i)

            # return {'StatusCode':'200','Items':items_list}
            return jsonify({'StatusCode' : '200', 'Items':items})
            

            
        
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})


class depositHistory(Resource):
    """docstring for depositHistory"""
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']

            cursor.execute("SELECT amount, depositLocation, depositType, depositorName, dateDeposited FROM deposit WHERE userid = {};".format(__regno))
            data = cursor.fetchall()
            if not data:
                return jsonify({'StatusCode' : '200', 'message':'NO record for this user'})
            items=[];
            for item in data:
                i = {
                    'amount':item[0],
                    'ItdepositLocationem':item[1],
                    'depositType':item[2],
                    'depositorName':item[3],
                    'dateDeposited':item[4]
                }
                items.append(i)

            # return {'StatusCode':'200','Items':items_list}
            return jsonify({'StatusCode' : '200', 'Items':items})            
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})

class loginHistory(Resource):
    """docstring for depositHistory"""
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']

            cursor.execute("SELECT routerIp,userIp,loginStatus,ldate FROM TraceLogin WHERE userid = {};".format(__regno))
            data = cursor.fetchall()

            if not data:
                return jsonify({'StatusCode' : '200', 'message':'NO record for this user'})

            items=[];
            for item in data:
                i = {
                    'routerIp':item[0],
                    'userIp':item[1],
                    'loginStatus':item[2],
                    'logindate':item[3]
                }
                items.append(i)
            return jsonify({'StatusCode' : '200', 'Items':items})
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})

class dashboardInfo(Resource):
    """docstring for dashboardInfo"""
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']

            cursor.execute("SELECT amount FROM deposit WHERE userid = {};".format(__regno))
            Tdeposit = sum(sum(x) for x in cursor.fetchall())

            cursor.execute("SELECT amount FROM spending WHERE userid = {};".format(__regno))
            Tspent = 0 if not cursor.fetchall() else sum(sum(x) for x in cursor.fetchall())

            cursor.execute("SELECT amount FROM transfers WHERE userid = {};".format(__regno))
            Ttransfers = 0 if not cursor.fetchall() else sum(sum(x) for x in cursor.fetchall())

            cursor.execute("SELECT activated FROM custormers WHERE regno = {};".format(__regno))
            flag = cursor.fetchone()[0]

            cursor.execute("SELECT amount,depositLocation,depositType,depositorName,dateDeposited FROM deposit WHERE userid = {} ORDER BY dateDeposited DESC LIMIT 1;".format(__regno))
            lastDeposited = cursor.fetchone()

            cursor.execute("SELECT amount,fromWho,toWho,approved,dateTransferd FROM transfers WHERE userid = {} ORDER BY dateTransferd DESC LIMIT 1;".format(__regno))
            lastTransfer = "no lastTransfer record" if not cursor.fetchone() else cursor.fetchone()

            cursor.execute("SELECT locationId,amount FROM spending WHERE userid = {} ORDER BY dateCreated DESC LIMIT 1;".format(__regno))
            spending =  cursor.fetchone()

            cursor.execute("SELECT routerIp,userIp,loginStatus,ldate FROM TraceLogin WHERE userid = {} ORDER BY ldate DESC LIMIT 1;".format(__regno))
            lastLocation = "no lastTransfer record" if not cursor.fetchone() else cursor.fetchone()

            if not Tdeposit:
                return jsonify({'StatusCode' : '200', 'message':'NO record for this user'})
            
            Llocation = {
                'routerIP': lastLocation[0],
                'userIP': lastLocation[1],
                'loginStatus': lastLocation[2],
                'ldate': lastLocation[3]
            }

            Ldeposited = {
                'amount': lastDeposited[0],
                'location': lastDeposited[1],
                'depositType': lastDeposited[2],
                'depositorName': lastDeposited[3],
                'dateDeposited': lastDeposited[4]
            }

            Ltransfer = {
                'amount': lastTransfer[0],
                'fromWho': lastTransfer[1],
                'toWho': lastTransfer[2],
                'approved': lastTransfer[3],
                'dateTransferd': lastTransfer[4]
            }

            items=[];            
            i = {
                'currentBalance': (Tdeposit) - (Tspent+Ttransfers),
                'flag':flag,
                'lastDeposited': Ldeposited,
                'lastTransfer':Ltransfer,
                'lastLoginLocation':Llocation,
                'lastTransactionLocation': spending[0],
                'lastAmountSpent': spending[1]
            }

            items.append(i)
            return jsonify({'StatusCode' : '200', 'data':items})
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})
        
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

class makeDeposit1(Resource):
    def post(self):
        try:
            req_data = request.get_json(force=True)
            expectedFields = ['regno']
            missing = handler.checkJson(expectedFields,req_data)
            if missing:
                return jsonify({'StatusCode' : '200', 'Missing field': missing})
            __regno = req_data['regno']
            __amount = req_data['amount']
            __cpl = req_data['cpl']

            cursor.execute("SELECT amount FROM deposit WHERE userid = {};".format(__regno))
            Tdeposit = sum(sum(x) for x in cursor.fetchall())

            cursor.execute("SELECT amount FROM spending WHERE userid = {};".format(__regno))
            Tspent = 0 if not cursor.fetchall() else sum(sum(x) for x in cursor.fetchall())

            cursor.execute("SELECT amount FROM transfers WHERE userid = {};".format(__regno))
            Ttransfers = 0 if not cursor.fetchall() else sum(sum(x) for x in cursor.fetchall())

            currentBalance = (Tdeposit) - (Tspent+Ttransfers)
            incremented = currentBalance + __amount

            arrayVal = str([__regno,__amount,__cpl,1,'cashpoint'])
            arrayTable = ['userid','amount','depositLocation','status','depositType']
            valType = [%s,%s,%s,%s,%s]
            query = handler.insertArr(arrayVal, arrayTable, valType,'deposit')
            if query == 'success':
                return jsonify({'StatusCode' : '200', 'data':'success'})
            else:
                return jsonify({'StatusCode' : '201', 'data':'error'})            
        
        except Exception as e:
            return {'error': str(e)}
        except TypeError:
            return jsonify({'status' : '400', 'message':'Invalid json input'})
