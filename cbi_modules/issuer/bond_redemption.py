import psycopg2

from datetime import datetime

def redeem(certification_id, user_email_address, file_1, file_2,file3, file4, file5, psql):
    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT * from cbi_bond_redemption WHERE certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        if data is not None:
            return {'error': "Row already exists"}, 409
        elif data is None:
            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                    password=psql['password'], host=psql['host'], port=psql['port'])

            cur = con.cursor()

            certification_status = 'redeemed'

            now= datetime.now()

            query = "INSERT INTO cbi_bond_redemption(certification_id,user_email_address,certification_status,file1,file2,file3,file4,file5, application_date) VALUES('{0}', '{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}'); ".format(
                certification_id, user_email_address, certification_status,file_1,file_2,file3,file4,file5,now)
            cur.execute(query)

            con.commit()
            con.close()

            return {'certificationId': certification_id, 'userEmail': user_email_address}, 200
        

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
