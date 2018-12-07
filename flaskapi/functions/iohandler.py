from inspect import getsourcefile
import os.path
import sys

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
	def insertArr(self, arrayVal, arrayTable, valuetype table):
		with self.db:
			cur = self.db.cursor()
    		sql = "INSERT INTO " + table + "(" + ','.join([(e) for e in arrayTable]) + ") " + "VALUES" + "(" + ','.join([(e) for e in valuetype]) + ")"
	        cur.execute(sql, arrayVal)
	        if cur.lastrowid:
	        	cur.commit()
	        	cursor.close()
	            return "success"
	        else:
	        	cur.commit()
	            return "error"

  
	#INSERT ROW
	def insert(self, table, fname, lname, pnum, nname):
		with self.db:
			cur = self.db.cursor()
			sql = 'INSERT INTO table(fn, ln, pn, nn) VALUES(%s, %s, %s, %s)'
			if (cur.execute(sql, (fname, lname, pnum, nname))):
				return "success"
			else:
				return "error"

	#UPDATE SINGLE ROW
	def update(self, table, fname, lname, pnum, nname, idd):
		with self.db:
			cur = self.db.cursor()
			sql = 'UPDATE table SET fn=%s, ln=%s, pn=%s, nn=%s WHERE id=%s'
			if (cur.execute(sql, (fname, lname, pnum, nname, idd))):
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
		








	
