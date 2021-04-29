import psycopg2

import random

import string

from werkzeug.security import generate_password_hash

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime


def reset(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT user_id, user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number, user_job_title from cbi_user WHERE user_email_address!='{user_email_address}'")
        data = cur.fetchone()

        con.commit()
        con.close()

        if data is not None:
            res = ''.join(random.choices(string.ascii_uppercase +
                                         string.ascii_lowercase+string.digits+string.punctuation, k=8))
            mail(user_email_address, res)
            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                   password=psql['password'], host=psql['host'], port=psql['port'])
            cur = con.cursor()
            cur.execute(
                f"UPDATE cbi_user SET user_password='{generate_password_hash(res.strip(), method='sha256')}' WHERE user_email_address='{user_email_address}' ; ")
            con.commit()
            con.close()
            return {'userEmail': user_email_address}, 200
        elif data is None:
            return {'error': "user doesnt exists"}, 404

    except Exception as e:
        error = str(e)

        return {'error': error}, 409


def mail(to, res):
    sender = 'cbigithub@vigameq.com'
    recipient = to
    body = f"Please use the Below tempory password to login into the CBI Portal, We strictly advise you to change the password once Logged in. \n Passowrd: {res}"
    msg = MIMEText(body)
    msg['Subject'] = "Climate Bond Initiative"
    msg['From'] = sender
    msg['To'] = recipient
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    server.login(sender, 'Vigameq@i2R')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()


def update(data, psql):

    try:
        user_first_name = data['firstName']
        if user_first_name is "":
            user_first_name = None

        user_last_name = data['lastName']
        if user_last_name is "":
            user_last_name = None

        user_company = data['companyName']
        if user_company is "":
            user_company = None

        user_email_address = data['userEmail']

        user_category = data['userRole']
        if user_category is "":
            user_category = None

        user_location = data['location']
        if user_location is "":
            user_location = None

        invoice_company_name = data['invoiceCompanyName']
        if invoice_company_name is "":
            invoice_company_name = None

        invoice_registration_number = data['businessRegistrationNo']
        if invoice_registration_number is "":
            invoice_registration_number = None

        invoice_billing_address = data['businessAddress']
        if invoice_billing_address is "":
            invoice_billing_address = None

        invoice_email_address = data['invoiceEmail']
        if invoice_email_address is "":
            invoice_email_address = None

        invoice_phone_number = data['phoneNumber']
        if invoice_phone_number is "":
            invoice_phone_number = None
        
        user_job_title = data['jobTitle']
        if user_job_title is "":
            user_job_title = None

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        query = f"UPDATE cbi_user set user_first_name='{user_first_name}', user_last_name='{user_last_name}', user_company='{user_company}', user_category='{user_category}', user_location='{user_location}', invoice_company_name='{invoice_company_name}', invoice_registration_number='{invoice_registration_number}', invoice_billing_address='{invoice_billing_address}', invoice_email_address='{invoice_email_address}', invoice_phone_number='{invoice_phone_number}', user_job_title='{user_job_title}' where user_email_address='{user_email_address}'; "

        cur.execute(query)

        con.commit()
        con.close()

        return {'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)
        return {'error': error}, 409


def remove(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])
        cur = con.cursor()
        cur.execute(f"DELETE from cbi_user WHERE user_email_address='{user_email_address}' ; ")
        con.commit()
        con.close()
        return {'userEmail': user_email_address}, 200


    except Exception as e:
        error = str(e)

        return {'error': error}, 409


def invite(user_email_address, psql):

    try:
        invite_token = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase+string.digits, k=8))
        invite_time = datetime.now()
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])
        cur = con.cursor()
        cur.execute(f"SELECT id, user_email_address, invite_token, invite_time from cbi_issuer_invitation WHERE user_email_address='{user_email_address}'")
        data = cur.fetchone()
        con.commit()

        if data is not None:
            return {"error": "Already Invited"}, 409
        else:
            cur.execute(f"INSERT INTO cbi_issuer_invitation(user_email_address, invite_token, invite_time) VALUES('{user_email_address}', '{invite_token}', '{invite_time}');")
            con.commit()
            mail2(user_email_address, invite_token)
            con.close()
            return {'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)

        return {'error': error}, 409

def verify_token(invite_token,psql):
    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])
        cur = con.cursor()
        cur.execute(f"SELECT id, user_email_address, invite_token, invite_time from cbi_issuer_invitation WHERE invite_token='{invite_token}'")
        data = cur.fetchone()
        con.commit()

        if data is not None:
            cur.execute(f"select user_email_address from cbi_issuer_invitation where extract(hour from current_timestamp - invite_time)<=12 and invite_token='{invite_token}'")
            try:
                verified_email = str((cur.fetchone()[0]))
                con.commit()
                cur.execute(f"DELETE from cbi_issuer_invitation WHERE user_email_address='{verified_email}' ; ")
                con.commit()
                return {"userEmail": verified_email}, 200
            except:
                return {'error': "Token Expired"}, 401
        else:
            return {'error': "Invalid Token"}, 401
        con.close()

    except Exception as e:
        error = str(e)

        return {'error': error}, 409


def mail2(to, res):
    sender = 'cbigithub@vigameq.com'
    recipient = to
    body = f"Please use the Below Link to register into CBI Portal, We strictly advise you to Login within 12 hours. \n Registration Link: http://143.110.213.22/registration/{res}"
    msg = MIMEText(body)
    msg['Subject'] = "Climate Bond Initiative"
    msg['From'] = sender
    msg['To'] = recipient
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    server.login(sender, 'Vigameq@i2R')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
