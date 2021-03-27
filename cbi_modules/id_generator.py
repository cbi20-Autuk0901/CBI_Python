import psycopg2

import random

from datetime import datetime

import string


def pre_certification_id(user_email_address, instrument_type, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute("SELECT MAX(id) FROM cbi_pre_issuance_certification;")
        try:
            pattern_id = str(int(cur.fetchone()[0])+1)
        except:
            pattern_id = "1"

        cur.execute(
            f"SELECT user_first_name from CBI_User  WHERE user_email_address='{user_email_address}'")
        patter_name = str((cur.fetchone()[0][0:3].upper()))

        now = datetime.now()
        pattern_month = str(now.month).zfill(2)
        pattern_year = str(now.year)[2:]

        pattern_random_four = ''.join(random.choices(string.digits, k=4))

        certification_id = patter_name+pattern_id + pattern_month+pattern_year+pattern_random_four

        certification_status = 'draft'

        query = "INSERT INTO cbi_pre_issuance_certification(certification_id,user_email_address,certification_status,instrument_type) VALUES('{0}', '{1}','{2}','{3}'); ".format(
            certification_id, user_email_address, certification_status, instrument_type)
        cur.execute(query)
        con.commit()

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)

        return {'error': error}, 409


def post_certification_id(user_email_address, instrument_type, certification_id, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        certification_status = 'draft'

        query = "INSERT INTO cbi_post_issuance_certification(certification_id,user_email_address,certification_status,instrument_type) VALUES('{0}', '{1}','{2}','{3}'); ".format(
            certification_id, user_email_address, certification_status, instrument_type)
        cur.execute(query)

        con.commit()
        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)

        return {'error': error}, 409
