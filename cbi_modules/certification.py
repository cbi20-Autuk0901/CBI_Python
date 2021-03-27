import psycopg2

import random

from datetime import datetime

import string


def step_one(data, psql):

    # if 'certificationId' in data:
    if len(data['certificationId']) > 0:
        try:
            certification_id = data['certificationId']
            user_email_address = data['userEmail']

            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                   password=psql['password'], host=psql['host'], port=psql['port'])

            cur = con.cursor()

            da_name = data['uniqueName']
            if len(da_name) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_name='{da_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_issuance_country = data['issuanceCountry']
            if len(da_issuance_country) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_issuance_country='{da_issuance_country}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_cusip = data['cusip']
            if len(da_cusip) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_cusip='{da_cusip}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_local_currency_lc = data['localCurrency']
            if len(da_local_currency_lc) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_local_currency_lc='{da_local_currency_lc}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_isin = data['isin']
            if len(da_isin) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_isin='{da_isin}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_amount_issued_lc = data['amountIssued']
            if len(da_amount_issued_lc) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_amount_issued_lc='{da_amount_issued_lc}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_coupon = data['coupon']
            if len(da_coupon) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_coupon='{da_coupon}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_underwriter = data['underwriter']
            if len(da_underwriter) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_underwriter='{da_underwriter}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_issue_date = data['issueDate']
            if len(da_issue_date) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_issue_date='{da_issue_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_maturity_date = data['maturityDate']
            if len(da_maturity_date) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_maturity_date='{da_maturity_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            t_proceeds = data['useOfProceeds']
            if len(t_proceeds) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET t_proceeds='{t_proceeds}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            t_proceeds_revenue = data['useOfProceedsRevenue']
            if len(t_proceeds_revenue) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET t_proceeds_revenue='{t_proceeds_revenue}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            t_verifier_name = data['verifierName']
            if len(t_verifier_name) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET t_verifier_name='{t_verifier_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            d_renewable_energy = data['renewableEnergy']
            if len(d_renewable_energy) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET d_renewable_energy='{d_renewable_energy}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            d_renewable_energy_text = data['renewableEnergyText']
            if len(d_renewable_energy_text) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET d_renewable_energy_text='{d_renewable_energy_text}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            con.close()

            return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

        except Exception as e:
            error = str(e)
            msg = error

            return {'error': msg},422
    else:
        try:
            user_email_address = data['userEmail']
            certification_status = 'Draft'

            con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])


            cur = con.cursor()

            cur.execute("SELECT MAX(id) FROM cbi_pre_issuance_certification;")
            try:
                pattern_id = str(int(cur.fetchone()[0])+1)
            except:
                pattern_id = "1"

            cur.execute(f"SELECT user_first_name from CBI_User  WHERE user_email_address='{user_email_address}'")
            patter_name = str((cur.fetchone()[0][0:3].upper()))

            now = datetime.now()
            pattern_month = str(now.month).zfill(2)
            pattern_year = str(now.year)[2:]

            pattern_random_four = ''.join(random.choices(string.digits, k=4))

            certification_id = patter_name+pattern_id+pattern_month+pattern_year+pattern_random_four

            query = "INSERT INTO cbi_pre_issuance_certification(certification_id,user_email_address,certification_status) VALUES('{0}', '{1}', '{2}'); ".format(certification_id, user_email_address,certification_status)
            cur.execute(query)
            con.commit()

            instrument_type = data['instrumentType']
            if len(instrument_type) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET instrument_type='{instrument_type}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_name = data['uniqueName']
            if len(da_name) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_name='{da_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_issuance_country = data['issuanceCountry']
            if len(da_issuance_country) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_issuance_country='{da_issuance_country}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_cusip = data['cusip']
            if len(da_cusip) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_cusip='{da_cusip}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_local_currency_lc = data['localCurrency']
            if len(da_local_currency_lc) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_local_currency_lc='{da_local_currency_lc}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_isin = data['isin']
            if len(da_isin) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_isin='{da_isin}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_amount_issued_lc = data['amountIssued']
            if len(da_amount_issued_lc) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_amount_issued_lc='{da_amount_issued_lc}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_coupon = data['coupon']
            if len(da_coupon) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_coupon='{da_coupon}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_underwriter = data['underwriter']
            if len(da_underwriter) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_underwriter='{da_underwriter}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_issue_date = data['issueDate']
            if len(da_issue_date) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_issue_date='{da_issue_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            da_maturity_date = data['maturityDate']
            if len(da_maturity_date) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET da_maturity_date='{da_maturity_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            t_proceeds = data['useOfProceeds']
            if len(t_proceeds) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET t_proceeds='{t_proceeds}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            t_proceeds_revenue = data['useOfProceedsRevenue']
            if len(t_proceeds_revenue) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET t_proceeds_revenue='{t_proceeds_revenue}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            t_verifier_name = data['verifierName']
            if len(t_verifier_name) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET t_verifier_name='{t_verifier_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            d_renewable_energy = data['renewableEnergy']
            if len(d_renewable_energy) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET d_renewable_energy='{d_renewable_energy}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            d_renewable_energy_text = data['renewableEnergyText']
            if len(d_renewable_energy_text) > 0:
                cur.execute(
                    f"UPDATE cbi_pre_issuance_certification SET d_renewable_energy_text='{d_renewable_energy_text}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
                con.commit()
            else:
                pass

            con.close()

            return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

        except Exception as e:
            error = str(e)
            msg = error

            return {'error': msg},422


def step_two(data, psql):

    try:
        certification_id = data['certificationId']
        user_email_address = data['userEmail']
        
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        ci_address_head_office = data['headOfficeAddress'].replace("'","''").replace(",",".")
        if len(ci_address_head_office) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ci_address_head_office='{ci_address_head_office}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ci_vat_number = data['vatNumber']
        if len(ci_vat_number) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ci_vat_number='{ci_vat_number}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ci_business_reg_number = data['businessRegistration']
        if len(ci_business_reg_number) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ci_business_reg_number='{ci_business_reg_number}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_name = data['contactName']
        if len(cp_name) > 0:
            cur.execute(
                f"UPDATE cbi_pre_issuance_certification SET cp_name='{cp_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_position = data['position']
        if len(cp_position) > 0:
            cur.execute(
                f"UPDATE cbi_pre_issuance_certification SET cp_position='{cp_position}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_company = data['company']
        if len(cp_company) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET cp_company='{cp_company}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_contact_number = data['contactNumber']
        if len(cp_contact_number) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET cp_contact_number='{cp_contact_number}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        id_name = data['invoiceName']
        if len(id_name) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET id_name='{id_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        d_renewable_energy = data['renewableEnergy']
        if len(d_renewable_energy) > 0:
            cur.execute(
                f"UPDATE cbi_pre_issuance_certification SET d_renewable_energy='{d_renewable_energy}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        d_renewable_energy_text = data['renewableEnergyText']
        if len(d_renewable_energy_text) > 0:
            cur.execute(
                f"UPDATE cbi_pre_issuance_certification SET d_renewable_energy_text='{d_renewable_energy_text}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg},422


def step_three(data, psql):

    try:
        certification_id = data['certificationId']
        user_email_address = data['userEmail']
        
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        ca_application_date = data['applicationDate']
        if len(ca_application_date) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_application_date='{ca_application_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_legal_name_issuing_entity = data['issuingEntityLegalName']
        if len(ca_legal_name_issuing_entity) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_legal_name_issuing_entity='{ca_legal_name_issuing_entity}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_unique_name_debt_instruments = data['debtInstrumentsUniqueName']
        if len(ca_unique_name_debt_instruments) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_unique_name_debt_instruments='{ca_unique_name_debt_instruments}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_address = data['address'].replace("'", "''").replace(",", ".")
        if len(ca_address) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_address='{ca_address}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_email_address = data['email']
        if len(ca_email_address) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_email_address='{ca_email_address}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_contact_person = data['issuerContactPerson']
        if len(ca_contact_person) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_contact_person='{ca_contact_person}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_signature = data['signature']
        if len(ca_signature) > 0:
            cur.execute(f"UPDATE cbi_pre_issuance_certification SET ca_signature='{ca_signature}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg},422


def step_four(certification_id, user_email_address, file_1, file_2, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()


        single_issuer_agreement = file_1
        if len(single_issuer_agreement) > 0:
            cur.execute(
                f"UPDATE cbi_pre_issuance_certification SET single_issuer_agreement='{single_issuer_agreement}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        verifier_agreement = file_2
        if len(verifier_agreement) > 0:
            cur.execute(
                f"UPDATE cbi_pre_issuance_certification SET verifier_agreement='{verifier_agreement}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 404


def submit(data, psql):

    try:
        certification_id = data['certificationId']
        user_email_address = data['userEmail']
        
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()
        query = "UPDATE cbi_pre_issuance_certification SET certification_status='Completed' WHERE user_email_address='{0}' AND certification_id='{1}'; ".format(
            user_email_address, certification_id)

        cur.execute(query)

        con.commit()
        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def step_one_get(user_email_address, certification_id, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                            password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, t_proceeds, t_proceeds_revenue, t_verifier_name, d_renewable_energy, d_renewable_energy_text from cbi_pre_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "instrumentType": data[0],
                "uniqueName": data[1],
                "issuanceCountry": data[2],
                "cusip": data[3],
                "isin": data[4],
                "localCurrency": data[5],
                "amountIssued": data[6],
                "coupon": data[7],
                "underwriter": data[8],
                "issueDate": data[9],
                "maturityDate": data[10],
                "useOfProceeds": data[11],
                "useOfProceedsRevenue": data[12],
                "verifierName": data[13],
                "renewableEnergy": data[14],
                "renewableEnergyText": data[15]}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def step_two_get(user_email_address, certification_id, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT d_renewable_energy,d_renewable_energy_text, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name from cbi_pre_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "headOfficeAddress": data[2],
                "vatNumber": data[3],
                "businessRegistration": data[4],
                "contactName": data[5],
                "position": data[6],
                "company": data[7],
                "contactNumber": data[8],
                "invoiceName": data[9],
                "renewableEnergy": data[0],
                "renewableEnergyText": data[1]}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def step_three_get(user_email_address, certification_id, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature from cbi_pre_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "applicationDate": data[0],
                "issuingEntityLegalName": data[1],
                "debtInstrumentsUniqueName": data[2],
                "address": data[3],
                "email": data[5],
                "issuerContactPerson": data[5],
                "signature": data[6]}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def step_four_get(user_email_address, certification_id, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT single_issuer_agreement, verifier_agreement from cbi_pre_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "caAssuranceReport": data[0],
                "gbAssuranceReport": data[1]},200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
