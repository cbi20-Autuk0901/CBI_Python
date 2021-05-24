import psycopg2

from werkzeug.security import generate_password_hash, check_password_hash


def update_user(data, psql):

    try:
        user_first_name = data['firstName']
        if user_first_name is "":
            user_first_name = None

        user_last_name = data['lastName']
        if user_last_name is "":
            user_last_name = None

        user_email_address = data['userEmail']

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


        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        query = f"UPDATE cbi_user set user_first_name='{user_first_name}', user_last_name='{user_last_name}',  user_location='{user_location}', invoice_company_name='{invoice_company_name}', invoice_registration_number='{invoice_registration_number}', invoice_billing_address='{invoice_billing_address}', invoice_email_address='{invoice_email_address}', invoice_phone_number='{invoice_phone_number}' where user_email_address='{user_email_address}'; "

        cur.execute(query)

        con.commit()
        con.close()

        return 1

    except:
        return 0


def get_user(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"select user_first_name, user_last_name, user_email_address, user_location,invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number,user_company from cbi_user WHERE user_email_address='{user_email_address}';")
        data = cur.fetchone()

        con.commit()
        con.close()
        if len(data) != 0:

            user_first_name = data[0]
            if user_first_name is "":
                user_first_name = None

            user_last_name = data[1]
            if user_last_name is "":
                user_last_name = None

            user_email_address = data[2]

            user_location = data[3]
            if user_location is "":
                user_location = None

            invoice_company_name = data[4]
            if invoice_company_name is "":
                invoice_company_name = None

            invoice_registration_number = data[5]
            if invoice_registration_number is "":
                invoice_registration_number = None

            invoice_billing_address = data[6]
            if invoice_billing_address is "":
                invoice_billing_address = None

            invoice_email_address = data[7]
            if invoice_email_address is "":
                invoice_email_address = None

            invoice_phone_number = data[8]
            if invoice_phone_number is "":
                invoice_phone_number = None

            user_company = data[9]
            if user_company is "":
                user_company = None

            return {"firstName": user_first_name,
                         "lastName": user_last_name,
                         "userEmail": user_email_address,
                         "location": user_location,
                         "invoiceCompanyName": invoice_company_name,
                         "businessRegistrationNo": invoice_registration_number,
                         "businessAddress": invoice_billing_address,
                         "invoiceEmail": invoice_email_address,
                         "phoneNumber": invoice_phone_number,
                         "companyName": user_company}, 200

        else:
            return {'userData': []}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def change_password(data, psql):

    user_email_address = data['userEmail'].lower()
    old_password = data['oldPassword']
    new_password = data['newPassword']

    con = psycopg2.connect(database=psql['database'], user=psql['user'],
                           password=psql['password'], host=psql['host'], port=psql['port'])

    cur = con.cursor()

    cur.execute(
        f"SELECT user_first_name,user_last_name,user_password,user_category from CBI_User  WHERE user_email_address='{user_email_address}'")
    user = cur.fetchone()

    con.close()

    if user is None:
        return {"error": "Invalid Email Address"}, 401
    else:
        if check_password_hash(user[2], old_password):
            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                   password=psql['password'], host=psql['host'], port=psql['port'])

            cur = con.cursor()

            query = f"UPDATE cbi_user set user_password='{generate_password_hash(new_password.strip(), method='sha256')}' where user_email_address='{user_email_address}'; "

            cur.execute(query)
            con.commit()

            con.commit()
            con.close()

            
            return {'message': 'Password Updated Successfully'}, 200
        else:
            return {"error": " Invalid Old Password"}, 403
