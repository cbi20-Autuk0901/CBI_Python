import psycopg2

import random

import string

from werkzeug.security import generate_password_hash

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def reset(user_email_address,psql):

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
            res = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k=8))
            mail(user_email_address,res)
            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                   password=psql['password'], host=psql['host'], port=psql['port'])
            cur = con.cursor()
            cur.execute(f"UPDATE cbi_user SET user_password='{generate_password_hash(res.strip(), method='sha256')}' WHERE user_email_address='{user_email_address}' ; ")
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
    body =f"Please use the Below tempory password to login into the CBI Portal, We strictly advise you to change the password once Logged in. \n Passowrd: {res}"
    msg = MIMEText(body)
    msg['Subject'] = "Climate Bond Password Reset"
    msg['From'] = sender
    msg['To'] = recipient
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    server.login(sender, 'Vigameq@i2R')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
