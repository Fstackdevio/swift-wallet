import pymysql as MySQLdb
# from flask.ext.mysql import MySQL
from flaskext.mysql import MySQL
from flask import Flask
from flask_restful import Resource, Api
class connection():
	def __init__(self):
		self.host = "localhost"
		self.username = "root"
		self.password = ""
		self.dbname = "easywallet"
		self.app = Flask(__name__)

	def startConn(self):
		Dbconn = MySQLdb.connect(self.host, self.username, self.password, self.dbname)
		return Dbconn

	def startConnection(self):
		mysql = MySQL()
		# MySQL configurations
		self.app.config['MYSQL_DATABASE_USER'] = self.username
		self.app.config['MYSQL_DATABASE_PASSWORD'] = self.password
		self.app.config['MYSQL_DATABASE_DB'] = self.dbname
		self.app.config['MYSQL_DATABASE_HOST'] = self.host
		mysql.init_app(self.app)
		Dbconn = mysql.connect()
		return Dbconn
