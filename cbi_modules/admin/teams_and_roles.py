import psycopg2


def stats(user_email_address,psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        # Reviewer Count
        try:
            cur.execute(f"select count(*) from cbi_user where user_category='reviewer'")
            reviewer_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            reviewer_count = "0"

        # Issuer Count
        try:
            cur.execute(f"select count(*) from cbi_user where user_category='programmaticIssuer' or user_category='singleIssuer'")
            issuer_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            issuer_count = "0"

        # Admin Count
        try:
            cur.execute(f"select count(*) from cbi_user where user_category='admin'")
            admin_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            admin_count = "0"

        # reviewers
        try:
            cur.execute(f"select user_id, user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number, user_job_title from cbi_user where user_category='reviewer'")
            admin_data = cur.fetchall()
            con.commit()
            reviewers_details = []
            for i in admin_data:
                data = {"firstName": i[1], "lastName": i[2], "companyName": i[3], "userEmail": i[4], "userRole": i[6], "location": i[7], "invoiceCompanyName": i[8], "businessRegistrationNo": i[9], "businessAddress": i[10], "invoiceEmail": i[11], "phoneNumber": i[12],"jobTitle":i[13] }
                reviewers_details.append(data)
        except:
            reviewers_details = []
        
        # admins
        try:
            cur.execute(
                f"select user_id, user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number, user_job_title from cbi_user where user_category='admin' and user_email_address != '{user_email_address}'")
            admin_data = cur.fetchall()
            con.commit()
            admins_details = []
            for i in admin_data:
                data = {"firstName": i[1], "lastName": i[2], "companyName": i[3], "userEmail": i[4], "userRole": i[6], "location": i[7],"invoiceCompanyName": i[8], "businessRegistrationNo": i[9], "businessAddress": i[10], "invoiceEmail": i[11], "phoneNumber": i[12],"jobTitle":i[13] }
                admins_details.append(data)
        except:
            admins_details = []

        # issuers
        try:
            cur.execute(f"select user_id, user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number, user_job_title from cbi_user where user_category='programmaticIssuer' or user_category='singleIssuer' or user_category='verifier' ")
            admin_data = cur.fetchall()
            con.commit()
            issuers_details = []
            for i in admin_data:
                data = {"firstName": i[1], "lastName": i[2], "companyName": i[3], "userEmail": i[4], "userRole": i[6], "location": i[7],"invoiceCompanyName": i[8], "businessRegistrationNo": i[9], "businessAddress": i[10], "invoiceEmail": i[11], "phoneNumber": i[12], "jobTitle": i[13]}
                issuers_details.append(data)
        except:
            issuers_details = []



        con.close()

        return {'userStats': {'reviewerCount': reviewer_count, 'issuerCount': issuer_count, 'adminCount': admin_count},"reviewers":reviewers_details, "admins":admins_details,"issuers":issuers_details}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
