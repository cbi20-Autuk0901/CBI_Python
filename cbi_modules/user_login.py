import psycopg2

import json

import os

from werkzeug.security import generate_password_hash, check_password_hash


def login(data,psql):

    user_email_address = data['user_email_address'].lower()
    user_password = data['user_password']

    con = psycopg2.connect(database=psql['database'], user=psql['user'],password=psql['password'], host=psql['host'], port=psql['port'])

    cur = con.cursor()

    cur.execute(f"SELECT user_first_name,user_last_name,user_password from CBI_User  WHERE user_email_address='{user_email_address}'")
    user = cur.fetchone()

    con.close()

    if user is None:
            return {"error": "Invalid Email Address"}
    else:
        if check_password_hash(user[2], user_password):
            return {'user_first_name': user[0], 'user_last_name': user[1]}
        else:
            return {"error": " Invalid Password"}
