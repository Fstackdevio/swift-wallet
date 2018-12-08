from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from v1.api import *

api.add_resource(Authenticate, '/Authenticate')
api.add_resource(Auth2, '/Authv2')
api.add_resource(logout, '/logout')
api.add_resource(spendingHistory, '/spendingHistory')
api.add_resource(transferHistory, '/transferHistory')
api.add_resource(depositHistory, '/depositHistory')
api.add_resource(loginHistory, '/loginHistory')
api.add_resource(dashboardInfo, '/dashboardInfo')
api.add_resource(makeDeposit1, '/makeDeposit1')
# api.add_resource(updateData, '/updateData')

if __name__ == '__main__':
    app.run(debug=True)
