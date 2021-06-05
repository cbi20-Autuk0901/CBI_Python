import psycopg2

from datetime import datetime


def unassigned_queue(user_email_address, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"select id, certification_id, certification_type, certification_status, reviewer, application_date, assigned_date, approved_date, user_company, certification_company, instrument_type, underwriter from cbi_certification_queue where certification_status='submitted' ;")
        cert_queue = cur.fetchall()
        con.commit()

        queue_main_data = []
        if cert_queue is not None:
            for i in cert_queue:
                if i[2] == 'pre':
                    cur.execute(f"select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, d_renewable_energy, d_renewable_energy_text, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement from cbi_pre_issuance_certification where certification_id='{i[1]}' ;")
                    cert_queue_data = cur.fetchone()
                    con.commit()
                    
                    cur.execute(f"SELECT user_company,user_first_name ,user_last_name from CBI_User  WHERE user_email_address='{cert_queue_data[2]}'")
                    verifier = cur.fetchone()
                    con.commit()
                    verifier_fname = verifier[1]
                    verifier_lname = verifier[2]
                    verifier_company = verifier[0]

                    da_name = cert_queue_data[5]
                    if da_name is None:
                        da_name = ""

                    da_issuance_country = cert_queue_data[6]
                    if da_issuance_country is None:
                        da_issuance_country = ""

                    da_cusip = cert_queue_data[7]
                    if da_cusip is None:
                        da_cusip = ""

                    da_isin = cert_queue_data[8]
                    if da_isin is None:
                        da_isin = ""

                    da_local_currency_lc = cert_queue_data[9]
                    if da_local_currency_lc is None:
                        da_local_currency_lc = []
                    else:
                        da_local_currency_lc = da_local_currency_lc.split("~")

                    da_amount_issued_lc = cert_queue_data[10]
                    if da_amount_issued_lc is None:
                        da_amount_issued_lc = []
                    else:
                        da_amount_issued_lc = da_amount_issued_lc.split("~")

                    da_coupon = cert_queue_data[11]
                    if da_coupon is None:
                        da_coupon = ""

                    da_underwriter = cert_queue_data[12]
                    if da_underwriter is None:
                        da_underwriter = []
                    else:
                        da_underwriter = da_underwriter.split("~")

                    da_issue_date = cert_queue_data[13]
                    if da_issue_date is None:
                        da_issue_date = ""

                    da_maturity_date = cert_queue_data[14]
                    if da_maturity_date is None:
                        da_maturity_date = ""

                    da_instrument_type = cert_queue_data[15]
                    if da_instrument_type is None:
                        da_instrument_type = ""

                    d_renewable_energy = cert_queue_data[16]
                    if d_renewable_energy is None:
                        d_renewable_energy = []
                    else:
                        d_renewable_energy = d_renewable_energy.split("~")

                    d_renewable_energy_text = cert_queue_data[17]
                    if d_renewable_energy_text is None:
                        d_renewable_energy_text = []
                    else:
                        d_renewable_energy_text = d_renewable_energy_text.split(
                            "~")

                    ps_financing_asset = cert_queue_data[18]
                    if ps_financing_asset is None:
                        ps_financing_asset = ""

                    ps_proceeds_allocation = cert_queue_data[19]
                    if ps_proceeds_allocation is None:
                        ps_proceeds_allocation = ""

                    pe_portfolio_approach = cert_queue_data[20]
                    if pe_portfolio_approach is None:
                        pe_portfolio_approach = ""

                    pe_assessment_procedure = cert_queue_data[21]
                    if pe_assessment_procedure is None:
                        pe_assessment_procedure = ""

                    pm_proceed_type = cert_queue_data[22]
                    if pm_proceed_type is None:
                        pm_proceed_type = ""

                    pm_proceed_detail = cert_queue_data[23]
                    if pm_proceed_detail is None:
                        pm_proceed_detail = ""

                    pm_proceed_timing = cert_queue_data[24]
                    if pm_proceed_timing is None:
                        pm_proceed_timing = ""

                    pm_proceed_use = cert_queue_data[25]
                    if pm_proceed_use is None:
                        pm_proceed_use = ""

                    ar_report_interval = cert_queue_data[26]
                    if ar_report_interval is None:
                        ar_report_interval = ""

                    ar_report_format = cert_queue_data[27]
                    if ar_report_format is None:
                        ar_report_format = ""

                    ar_report_access = cert_queue_data[28]
                    if ar_report_access is None:
                        ar_report_access = ""

                    ar_report_link = cert_queue_data[29]
                    if ar_report_link is None:
                        ar_report_link = ""

                    ar_report_breakdown = cert_queue_data[30]
                    if ar_report_breakdown is None:
                        ar_report_breakdown = ""

                    ir_report_interval = cert_queue_data[31]
                    if ir_report_interval is None:
                        ir_report_interval = ""

                    ir_report_format = cert_queue_data[32]
                    if ir_report_format is None:
                        ir_report_format = ""

                    ir_report_access = cert_queue_data[33]
                    if ir_report_access is None:
                        ir_report_access = ""

                    ir_report_link = cert_queue_data[34]
                    if ir_report_link is None:
                        ir_report_link = ""

                    ir_report_indicators = cert_queue_data[35]
                    if ir_report_indicators is None:
                        ir_report_indicators = ""

                    ci_address_head_office = cert_queue_data[36]
                    if ci_address_head_office is None:
                        ci_address_head_office = ""

                    ci_vat_number = cert_queue_data[37]
                    if ci_vat_number is None:
                        ci_vat_number = ""

                    ci_business_reg_number = cert_queue_data[38]
                    if ci_business_reg_number is None:
                        ci_business_reg_number = ""

                    cp_name = cert_queue_data[39]
                    if cp_name is None:
                        cp_name = ""

                    cp_position = cert_queue_data[40]
                    if cp_position is None:
                        cp_position = ""

                    cp_company = cert_queue_data[41]
                    if cp_company is None:
                        cp_company = ""

                    cp_contact_number = cert_queue_data[42]
                    if cp_contact_number is None:
                        cp_contact_number = ""

                    id_name = cert_queue_data[43]
                    if id_name is None:
                        id_name = ""

                    ca_application_date = cert_queue_data[44]
                    if ca_application_date is None:
                        ca_application_date = ""

                    ca_legal_name_issuing_entity = cert_queue_data[45]
                    if ca_legal_name_issuing_entity is None:
                        ca_legal_name_issuing_entity = ""

                    ca_unique_name_debt_instruments = cert_queue_data[46]
                    if ca_unique_name_debt_instruments is None:
                        ca_unique_name_debt_instruments = ""

                    ca_address = cert_queue_data[47]
                    if ca_address is None:
                        ca_address = ""

                    ca_email_address = cert_queue_data[48]
                    if ca_email_address is None:
                        ca_email_address = ""

                    ca_contact_person = cert_queue_data[49]
                    if ca_contact_person is None:
                        ca_contact_person = ""

                    ca_signature = cert_queue_data[50]
                    if ca_signature is None:
                        ca_signature = ""

                    single_issuer_agreement = cert_queue_data[51]
                    if single_issuer_agreement is None:
                        single_issuer_agreement = ""

                    verifier_agreement = cert_queue_data[52]
                    if verifier_agreement is None:
                        verifier_agreement = ""

                    resp_data = {"certificationId": cert_queue_data[1],
                                 "userEmail": cert_queue_data[2],
                                 "certificationStatus": cert_queue_data[3],
                                 "instrumentType": cert_queue_data[4],
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
                                 "daInstrumentType": da_instrument_type,
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
                                 "invoiceName": id_name,
                                 "applicationDate": ca_application_date,
                                 "issuingEntityLegalName": ca_legal_name_issuing_entity,
                                 "debtInstrumentsUniqueName": ca_unique_name_debt_instruments,
                                 "address": ca_address,
                                 "email": ca_email_address,
                                 "issuerContactPerson": ca_contact_person,
                                 "signature": ca_signature,
                                 "caAssuranceReport": single_issuer_agreement.split("/")[-1],
                                 "gbAssuranceReport": verifier_agreement.split("/")[-1],
                                 "verifierCompany": verifier_company,
                                 "verifierFirstName": verifier_fname,
                                 "verifierLastName": verifier_lname}

                    queue_main_data.append(resp_data)
                elif i[2] == 'post':
                    cur.execute(f"select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, d_renewable_energy, d_renewable_energy_text, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement from cbi_post_issuance_certification where certification_id='{i[1]}' ;")
                    cert_queue_data = cur.fetchone()
                    con.commit()

                    cur.execute(f"SELECT user_company,user_first_name ,user_last_name from CBI_User  WHERE user_email_address='{cert_queue_data[2]}'")
                    verifier = cur.fetchone()
                    con.commit()
                    verifier_fname = verifier[1]
                    verifier_lname = verifier[2]
                    verifier_company = verifier[0]

                    da_name = cert_queue_data[5]
                    if da_name is None:
                        da_name = ""

                    da_issuance_country = cert_queue_data[6]
                    if da_issuance_country is None:
                        da_issuance_country = ""

                    da_cusip = cert_queue_data[7]
                    if da_cusip is None:
                        da_cusip = ""

                    da_isin = cert_queue_data[8]
                    if da_isin is None:
                        da_isin = ""

                    da_local_currency_lc = cert_queue_data[9]
                    if da_local_currency_lc is None:
                        da_local_currency_lc = []
                    else:
                        da_local_currency_lc = da_local_currency_lc.split("~")

                    da_amount_issued_lc = cert_queue_data[10]
                    if da_amount_issued_lc is None:
                        da_amount_issued_lc = []
                    else:
                        da_amount_issued_lc = da_amount_issued_lc.split("~")

                    da_coupon = cert_queue_data[11]
                    if da_coupon is None:
                        da_coupon = ""

                    da_underwriter = cert_queue_data[12]
                    if da_underwriter is None:
                        da_underwriter = []
                    else:
                        da_underwriter = da_underwriter.split("~")

                    da_issue_date = cert_queue_data[13]
                    if da_issue_date is None:
                        da_issue_date = ""

                    da_maturity_date = cert_queue_data[14]
                    if da_maturity_date is None:
                        da_maturity_date = ""

                    da_instrument_type = cert_queue_data[15]
                    if da_instrument_type is None:
                        da_instrument_type = ""

                    d_renewable_energy = cert_queue_data[16]
                    if d_renewable_energy is None:
                        d_renewable_energy = []
                    else:
                        d_renewable_energy = d_renewable_energy.split("~")

                    d_renewable_energy_text = cert_queue_data[17]
                    if d_renewable_energy_text is None:
                        d_renewable_energy_text = []
                    else:
                        d_renewable_energy_text = d_renewable_energy_text.split(
                            "~")

                    ps_financing_asset = cert_queue_data[18]
                    if ps_financing_asset is None:
                        ps_financing_asset = ""

                    ps_proceeds_allocation = cert_queue_data[19]
                    if ps_proceeds_allocation is None:
                        ps_proceeds_allocation = ""

                    pe_portfolio_approach = cert_queue_data[20]
                    if pe_portfolio_approach is None:
                        pe_portfolio_approach = ""

                    pe_assessment_procedure = cert_queue_data[21]
                    if pe_assessment_procedure is None:
                        pe_assessment_procedure = ""

                    pm_proceed_type = cert_queue_data[22]
                    if pm_proceed_type is None:
                        pm_proceed_type = ""

                    pm_proceed_detail = cert_queue_data[23]
                    if pm_proceed_detail is None:
                        pm_proceed_detail = ""

                    pm_proceed_timing = cert_queue_data[24]
                    if pm_proceed_timing is None:
                        pm_proceed_timing = ""

                    pm_proceed_use = cert_queue_data[25]
                    if pm_proceed_use is None:
                        pm_proceed_use = ""

                    ar_report_interval = cert_queue_data[26]
                    if ar_report_interval is None:
                        ar_report_interval = ""

                    ar_report_format = cert_queue_data[27]
                    if ar_report_format is None:
                        ar_report_format = ""

                    ar_report_access = cert_queue_data[28]
                    if ar_report_access is None:
                        ar_report_access = ""

                    ar_report_link = cert_queue_data[29]
                    if ar_report_link is None:
                        ar_report_link = ""

                    ar_report_breakdown = cert_queue_data[30]
                    if ar_report_breakdown is None:
                        ar_report_breakdown = ""

                    ir_report_interval = cert_queue_data[31]
                    if ir_report_interval is None:
                        ir_report_interval = ""

                    ir_report_format = cert_queue_data[32]
                    if ir_report_format is None:
                        ir_report_format = ""

                    ir_report_access = cert_queue_data[33]
                    if ir_report_access is None:
                        ir_report_access = ""

                    ir_report_link = cert_queue_data[34]
                    if ir_report_link is None:
                        ir_report_link = ""

                    ir_report_indicators = cert_queue_data[35]
                    if ir_report_indicators is None:
                        ir_report_indicators = ""

                    ci_address_head_office = cert_queue_data[36]
                    if ci_address_head_office is None:
                        ci_address_head_office = ""

                    ci_vat_number = cert_queue_data[37]
                    if ci_vat_number is None:
                        ci_vat_number = ""

                    ci_business_reg_number = cert_queue_data[38]
                    if ci_business_reg_number is None:
                        ci_business_reg_number = ""

                    cp_name = cert_queue_data[39]
                    if cp_name is None:
                        cp_name = ""

                    cp_position = cert_queue_data[40]
                    if cp_position is None:
                        cp_position = ""

                    cp_company = cert_queue_data[41]
                    if cp_company is None:
                        cp_company = ""

                    cp_contact_number = cert_queue_data[42]
                    if cp_contact_number is None:
                        cp_contact_number = ""

                    id_name = cert_queue_data[43]
                    if id_name is None:
                        id_name = ""

                    ca_application_date = cert_queue_data[44]
                    if ca_application_date is None:
                        ca_application_date = ""

                    ca_legal_name_issuing_entity = cert_queue_data[45]
                    if ca_legal_name_issuing_entity is None:
                        ca_legal_name_issuing_entity = ""

                    ca_unique_name_debt_instruments = cert_queue_data[46]
                    if ca_unique_name_debt_instruments is None:
                        ca_unique_name_debt_instruments = ""

                    ca_address = cert_queue_data[47]
                    if ca_address is None:
                        ca_address = ""

                    ca_email_address = cert_queue_data[48]
                    if ca_email_address is None:
                        ca_email_address = ""

                    ca_contact_person = cert_queue_data[49]
                    if ca_contact_person is None:
                        ca_contact_person = ""

                    ca_signature = cert_queue_data[50]
                    if ca_signature is None:
                        ca_signature = ""

                    single_issuer_agreement = cert_queue_data[51]
                    if single_issuer_agreement is None:
                        single_issuer_agreement = ""

                    verifier_agreement = cert_queue_data[52]
                    if verifier_agreement is None:
                        verifier_agreement = ""

                    resp_data = {"certificationId": cert_queue_data[1],
                                 "userEmail": cert_queue_data[2],
                                 "certificationStatus": cert_queue_data[3],
                                 "instrumentType": cert_queue_data[4],
                                 "certificationType": "post",
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
                                 "daInstrumentType": da_instrument_type,
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
                                 "invoiceName": id_name,
                                 "applicationDate": ca_application_date,
                                 "issuingEntityLegalName": ca_legal_name_issuing_entity,
                                 "debtInstrumentsUniqueName": ca_unique_name_debt_instruments,
                                 "address": ca_address,
                                 "email": ca_email_address,
                                 "issuerContactPerson": ca_contact_person,
                                 "signature": ca_signature,
                                 "caAssuranceReport": single_issuer_agreement.split("/")[-1],
                                 "gbAssuranceReport": verifier_agreement.split("/")[-1],
                                 "verifierCompany": verifier_company,
                                 "verifierFirstName": verifier_fname,
                                 "verifierLastName": verifier_lname}

                    queue_main_data.append(resp_data)
                elif i[2] == 'bond_redemption':
                    cur.execute(f"select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, d_renewable_energy, d_renewable_energy_text, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement from cbi_post_issuance_certification where certification_id='{i[1]}' ;")
                    cert_queue_data = cur.fetchone()
                    con.commit()

                    cur.execute(f"SELECT user_company,user_first_name ,user_last_name from CBI_User  WHERE user_email_address='{cert_queue_data[2]}'")
                    verifier = cur.fetchone()
                    con.commit()
                    verifier_fname = verifier[1]
                    verifier_lname = verifier[2]
                    verifier_company = verifier[0]

                    cur.execute(f"select id, certification_id, user_email_address, certification_status, file1, file2, file3, file4, file5, application_date from cbi_bond_redemption where certification_id='{i[1]}' ;")
                    cert_queue_data_redemption = cur.fetchone()
                    con.commit()

                    da_name = cert_queue_data[5]
                    if da_name is None:
                        da_name = ""

                    da_issuance_country = cert_queue_data[6]
                    if da_issuance_country is None:
                        da_issuance_country = ""

                    da_cusip = cert_queue_data[7]
                    if da_cusip is None:
                        da_cusip = ""

                    da_isin = cert_queue_data[8]
                    if da_isin is None:
                        da_isin = ""

                    da_local_currency_lc = cert_queue_data[9]
                    if da_local_currency_lc is None:
                        da_local_currency_lc = []
                    else:
                        da_local_currency_lc = da_local_currency_lc.split("~")

                    da_amount_issued_lc = cert_queue_data[10]
                    if da_amount_issued_lc is None:
                        da_amount_issued_lc = []
                    else:
                        da_amount_issued_lc = da_amount_issued_lc.split("~")

                    da_coupon = cert_queue_data[11]
                    if da_coupon is None:
                        da_coupon = ""

                    da_underwriter = cert_queue_data[12]
                    if da_underwriter is None:
                        da_underwriter = []
                    else:
                        da_underwriter = da_underwriter.split("~")

                    da_issue_date = cert_queue_data[13]
                    if da_issue_date is None:
                        da_issue_date = ""

                    da_maturity_date = cert_queue_data[14]
                    if da_maturity_date is None:
                        da_maturity_date = ""

                    da_instrument_type = cert_queue_data[15]
                    if da_instrument_type is None:
                        da_instrument_type = ""

                    d_renewable_energy = cert_queue_data[16]
                    if d_renewable_energy is None:
                        d_renewable_energy = []
                    else:
                        d_renewable_energy = d_renewable_energy.split("~")

                    d_renewable_energy_text = cert_queue_data[17]
                    if d_renewable_energy_text is None:
                        d_renewable_energy_text = []
                    else:
                        d_renewable_energy_text = d_renewable_energy_text.split(
                            "~")

                    ps_financing_asset = cert_queue_data[18]
                    if ps_financing_asset is None:
                        ps_financing_asset = ""

                    ps_proceeds_allocation = cert_queue_data[19]
                    if ps_proceeds_allocation is None:
                        ps_proceeds_allocation = ""

                    pe_portfolio_approach = cert_queue_data[20]
                    if pe_portfolio_approach is None:
                        pe_portfolio_approach = ""

                    pe_assessment_procedure = cert_queue_data[21]
                    if pe_assessment_procedure is None:
                        pe_assessment_procedure = ""

                    pm_proceed_type = cert_queue_data[22]
                    if pm_proceed_type is None:
                        pm_proceed_type = ""

                    pm_proceed_detail = cert_queue_data[23]
                    if pm_proceed_detail is None:
                        pm_proceed_detail = ""

                    pm_proceed_timing = cert_queue_data[24]
                    if pm_proceed_timing is None:
                        pm_proceed_timing = ""

                    pm_proceed_use = cert_queue_data[25]
                    if pm_proceed_use is None:
                        pm_proceed_use = ""

                    ar_report_interval = cert_queue_data[26]
                    if ar_report_interval is None:
                        ar_report_interval = ""

                    ar_report_format = cert_queue_data[27]
                    if ar_report_format is None:
                        ar_report_format = ""

                    ar_report_access = cert_queue_data[28]
                    if ar_report_access is None:
                        ar_report_access = ""

                    ar_report_link = cert_queue_data[29]
                    if ar_report_link is None:
                        ar_report_link = ""

                    ar_report_breakdown = cert_queue_data[30]
                    if ar_report_breakdown is None:
                        ar_report_breakdown = ""

                    ir_report_interval = cert_queue_data[31]
                    if ir_report_interval is None:
                        ir_report_interval = ""

                    ir_report_format = cert_queue_data[32]
                    if ir_report_format is None:
                        ir_report_format = ""

                    ir_report_access = cert_queue_data[33]
                    if ir_report_access is None:
                        ir_report_access = ""

                    ir_report_link = cert_queue_data[34]
                    if ir_report_link is None:
                        ir_report_link = ""

                    ir_report_indicators = cert_queue_data[35]
                    if ir_report_indicators is None:
                        ir_report_indicators = ""

                    ci_address_head_office = cert_queue_data[36]
                    if ci_address_head_office is None:
                        ci_address_head_office = ""

                    ci_vat_number = cert_queue_data[37]
                    if ci_vat_number is None:
                        ci_vat_number = ""

                    ci_business_reg_number = cert_queue_data[38]
                    if ci_business_reg_number is None:
                        ci_business_reg_number = ""

                    cp_name = cert_queue_data[39]
                    if cp_name is None:
                        cp_name = ""

                    cp_position = cert_queue_data[40]
                    if cp_position is None:
                        cp_position = ""

                    cp_company = cert_queue_data[41]
                    if cp_company is None:
                        cp_company = ""

                    cp_contact_number = cert_queue_data[42]
                    if cp_contact_number is None:
                        cp_contact_number = ""

                    id_name = cert_queue_data[43]
                    if id_name is None:
                        id_name = ""

                    ca_application_date = cert_queue_data[44]
                    if ca_application_date is None:
                        ca_application_date = ""

                    ca_legal_name_issuing_entity = cert_queue_data[45]
                    if ca_legal_name_issuing_entity is None:
                        ca_legal_name_issuing_entity = ""

                    ca_unique_name_debt_instruments = cert_queue_data[46]
                    if ca_unique_name_debt_instruments is None:
                        ca_unique_name_debt_instruments = ""

                    ca_address = cert_queue_data[47]
                    if ca_address is None:
                        ca_address = ""

                    ca_email_address = cert_queue_data[48]
                    if ca_email_address is None:
                        ca_email_address = ""

                    ca_contact_person = cert_queue_data[49]
                    if ca_contact_person is None:
                        ca_contact_person = ""

                    ca_signature = cert_queue_data[50]
                    if ca_signature is None:
                        ca_signature = ""

                    single_issuer_agreement = cert_queue_data[51]
                    if single_issuer_agreement is None:
                        single_issuer_agreement = ""

                    verifier_agreement = cert_queue_data[52]
                    if verifier_agreement is None:
                        verifier_agreement = ""

                    resp_data = {"certificationId": cert_queue_data[1],
                                 "userEmail": cert_queue_data[2],
                                 "certificationStatus": cert_queue_data_redemption[3],
                                 "instrumentType": cert_queue_data[4],
                                 "certificationType": "bondRedemption",
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
                                 "daInstrumentType": da_instrument_type,
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
                                 "invoiceName": id_name,
                                 "applicationDate": ca_application_date,
                                 "issuingEntityLegalName": ca_legal_name_issuing_entity,
                                 "debtInstrumentsUniqueName": ca_unique_name_debt_instruments,
                                 "address": ca_address,
                                 "email": ca_email_address,
                                 "issuerContactPerson": ca_contact_person,
                                 "signature": ca_signature,
                                 "caAssuranceReport": single_issuer_agreement.split("/")[-1],
                                 "gbAssuranceReport": verifier_agreement.split("/")[-1],
                                 "file1": cert_queue_data_redemption[4].split("/")[-1],
                                 "file2": cert_queue_data_redemption[5].split("/")[-1],
                                 "file3": cert_queue_data_redemption[6].split("/")[-1],
                                 "file4": cert_queue_data_redemption[7].split("/")[-1],
                                 "file5": cert_queue_data_redemption[8].split("/")[-1],
                                 "verifierCompany": verifier_company,
                                 "verifierFirstName": verifier_fname,
                                 "verifierLastName": verifier_lname}

                    queue_main_data.append(resp_data)

        con.close()
        return {'data': queue_main_data}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def validate_reviewer(user_email_address, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"SELECT user_id, user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number, user_job_title from CBI_User  WHERE user_email_address='{user_email_address}' and user_category='reviewer'")
        reviewer = cur.fetchone()
        con.commit()
        con.close()

        if reviewer is None:
            return 0
        else:
            return 1


    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def assign_reviewer(user_email_address,certification_type,certification_id, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        now= datetime.now()

        try:

            if certification_type == 'bondRedemption':
                certification_type = 'bond_redemption'

            query = f"UPDATE cbi_certification_queue SET reviewer='{user_email_address}',assigned_date='{now}',certification_status='in-review' WHERE certification_type='{certification_type}'  AND certification_id='{certification_id}'; "
            cur.execute(query)
            con.commit()

            if certification_type == "pre":
                query = f"UPDATE cbi_pre_issuance_certification SET certification_status='in-review' WHERE certification_id='{certification_id}'; "
                cur.execute(query)
                con.commit()
            elif certification_type == "post":
                query = f"UPDATE cbi_post_issuance_certification SET certification_status='in-review' WHERE certification_id='{certification_id}'; "
                cur.execute(query)
                con.commit()
            elif certification_type == "bond_redemption":
                query = f"UPDATE cbi_bond_redemption SET certification_status='in-review' WHERE certification_id='{certification_id}'; "
                cur.execute(query)
                con.commit()

            con.close()

            return 1
        except:
            return 0

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
