import psycopg2

from werkzeug.security import generate_password_hash, check_password_hash

def register(data,psql):

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

        user_email_address = data['userEmail'].lower()
        if user_email_address is "":
            user_email_address = None

        user_password = data['password']
        if user_password is "":
            user_password = None

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


        con = psycopg2.connect(database=psql['database'], user=psql['user'],password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        query = "INSERT INTO cbi_user(user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}'); ".format(
            user_first_name, user_last_name, user_company, user_email_address, generate_password_hash(user_password.strip(), method='sha256'), user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number)

        cur.execute(query)

        con.commit()
        con.close()

        return {'userEmail': user_email_address}, 200

    except Exception as e:
        error= str(e)
        if "user_email_address" in error:
            msg='User Email Address Already Exists'
        elif "invoice_email_address" in error:
            msg = 'Invoice Email Address Already Exists'
        else:
            msg = error
        
        return {'error': msg},409
