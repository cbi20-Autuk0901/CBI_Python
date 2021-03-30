import psycopg2

from werkzeug.security import generate_password_hash, check_password_hash


def login(data,psql):

    user_email_address = data['userEmail'].lower()
    user_password = data['userPassword']

    con = psycopg2.connect(database=psql['database'], user=psql['user'],password=psql['password'], host=psql['host'], port=psql['port'])

    cur = con.cursor()

    cur.execute(f"SELECT user_first_name,user_last_name,user_password,user_category from CBI_User  WHERE user_email_address='{user_email_address}'")
    user = cur.fetchone()

    con.close()

    if user is None:
            return {"error": "Invalid Email Address"},401
    else:
        if check_password_hash(user[2], user_password):
            return {'firstName': user[0], 'lastName': user[1], 'userEmail': user_email_address, 'userRole': user[3]}, 200
        else:
            return {"error": " Invalid Password"},403
