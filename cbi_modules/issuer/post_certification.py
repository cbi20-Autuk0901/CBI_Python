import psycopg2

from datetime import datetime


def step_one(data, psql):

    try:
        certification_id = data['certificationId']
        user_email_address = data['userEmail']

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        da_name = data['uniqueName'].replace("'", "''")
        if len(da_name) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_name='{da_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_issuance_country = data['issuanceCountry'].replace("'", "''")
        if len(da_issuance_country) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_issuance_country='{da_issuance_country}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_cusip = data['cusip'].replace("'", "''")
        if len(da_cusip) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_cusip='{da_cusip}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_local_currency_lc = data['localCurrency']
        if len(da_local_currency_lc) > 0:
            da_local_currency_lc = "~".join(da_local_currency_lc).replace("'", "''")
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_local_currency_lc='{da_local_currency_lc}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_isin = data['isin'].replace("'", "''")
        if len(da_isin) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_isin='{da_isin}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_amount_issued_lc = data['amountIssued']
        if len(da_amount_issued_lc) > 0:
            da_amount_issued_lc = "~".join(
                da_amount_issued_lc).replace("'", "''")
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_amount_issued_lc='{da_amount_issued_lc}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_coupon = data['coupon'].replace("'", "''")
        if len(da_coupon) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_coupon='{da_coupon}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_underwriter = data['underwriter']
        if len(da_underwriter) > 0:
            da_underwriter = "~".join(da_underwriter).replace("'", "''")
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_underwriter='{da_underwriter}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_issue_date = data['issueDate']
        if len(da_issue_date) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_issue_date='{da_issue_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_maturity_date = data['maturityDate']
        if len(da_maturity_date) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_maturity_date='{da_maturity_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        da_instrument_type = data['daInstrumentType'].replace("'", "''")
        if len(da_instrument_type) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET da_instrument_type='{da_instrument_type}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ps_financing_asset = data['financingAssets'].replace("'", "''")
        if len(ps_financing_asset) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ps_financing_asset='{ps_financing_asset}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ps_proceeds_allocation = data['proceedsAllocation'].replace("'", "''")
        if len(ps_proceeds_allocation) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ps_proceeds_allocation='{ps_proceeds_allocation}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        pe_portfolio_approach = data['portfolioApproach'].replace("'", "''")
        if len(pe_portfolio_approach) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET pe_portfolio_approach='{pe_portfolio_approach}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        pe_assessment_procedure = data['decisionProcedure'].replace("'", "''")
        if len(pe_assessment_procedure) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET pe_assessment_procedure='{pe_assessment_procedure}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        pm_proceed_type = data['proceedsType'].replace("'", "''")
        if len(pm_proceed_type) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET pm_proceed_type='{pm_proceed_type}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        pm_proceed_detail = data['proceedsProcessDetail'].replace("'", "''")
        if len(pm_proceed_detail) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET pm_proceed_detail='{pm_proceed_detail}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        pm_proceed_timing = data['proceedsAllocationTiming'].replace("'", "''")
        if len(pm_proceed_timing) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET pm_proceed_timing='{pm_proceed_timing}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        pm_proceed_use = data['proceedsUse'].replace("'", "''")
        if len(pm_proceed_use) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET pm_proceed_use='{pm_proceed_use}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        d_renewable_energy = data['renewableEnergy']
        if len(d_renewable_energy) > 0:
            d_renewable_energy = "~".join(
                d_renewable_energy).replace("'", "''")
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET d_renewable_energy='{d_renewable_energy}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        d_renewable_energy_text = data['renewableEnergyText']
        if len(d_renewable_energy_text) > 0:
            d_renewable_energy_text = "~".join(d_renewable_energy_text).replace("'", "''")
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET d_renewable_energy_text='{d_renewable_energy_text}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address, "certificationType": "post"}, 200

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

        ar_report_interval = data['allocationReportFreq'].replace("'", "''")
        if len(ar_report_interval) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ar_report_interval='{ar_report_interval}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ar_report_format = data['allocationReportFormat'].replace("'", "''")
        if len(ar_report_format) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ar_report_format='{ar_report_format}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ar_report_access = data['allocationReportAccess'].replace("'", "''")
        if len(ar_report_access) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ar_report_access='{ar_report_access}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ar_report_link = data['allocationReportAddressLink'].replace("'", "''")
        if len(ar_report_link) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ar_report_link='{ar_report_link}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ar_report_breakdown = data['breakdownInclusion'].replace("'", "''")
        if len(ar_report_breakdown) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ar_report_breakdown='{ar_report_breakdown}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ir_report_interval = data['impactReportFreq'].replace("'", "''")
        if len(ir_report_interval) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ir_report_interval='{ir_report_interval}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ir_report_format = data['impactReportFormat'].replace("'", "''")
        if len(ir_report_format) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ir_report_format='{ir_report_format}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ir_report_access = data['impactReportAccess'].replace("'", "''")
        if len(ir_report_access) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ir_report_access='{ir_report_access}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ir_report_link = data['impactReportAddressLink'].replace("'", "''")
        if len(ir_report_link) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ir_report_link='{ir_report_link}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ir_report_indicators = data['quantitativeImpact'].replace("'", "''")
        if len(ir_report_indicators) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET ir_report_indicators='{ir_report_indicators}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass
        
        ci_address_head_office = data['headOfficeAddress'].replace("'", "''").replace(",", ".")
        if len(ci_address_head_office) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ci_address_head_office='{ci_address_head_office}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ci_vat_number = data['vatNumber'].replace("'", "''")
        if len(ci_vat_number) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ci_vat_number='{ci_vat_number}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ci_business_reg_number = data['businessRegistration'].replace("'", "''")
        if len(ci_business_reg_number) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ci_business_reg_number='{ci_business_reg_number}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_name = data['contactName'].replace("'", "''")
        if len(cp_name) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET cp_name='{cp_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_position = data['position'].replace("'", "''")
        if len(cp_position) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET cp_position='{cp_position}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_company = data['company'].replace("'", "''")
        if len(cp_company) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET cp_company='{cp_company}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        cp_contact_number = data['contactNumber'].replace("'", "''")
        if len(cp_contact_number) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET cp_contact_number='{cp_contact_number}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        id_name = data['invoiceName'].replace("'", "''")
        if len(id_name) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET id_name='{id_name}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address, "certificationType": "post"}, 200

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
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_application_date='{ca_application_date}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_legal_name_issuing_entity = data['issuingEntityLegalName'].replace("'", "''")
        if len(ca_legal_name_issuing_entity) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_legal_name_issuing_entity='{ca_legal_name_issuing_entity}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_unique_name_debt_instruments = data['debtInstrumentsUniqueName'].replace("'", "''")
        if len(ca_unique_name_debt_instruments) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_unique_name_debt_instruments='{ca_unique_name_debt_instruments}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_address = data['address'].replace("'", "''").replace(",", ".")
        if len(ca_address) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_address='{ca_address}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_email_address = data['email'].replace("'", "''")
        if len(ca_email_address) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_email_address='{ca_email_address}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_contact_person = data['issuerContactPerson'].replace("'", "''")
        if len(ca_contact_person) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_contact_person='{ca_contact_person}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        ca_signature = data['signature'].replace("'", "''")
        if len(ca_signature) > 0:
            cur.execute(f"UPDATE cbi_post_issuance_certification SET ca_signature='{ca_signature}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address, "certificationType": "post", "agreement": "agreement"+"_"+str(certification_id)+".pdf"}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg},422


def step_four(certification_id, user_email_address, file_1, file_2, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()


        single_issuer_agreement = file_1.replace("'", "''")
        if len(single_issuer_agreement) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET single_issuer_agreement='{single_issuer_agreement}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        verifier_agreement = file_2.replace("'", "''")
        if len(verifier_agreement) > 0:
            cur.execute(
                f"UPDATE cbi_post_issuance_certification SET verifier_agreement='{verifier_agreement}' WHERE user_email_address='{user_email_address}' AND certification_id='{certification_id}'; ")
            con.commit()
        else:
            pass

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address, "certificationType": "post"}, 200

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
        query = "UPDATE cbi_post_issuance_certification SET certification_status='submitted' WHERE user_email_address='{0}' AND certification_id='{1}'; ".format(
            user_email_address, certification_id)
        cur.execute(query)
        con.commit()

        now=datetime.now()
        query = "UPDATE cbi_post_issuance_certification SET ca_application_date='{2}' WHERE user_email_address='{0}' AND certification_id='{1}'; ".format(
            user_email_address, certification_id,now)
        cur.execute(query)
        con.commit()

        cur.execute(f"SELECT instrument_type, da_underwriter,cp_company from cbi_post_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        cert_data = cur.fetchone()

        cur.execute(f"SELECT user_company from CBI_User  WHERE user_email_address='{user_email_address}'")
        user_data = cur.fetchone()

        query = "INSERT INTO CBI_Certification_Queue(certification_id,certification_type,certification_status,application_date,user_company,certification_company,instrument_type,underwriter) VALUES('{0}', '{1}','{2}','{3}','{4}','{5}','{6}','{7}'); ".format(
            certification_id, 'post', 'submitted', now,user_data[0],cert_data[2],cert_data[0],cert_data[1].replace("'", "''"))
        cur.execute(query)
        con.commit()

        con.close()

        return {'certificationId': certification_id, 'userEmail': user_email_address, "certificationType": "post"}, 200

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
            f"SELECT instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, d_renewable_energy, d_renewable_energy_text,ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use,da_instrument_type from cbi_post_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        instrument_type = data[0]

        da_name = data[1]
        if da_name is None:
            da_name = ""

        da_issuance_country = data[2]
        if da_issuance_country is None:
            da_issuance_country = ""

        da_cusip = data[3]
        if da_cusip is None:
            da_cusip = ""

        da_isin = data[4]
        if da_isin is None:
            da_isin = ""

        da_local_currency_lc = data[5]
        if da_local_currency_lc is None:
            da_local_currency_lc = []
        else:
            da_local_currency_lc = da_local_currency_lc.split("~")

        da_amount_issued_lc = data[6]
        if da_amount_issued_lc is None:
            da_amount_issued_lc = []
        else:
            da_amount_issued_lc = da_amount_issued_lc.split("~")

        da_coupon = data[7]
        if da_coupon is None:
            da_coupon = ""

        da_underwriter = data[8]
        if da_underwriter is None:
            da_underwriter = []
        else:
            da_underwriter = da_underwriter.split("~")

        da_issue_date = data[9]
        if da_issue_date is None:
            da_issue_date = ""

        da_maturity_date = data[10]
        if da_maturity_date is None:
            da_maturity_date = ""

        d_renewable_energy = data[11]
        if d_renewable_energy is None:
            d_renewable_energy = []
        else:
            d_renewable_energy = d_renewable_energy.split("~")

        d_renewable_energy_text = data[12]
        if d_renewable_energy_text is None:
            d_renewable_energy_text = []
        else:
            d_renewable_energy_text = d_renewable_energy_text.split("~")

        ps_financing_asset = data[13]
        if ps_financing_asset is None:
            ps_financing_asset = ""

        ps_proceeds_allocation = data[14]
        if ps_proceeds_allocation is None:
            ps_proceeds_allocation = ""

        pe_portfolio_approach = data[15]
        if pe_portfolio_approach is None:
            pe_portfolio_approach = ""

        pe_assessment_procedure = data[16]
        if pe_assessment_procedure is None:
            pe_assessment_procedure = ""

        pm_proceed_type = data[17]
        if pm_proceed_type is None:
            pm_proceed_type = ""

        pm_proceed_detail = data[18]
        if pm_proceed_detail is None:
            pm_proceed_detail = ""

        pm_proceed_timing = data[19]
        if pm_proceed_timing is None:
            pm_proceed_timing = ""

        pm_proceed_use = data[20]
        if pm_proceed_use is None:
            pm_proceed_use = ""

        da_instrument_type = data[21]
        if da_instrument_type is None:
            da_instrument_type = ""

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "instrumentType": instrument_type,
                "certificationType": "pre",
                "uniqueName": da_name,
                "issuanceCountry": da_issuance_country,
                "cusip": da_cusip,
                "isin": da_isin,
                "localCurrency": da_local_currency_lc,
                "amountIssued": da_amount_issued_lc,
                "coupon": da_coupon,
                "underwriter": da_underwriter,
                "issueDate": da_issue_date,
                "maturityDate": da_maturity_date,
                "renewableEnergy": d_renewable_energy,
                "renewableEnergyText": d_renewable_energy_text,
                "financingAssets": ps_financing_asset,
                "proceedsAllocation": ps_proceeds_allocation,
                "portfolioApproach": pe_portfolio_approach,
                "decisionProcedure": pe_assessment_procedure,
                "proceedsType": pm_proceed_type,
                "proceedsProcessDetail": pm_proceed_detail,
                "proceedsAllocationTiming": pm_proceed_timing,
                "proceedsUse": pm_proceed_use,
                "daInstrumentType": da_instrument_type}, 200

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
            f"SELECT ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name from cbi_post_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        cur.execute(
            f"SELECT invoice_billing_address, invoice_registration_number from cbi_user  WHERE user_email_address='{user_email_address}'")
        data_user = cur.fetchone()

        con.close()

        invoice_billing_address = data_user[0]
        if invoice_billing_address is None:
            invoice_billing_address = ""

        invoice_registration_number = data_user[1]
        if invoice_registration_number is None:
            invoice_registration_number = ""         

        ar_report_interval = data[0]
        if ar_report_interval is None:
            ar_report_interval = ""

        ar_report_format = data[1]
        if ar_report_format is None:
            ar_report_format = ""

        ar_report_access = data[2]
        if ar_report_access is None:
            ar_report_access = ""

        ar_report_link = data[3]
        if ar_report_link is None:
            ar_report_link = ""

        ar_report_breakdown = data[4]
        if ar_report_breakdown is None:
            ar_report_breakdown = ""

        ir_report_interval = data[5]
        if ir_report_interval is None:
            ir_report_interval = ""

        ir_report_format = data[6]
        if ir_report_format is None:
            ir_report_format = ""

        ir_report_access = data[7]
        if ir_report_access is None:
            ir_report_access = ""

        ir_report_link = data[8]
        if ir_report_link is None:
            ir_report_link = ""

        ir_report_indicators = data[9]
        if ir_report_indicators is None:
            ir_report_indicators = ""

        ci_address_head_office = data[10]
        if ci_address_head_office is None:
            ci_address_head_office = invoice_billing_address

        ci_vat_number = data[11]
        if ci_vat_number is None:
            ci_vat_number = ""

        ci_business_reg_number = data[12]
        if ci_business_reg_number is None:
            ci_business_reg_number = invoice_registration_number

        cp_name = data[13]
        if cp_name is None:
            cp_name = ""

        cp_position = data[14]
        if cp_position is None:
            cp_position = ""

        cp_company = data[15]
        if cp_company is None:
            cp_company = ""

        cp_contact_number = data[16]
        if cp_contact_number is None:
            cp_contact_number = ""

        id_name = data[17]
        if id_name is None:
            id_name = ""

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "certificationType": "pre",
                "headOfficeAddress": ci_address_head_office,
                "allocationReportFreq": ar_report_interval,
                "allocationReportFormat": ar_report_format,
                "allocationReportAccess": ar_report_access,
                "allocationReportAddressLink": ar_report_link,
                "breakdownInclusion": ar_report_breakdown,
                "impactReportFreq": ir_report_interval,
                "impactReportFormat": ir_report_format,
                "impactReportAccess": ir_report_access,
                "impactReportAddressLink": ir_report_link,
                "quantitativeImpact": ir_report_indicators,
                "vatNumber": ci_vat_number,
                "businessRegistration": ci_business_reg_number,
                "contactName": cp_name,
                "position": cp_position,
                "company": cp_company,
                "contactNumber": cp_contact_number,
                "invoiceName": id_name}, 200

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
            f"SELECT ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature from cbi_post_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()
        con.commit()

        cur.execute(f" select reviewer from cbi_certification_queue where certification_id='{certification_id}' and certification_type='pre';")
        reviewer = str(cur.fetchone()[0])
        con.commit()

        con.close()

        ca_application_date = data[0]
        if ca_application_date is None:
            ca_application_date = ""

        ca_legal_name_issuing_entity = data[1]
        if ca_legal_name_issuing_entity is None:
            ca_legal_name_issuing_entity = ""

        ca_unique_name_debt_instruments = data[2]
        if ca_unique_name_debt_instruments is None:
            ca_unique_name_debt_instruments = ""

        ca_address = data[3]
        if ca_address is None:
            ca_address = ""

        ca_email_address = data[4]
        if ca_email_address is None:
            ca_email_address = ""

        ca_contact_person = data[5]
        if ca_contact_person is None:
            ca_contact_person = ""

        ca_signature = data[6]
        if ca_signature is None:
            ca_signature = ""

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "applicationDate": ca_application_date,
                "certificationType": "post",
                "issuingEntityLegalName": ca_legal_name_issuing_entity,
                "debtInstrumentsUniqueName": ca_unique_name_debt_instruments,
                "address": ca_address,
                "email": ca_email_address,
                "issuerContactPerson": ca_contact_person,
                "signature": ca_signature,
                "agreement": "agreement"+"_"+str(certification_id)+".pdf",
                "reviewer": reviewer}, 200

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
            f"SELECT single_issuer_agreement, verifier_agreement from cbi_post_issuance_certification  WHERE user_email_address='{user_email_address}' and certification_id='{certification_id}'")
        data = cur.fetchone()

        con.close()

        single_issuer_agreement = data[0]
        if single_issuer_agreement is None:
            single_issuer_agreement = ""

        verifier_agreement = data[1]
        if verifier_agreement is None:
            verifier_agreement = ""

        return {"certificationId": certification_id,
                "userEmail": user_email_address,
                "certificationType": "post",
                "caAssuranceReport": single_issuer_agreement.split("/")[-1],
                "gbAssuranceReport": verifier_agreement.split("/")[-1]}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
