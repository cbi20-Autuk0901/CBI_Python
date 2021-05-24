import psycopg2

from datetime import datetime

def redeem(certification_id, user_email_address, file_1, file_2,file3, file4, file5, psql):
    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT id, certification_id, user_email_address, certification_status, file1, file2, file3, file4, file5, application_date from cbi_bond_redemption WHERE certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        if data is not None:
            return {'error': "Row already exists"}, 409
        elif data is None:
            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                    password=psql['password'], host=psql['host'], port=psql['port'])

            cur = con.cursor()

            certification_status = 'approved'#'submitted'

            now= datetime.now()

            query = "INSERT INTO cbi_bond_redemption(certification_id,user_email_address,certification_status,file1,file2,file3,file4,file5, application_date) VALUES('{0}', '{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}'); ".format(
                certification_id, user_email_address, certification_status,file_1,file_2,file3,file4,file5,now)
            cur.execute(query)
            con.commit()

            cur.execute(f"SELECT instrument_type, da_underwriter,cp_company from cbi_pre_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
            cert_data = cur.fetchone()

            cur.execute(f"SELECT user_company from CBI_User  WHERE user_email_address='{user_email_address}'")
            user_data = cur.fetchone()

            query = "INSERT INTO CBI_Certification_Queue(certification_id,certification_type,certification_status,application_date,user_company,certification_company,instrument_type,underwriter) VALUES('{0}', '{1}','{2}','{3}','{4}','{5}','{6}','{7}'); ".format(
                certification_id, 'bond_redemption', 'approved', now, user_data[0], cert_data[2], cert_data[0], cert_data[1])
            cur.execute(query)
            con.commit()
            con.close()

            return {'certificationId': certification_id, 'userEmail': user_email_address}, 200
        

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
