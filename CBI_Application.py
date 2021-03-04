from flask import Flask, request, jsonify

import sys
import os

from cbi_modules import user_login, user_register

from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

psql = {
    "database": "cbidatabase",
    "user": "cbiuser",
    "password": "cbipass",
    "host": "104.236.233.114",
    "port": "5432"
}

@app.route("/cbi_user_register", methods=['POST'])
def cbi_user_register():

    data = request.json

    cbi_register_response = user_register.register(data,psql)

    return cbi_register_response



@app.route("/cbi_login", methods=['POST'])
def cbi_login():
    
    data = request.json

    cbi_login_response = user_login.login(data,psql)

    return cbi_login_response

    


if __name__ == '__main__':
    # app.debug = True
    app.config['DEBUG'] = True
    app.run()
