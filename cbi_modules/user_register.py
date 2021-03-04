import psycopg2

import json

import os

from werkzeug.security import generate_password_hash, check_password_hash

def register(data,psql):

    try:
        user_first_name = data['user_first_name']
        user_last_name = data['user_last_name']
        user_company = data['user_company']
        user_email_address = data['user_email_address'].lower()
        user_password = data['user_password']
        user_category = data['user_category']
        user_location = data['user_location']
        invoice_company_name = data['invoice_company_name']
        invoice_registration_number = data['invoice_registration_number']
        invoice_billing_address = data['invoice_billing_address']
        invoice_email_address = data['invoice_email_address']
        invoice_phone_number = data['invoice_phone_number']

        con = psycopg2.connect(database=psql['database'], user=psql['user'],password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        query = "INSERT INTO cbi_user(user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}'); ".format(
            user_first_name, user_last_name, user_company, user_email_address, generate_password_hash(user_password.strip(), method='sha256'), user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number)

        cur.execute(query)

        con.commit()
        con.close()

        return {'status': 200}

    except Exception as e:
        error= str(e)
        if "user_email_address" in error:
            msg='User Email Address Already Exists'
        elif "invoice_email_address" in error:
            msg = 'Invoice Email Address Already Exists'
        else:
            msg = error
        
        return {'error': msg}
