import psycopg2

from datetime import datetime

def single_signed_doc(certification_id, user_email_address, file_1, psql):

    try:
        signed_agreement = file_1

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"SELECT * from cbi_single_signed_agreement WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        now = datetime.now()
        if len(signed_agreement) > 0:
            if data is not None:
                cur.execute(f"UPDATE cbi_single_signed_agreement SET signed_agreement='{signed_agreement}',application_date='{now}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
                return {'certificationId': certification_id, 'userEmail': user_email_address, "signedCertificationAgreement": file_1}, 200
            elif data is None:
                query = "INSERT INTO cbi_single_signed_agreement(certification_id,user_email_address,signed_agreement,application_date) VALUES('{0}', '{1}','{2}','{3}'); ".format(certification_id, user_email_address, file_1, now)
                cur.execute(query)
                con.commit()
            con.close()
            return {'certificationId': certification_id, 'userEmail': user_email_address, "signedCertificationAgreement": file_1}, 200
        else:
            return {'error': "Invalid File"}, 422

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 404


def programmatic_signed_doc(certification_id, user_email_address, file_1, psql):

    try:
        signed_agreement = file_1

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"SELECT invoice_company_name from cbi_user WHERE user_email_address='{user_email_address}'")
        company = cur.fetchone()[0]

        if company is not None:
            cur.execute(f"SELECT * from cbi_programmatic_signed_agreement WHERE invoice_company_name='{company}'")
            data = cur.fetchone()

            now = datetime.now()
            if len(signed_agreement) > 0:
                if data is not None:
                    cur.execute(f"UPDATE cbi_programmatic_signed_agreement SET signed_agreement='{signed_agreement}',application_date='{now}' WHERE invoice_company_name='{company}'; ")
                    con.commit()
                    return {'certificationId': certification_id, 'userEmail': user_email_address, "signedCertificationAgreement": file_1}, 200
                elif data is None:
                    query = "INSERT INTO cbi_programmatic_signed_agreement(invoice_company_name,user_email_address,signed_agreement,application_date) VALUES('{0}', '{1}','{2}','{3}'); ".format(company, user_email_address, file_1, now)
                    cur.execute(query)
                    con.commit()
                con.close()
                return {'certificationId': certification_id, 'userEmail': user_email_address, "signedCertificationAgreement": file_1}, 200
            else:
                return {'error': "Invalid File"}, 422
        else:
            return {'error': "Invalid Company"}, 422

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 404


def single_signed_doc_get(certification_id, user_email_address, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT * from cbi_single_signed_agreement WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()
        if data is not None:
            return {'certificationId': certification_id, 'userEmail': user_email_address, "signedCertificationAgreement": data[3],"applicationDate":data[4]}, 200
        elif data is None:

            return {'error': "No Data"}, 404

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 404


def programmatic_signed_doc_get(certification_id, user_email_address, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT invoice_company_name from cbi_user WHERE user_email_address='{user_email_address}'")
        company = cur.fetchone()[0]

        if company is not None:
            cur.execute(
                f"SELECT * from cbi_programmatic_signed_agreement WHERE invoice_company_name='{company}'")
            data = cur.fetchone()

            con.close()
            if data is not None:
                return {'certificationId': certification_id, 'userEmail': user_email_address, "signedCertificationAgreement": data[3], "applicationDate": data[4],'company':data[1]}, 200
            elif data is None:
                return {'error': "No Data"}, 404

        else:
            return {'error': "Invalid Company"}, 422

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 404
