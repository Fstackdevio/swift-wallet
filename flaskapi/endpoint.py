from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from v1.api import *


api.add_resource(Authenticate, '/Authenticate')
api.add_resource(logout, '/logout')
api.add_resource(depositHistory, '/depositHistory')
api.add_resource(GetAllTrans, '/GetAllTrans')
api.add_resource(Test, '/test')
api.add_resource(ReturnResponse, '/testResponse')
api.add_resource(newData, '/insertData')
# api.add_resource(updateData, '/updateData')

if __name__ == '__main__':
    app.run(debug=True)

# This is to inform all parents/guardians that their ward in the department of mass communication would be participating  in a departmental workshop program which commences on Wednesday 5th November 2018 with the sum of #70,000 all payments should be made at the account office on or before Wednesday 5th November 2018, we apologize for the short notice and inconvenience this may have caused, God continue to bless and uphold you.