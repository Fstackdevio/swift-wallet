from inspect import getsourcefile
import os.path
import sys
import socket
import fcntl
import struct

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)


import pymysql as MySQLdb
# from flask.ext.mysql import MySQL
from flaskext.mysql import MySQL
import sys
import hashlib
from config import config as config

class Ioapi():
	def __init__(self):
		try:
			classuse = config.connection()
			self.db = classuse.startConn()
			cur = self.db.cursor()
		except MySQLdb.Error, e:
		    print "Error %d: %s" % (e.args[0],e.args[1])
		    print "error err errr error"
		    sys.exit(1)
		# finally:
		#     if self.db:
		# 		self.db.close()

	# check json data
	def checkJson(self, expectedFields,data):
		if not data:
			return 'data'
		for f in expectedFields:
			try:
				data[f]
			except:
				return f

	#INSERT ARRAY 
	def insertArr(self, arrayVal, arrayTable, valuetype, table):
		with self.db:
			cur = self.db.cursor()
    		sql = "INSERT INTO " + table + '(' + ','.join([(e) for e in arrayTable]) + ') ' + "VALUES" + '(' + ','.join([(e) for e in valuetype]) + ')'
	        cur.execute(sql, arrayVal)
	        if cur.lastrowid:
	        	cur.commit()
	        	cursor.close()
	        	return "success"
	        else:
	        	cur.commit()
	        	return "error"

  	def insert(self, table, fields=(), values=()):
		# g.db is the database connection
		cur = self.db.cursor()
		query = '''INSERT INTO %s (%s) VALUES (%s)''' % (
			table,
			', '.join(fields),
			', '.join(['?'] * len(values))
		)
		cur.execute(query, values)
		g.db.commit()
		lid = cur.lastrowid
		cur.close()
		return lid

	def insertv2(self, query, values):
		# g.r is the database connection
		cur = self.db.cursor()
		cur.execute(query, values)
		self.db.commit()
		lid = cur.lastrowid
		cur.close()
		return lid

	#INSERT ROW
	def insertin(self, table, fname, lname, pnum, nname):
		with self.db:
			cur = self.db.cursor()
			sql = '''INSERT INTO table(fn, ln, pn, nn) VALUES(%s, %s, %s, %s)'''
			if (cur.execute(sql, (fname, lname, pnum, nname))):
				return "success"
			else:
				return "error"

	#UPDATE SINGLE ROW
	def lockAccount(self, table, regno, locktype):
		with self.db:
			cur = self.db.cursor()
			sql = 'UPDATE customers SET disabled=%s WHERE regno=%s'
			if (cur.execute(sql, (locktype,regno))):
				self.db.commit()
				return "success"
			else:
				return "error"

	def get_ip():
	    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    try:
	        # doesn't even have to be reachable
	        s.connect(('10.255.255.255', 1))
	        IP = s.getsockname()[0]
	    except:
	        IP = '127.0.0.1'
	    finally:
	        s.close()
	    return IP

	def get_ip_address(ifname):
	    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    return socket.inet_ntoa(fcntl.ioctl(
	        s.fileno(),
	        0x8915,  # SIOCGIFADDR
	        struct.pack('256s', ifname[:15])
	    )[20:24])
	   	#  get_ip_address('eth0')

	def tempupdateQ(self, query, values):
		cur = self.db.cursor()
		cur.execute(query, values)
		self.db.commit()
		cur.close()
		return "success"

	def updateQ(self, sql, values=()):
		with self.db:
			cur = self.db.cursor()
			if (cur.execute(sql, values)):
				self.db.commit()
				return "success"
			else:
				return "error"

	def unLockAccount(self, table, regno):
		with self.db:
			cur = self.db.cursor()
			sql = 'UPDATE table SET disabled=%s WHERE regno=%s'
			if (cur.execute(sql, (0,regno))):
				return "success",  cur.rowcount
			else:
				return "error"

	#GET SINGLE ROW
	def getSingle(self, table, idd):
		with self.db:
			cur = self.db.cursor(MySQLdb.cursors.DictCursor)
			sql = 'SELECT * FROM table WHERE id=%i'
			cur.execute(sql, (idd))
			row = cur.fetch()
			return row

	#DELETE ROW
	def delete(self, table, idd):
		with self.db:
			cur = self.db.cursor()
	        sql = 'DELETE FROM table WHERE Id = %i'
	        cur.execute(sql, (idd))
	        print "row deleted : ", cur.rowcount 


	# CREATE A NEW TABLE and INSERT SOME VALUES
	def createTable(db, tableName):
	    with self.db:
	        cur = self.db.cursor()
	        cur.execute("DROP TABLE IF EXISTS TableTest")
	        sql = 'CREATE TABLE tableName(Id INT PRIMARY KEY AUTO_INCREMENT, \ fn VARCHAR(55), \ ln VARCHAR(55), \ pn INT(15), \ nn VARCHAR(55))'
	        if (cur.execute(sql)):
	        	return "success"
	        else:
	        	return "error"


	# get  ROWS
	def getAll(Table):
	    with self.db:
	        cur = self.db.cursor(MySQLdb.cursors.DictCursor)
	        sql = 'SELECT * FROM Table'
	        cur.execute(sql)
	        rows = cur.fetchall()
	        for row in rows:
	            return row["Id"], row["Name"]


	def sha256(hash_string):
	    sha_signature = \
	    	hashlib.sha256(hash_string.encode()).hexdigest()
	    return sha_signature
		








	
