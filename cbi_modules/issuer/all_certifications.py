import psycopg2


def get_certifications(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"(select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, d_renewable_energy, d_renewable_energy_text, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement,'post' as certification_type from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}') UNION (select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, d_renewable_energy, d_renewable_energy_text, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement,'pre' as certification_type from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}');")
        data = cur.fetchall()

        cur.execute(f"(select a.id, a.certification_id, a.user_email_address, a.certification_status, a.file1, a.file2, a.file3, a.file4, a.file5, a.application_date,b.da_name,b.instrument_type from cbi_bond_redemption a left join cbi_pre_issuance_certification b on a.certification_id=b.certification_id where a.user_email_address='{user_email_address}');")
        data1 = cur.fetchall()

        con.commit()
        con.close()
        if len(data)!=0:

            all_certifications = []

            for i in data:
                da_name = i[5]
                if da_name is None:
                    da_name = ""

                da_issuance_country = i[6]
                if da_issuance_country is None:
                    da_issuance_country = ""

                da_cusip = i[7]
                if da_cusip is None:
                    da_cusip = ""

                da_isin = i[8]
                if da_isin is None:
                    da_isin = ""

                da_local_currency_lc = i[9]
                if da_local_currency_lc is None:
                    da_local_currency_lc = []
                else:
                    da_local_currency_lc = da_local_currency_lc.split("~")

                da_amount_issued_lc = i[10]
                if da_amount_issued_lc is None:
                    da_amount_issued_lc = []
                else:
                    da_amount_issued_lc = da_amount_issued_lc.split("~")

                da_coupon = i[11]
                if da_coupon is None:
                    da_coupon = ""

                da_underwriter = i[12]
                if da_underwriter is None:
                    da_underwriter = []
                else:
                    da_underwriter = da_underwriter.split("~")

                da_issue_date = i[13]
                if da_issue_date is None:
                    da_issue_date = ""

                da_maturity_date = i[14]
                if da_maturity_date is None:
                    da_maturity_date = ""
                    
                da_instrument_type = i[15]
                if da_instrument_type is None:
                    da_instrument_type = ""

                d_renewable_energy = i[16]
                if d_renewable_energy is None:
                    d_renewable_energy = []
                else:
                    d_renewable_energy = d_renewable_energy.split("~")

                d_renewable_energy_text = i[17]
                if d_renewable_energy_text is None:
                    d_renewable_energy_text = []
                else:
                    d_renewable_energy_text = d_renewable_energy_text.split("~")

                ps_financing_asset = i[18]
                if ps_financing_asset is None:
                    ps_financing_asset = ""

                ps_proceeds_allocation = i[19]
                if ps_proceeds_allocation is None:
                    ps_proceeds_allocation = ""

                pe_portfolio_approach = i[20]
                if pe_portfolio_approach is None:
                    pe_portfolio_approach = ""

                pe_assessment_procedure = i[21]
                if pe_assessment_procedure is None:
                    pe_assessment_procedure = ""

                pm_proceed_type = i[22]
                if pm_proceed_type is None:
                    pm_proceed_type = ""

                pm_proceed_detail = i[23]
                if pm_proceed_detail is None:
                    pm_proceed_detail = ""

                pm_proceed_timing = i[24]
                if pm_proceed_timing is None:
                    pm_proceed_timing = ""

                pm_proceed_use = i[25]
                if pm_proceed_use is None:
                    pm_proceed_use = ""

                ar_report_interval = i[26]
                if ar_report_interval is None:
                    ar_report_interval = ""

                ar_report_format = i[27]
                if ar_report_format is None:
                    ar_report_format = ""

                ar_report_access = i[28]
                if ar_report_access is None:
                    ar_report_access = ""

                ar_report_link = i[29]
                if ar_report_link is None:
                    ar_report_link = ""

                ar_report_breakdown = i[30]
                if ar_report_breakdown is None:
                    ar_report_breakdown = ""

                ir_report_interval = i[31]
                if ir_report_interval is None:
                    ir_report_interval = ""

                ir_report_format = i[32]
                if ir_report_format is None:
                    ir_report_format = ""

                ir_report_access = i[33]
                if ir_report_access is None:
                    ir_report_access = ""

                ir_report_link = i[34]
                if ir_report_link is None:
                    ir_report_link = ""

                ir_report_indicators = i[35]
                if ir_report_indicators is None:
                    ir_report_indicators = ""

                ci_address_head_office = i[36]
                if ci_address_head_office is None:
                    ci_address_head_office = ""

                ci_vat_number = i[37]
                if ci_vat_number is None:
                    ci_vat_number = ""

                ci_business_reg_number = i[38]
                if ci_business_reg_number is None:
                    ci_business_reg_number = ""

                cp_name = i[39]
                if cp_name is None:
                    cp_name = ""

                cp_position = i[40]
                if cp_position is None:
                    cp_position = ""

                cp_company = i[41]
                if cp_company is None:
                    cp_company = ""

                cp_contact_number = i[42]
                if cp_contact_number is None:
                    cp_contact_number = ""

                id_name = i[43]
                if id_name is None:
                    id_name = ""

                ca_application_date = i[44]
                if ca_application_date is None:
                    ca_application_date = ""

                ca_legal_name_issuing_entity = i[45]
                if ca_legal_name_issuing_entity is None:
                    ca_legal_name_issuing_entity = ""

                ca_unique_name_debt_instruments = i[46]
                if ca_unique_name_debt_instruments is None:
                    ca_unique_name_debt_instruments = ""

                ca_address = i[47]
                if ca_address is None:
                    ca_address = ""

                ca_email_address = i[48]
                if ca_email_address is None:
                    ca_email_address = ""

                ca_contact_person = i[49]
                if ca_contact_person is None:
                    ca_contact_person = ""

                ca_signature = i[50]
                if ca_signature is None:
                    ca_signature = ""

                single_issuer_agreement = i[51]
                if single_issuer_agreement is None:
                    single_issuer_agreement = ""

                verifier_agreement = i[52]
                if verifier_agreement is None:
                    verifier_agreement = ""

                certification_status = i[3]
                if certification_status != "approved":
                    certificate = ""
                    approval = ""
                else:
                    certificate = f"certificate_"+str(i[1])+"_"+str(i[53])+".pdf"
                    approval = "approval_"+str(i[1])+"_"+str(i[53])+".pdf"


                resp_data = {"certificationId": i[1],
                        "userEmail": i[2],
                        "certificationStatus": i[3],
                        "instrumentType": i[4],
                        "certificationType": i[53],
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
                        "certificate": certificate,
                        "approval":approval}
                all_certifications.append(resp_data)
            if len(data1) != 0:
                for j in data1:
                    certification_status = j[3]
                    if certification_status != "approved":
                        certificate = ""
                        approval = ""
                    else:
                        certificate = f"certificate_"+str(j[1])+"_bond_redemption.pdf"
                        approval = "approval_"+str(j[1])+"_bond_redemption.pdf.pdf"
                    resp_data1 = {"certificationId": j[1],
                                    "userEmail": j[2],
                                    "certificationStatus": j[3],
                                    "instrumentType": j[11],
                                    "certificationType": "bondRedemption",
                                    "uniqueName": j[10],
                                    "file1": j[4].split("/")[-1],
                                    "file2": j[5].split("/")[-1],
                                    "file3": j[6].split("/")[-1],
                                    "file4": j[7].split("/")[-1],
                                    "file5": j[8].split("/")[-1],
                                    "applicationDate": i[9],
                                    "certificate": certificate,
                                    "approval": approval}
                    all_certifications.append(resp_data1)
                            
            return {'recentCertifications': all_certifications}, 200
        
        else:
            return {'recentCertifications': []}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def pre_certifications(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"SELECT pre.id, pre.certification_id, pre.user_email_address, pre.certification_status, pre.instrument_type, pre.da_name, pre.da_issuance_country, pre.da_cusip, pre.da_isin, pre.da_local_currency_lc, pre.da_amount_issued_lc, pre.da_coupon, pre.da_underwriter, pre.da_issue_date, pre.da_maturity_date, pre.da_instrument_type, pre.d_renewable_energy, pre.d_renewable_energy_text, pre.ps_financing_asset, pre.ps_proceeds_allocation, pre.pe_portfolio_approach, pre.pe_assessment_procedure, pre.pm_proceed_type, pre.pm_proceed_detail, pre.pm_proceed_timing, pre.pm_proceed_use, pre.ar_report_interval, pre.ar_report_format, pre.ar_report_access, pre.ar_report_link, pre.ar_report_breakdown, pre.ir_report_interval, pre.ir_report_format, pre.ir_report_access, pre.ir_report_link, pre.ir_report_indicators, pre.ci_address_head_office, pre.ci_vat_number, pre.ci_business_reg_number, pre.cp_name, pre.cp_position, pre.cp_company, pre.cp_contact_number, pre.id_name, pre.ca_application_date, pre.ca_legal_name_issuing_entity, pre.ca_unique_name_debt_instruments, pre.ca_address, pre.ca_email_address, pre.ca_contact_person, pre.ca_signature, pre.single_issuer_agreement, pre.verifier_agreement FROM cbi_pre_issuance_certification pre WHERE Not EXISTS(SELECT post.id, post.certification_id, post.user_email_address, post.certification_status, post.instrument_type, post.da_name, post.da_issuance_country, post.da_cusip, post.da_isin, post.da_local_currency_lc, post.da_amount_issued_lc, post.da_coupon, post.da_underwriter, post.da_issue_date, post.da_maturity_date, post.da_instrument_type, post.ps_financing_asset, post.ps_proceeds_allocation, post.pe_portfolio_approach, post.pe_assessment_procedure, post.pm_proceed_type, post.pm_proceed_detail, post.pm_proceed_timing, post.pm_proceed_use, post.ar_report_interval, post.ar_report_format, post.ar_report_access, post.ar_report_link, post.ar_report_breakdown, post.ir_report_interval, post.ir_report_format, post.ir_report_access, post.ir_report_link, post.ir_report_indicators, post.d_renewable_energy, post.d_renewable_energy_text, post.ci_address_head_office, post.ci_vat_number, post.ci_business_reg_number, post.cp_name, post.cp_position, post.cp_company, post.cp_contact_number, post.id_name, post.ca_application_date, post.ca_legal_name_issuing_entity, post.ca_unique_name_debt_instruments, post.ca_address, post.ca_email_address, post.ca_contact_person, post.ca_signature, post.single_issuer_agreement, post.verifier_agreement FROM cbi_post_issuance_certification post WHERE pre.certification_id=post.certification_id and post.certification_status!='draft' and post.user_email_address='{user_email_address}') and pre.certification_status='approved' and pre.user_email_address='{user_email_address}';")
        data = cur.fetchall()

        con.commit()
        con.close()
        if len(data) != 0:

            pre_certifications = []

            for i in data:

                da_name = i[5]
                if da_name is None:
                    da_name = ""

                da_issuance_country = i[6]
                if da_issuance_country is None:
                    da_issuance_country = ""

                da_cusip = i[7]
                if da_cusip is None:
                    da_cusip = ""

                da_isin = i[8]
                if da_isin is None:
                    da_isin = ""

                da_local_currency_lc = i[9]
                if da_local_currency_lc is None:
                    da_local_currency_lc = []
                else:
                    da_local_currency_lc = da_local_currency_lc.split("~")

                da_amount_issued_lc = i[10]
                if da_amount_issued_lc is None:
                    da_amount_issued_lc = []
                else:
                    da_amount_issued_lc = da_amount_issued_lc.split("~")

                da_coupon = i[11]
                if da_coupon is None:
                    da_coupon = ""

                da_underwriter = i[12]
                if da_underwriter is None:
                    da_underwriter = []
                else:
                    da_underwriter = da_underwriter.split("~")

                da_issue_date = i[13]
                if da_issue_date is None:
                    da_issue_date = ""

                da_maturity_date = i[14]
                if da_maturity_date is None:
                    da_maturity_date = ""

                da_instrument_type = i[15]
                if da_instrument_type is None:
                    da_instrument_type = ""

                d_renewable_energy = i[16]
                if d_renewable_energy is None:
                    d_renewable_energy = []
                else:
                    d_renewable_energy = d_renewable_energy.split("~")

                d_renewable_energy_text = i[17]
                if d_renewable_energy_text is None:
                    d_renewable_energy_text = []
                else:
                    d_renewable_energy_text = d_renewable_energy_text.split(
                        "~")

                ps_financing_asset = i[18]
                if ps_financing_asset is None:
                    ps_financing_asset = ""

                ps_proceeds_allocation = i[19]
                if ps_proceeds_allocation is None:
                    ps_proceeds_allocation = ""

                pe_portfolio_approach = i[20]
                if pe_portfolio_approach is None:
                    pe_portfolio_approach = ""

                pe_assessment_procedure = i[21]
                if pe_assessment_procedure is None:
                    pe_assessment_procedure = ""

                pm_proceed_type = i[22]
                if pm_proceed_type is None:
                    pm_proceed_type = ""

                pm_proceed_detail = i[23]
                if pm_proceed_detail is None:
                    pm_proceed_detail = ""

                pm_proceed_timing = i[24]
                if pm_proceed_timing is None:
                    pm_proceed_timing = ""

                pm_proceed_use = i[25]
                if pm_proceed_use is None:
                    pm_proceed_use = ""

                ar_report_interval = i[26]
                if ar_report_interval is None:
                    ar_report_interval = ""

                ar_report_format = i[27]
                if ar_report_format is None:
                    ar_report_format = ""

                ar_report_access = i[28]
                if ar_report_access is None:
                    ar_report_access = ""

                ar_report_link = i[29]
                if ar_report_link is None:
                    ar_report_link = ""

                ar_report_breakdown = i[30]
                if ar_report_breakdown is None:
                    ar_report_breakdown = ""

                ir_report_interval = i[31]
                if ir_report_interval is None:
                    ir_report_interval = ""

                ir_report_format = i[32]
                if ir_report_format is None:
                    ir_report_format = ""

                ir_report_access = i[33]
                if ir_report_access is None:
                    ir_report_access = ""

                ir_report_link = i[34]
                if ir_report_link is None:
                    ir_report_link = ""

                ir_report_indicators = i[35]
                if ir_report_indicators is None:
                    ir_report_indicators = ""

                ci_address_head_office = i[36]
                if ci_address_head_office is None:
                    ci_address_head_office = ""

                ci_vat_number = i[37]
                if ci_vat_number is None:
                    ci_vat_number = ""

                ci_business_reg_number = i[38]
                if ci_business_reg_number is None:
                    ci_business_reg_number = ""

                cp_name = i[39]
                if cp_name is None:
                    cp_name = ""

                cp_position = i[40]
                if cp_position is None:
                    cp_position = ""

                cp_company = i[41]
                if cp_company is None:
                    cp_company = ""

                cp_contact_number = i[42]
                if cp_contact_number is None:
                    cp_contact_number = ""

                id_name = i[43]
                if id_name is None:
                    id_name = ""

                ca_application_date = i[44]
                if ca_application_date is None:
                    ca_application_date = ""

                ca_legal_name_issuing_entity = i[45]
                if ca_legal_name_issuing_entity is None:
                    ca_legal_name_issuing_entity = ""

                ca_unique_name_debt_instruments = i[46]
                if ca_unique_name_debt_instruments is None:
                    ca_unique_name_debt_instruments = ""

                ca_address = i[47]
                if ca_address is None:
                    ca_address = ""

                ca_email_address = i[48]
                if ca_email_address is None:
                    ca_email_address = ""

                ca_contact_person = i[49]
                if ca_contact_person is None:
                    ca_contact_person = ""

                ca_signature = i[50]
                if ca_signature is None:
                    ca_signature = ""

                single_issuer_agreement = i[51]
                if single_issuer_agreement is None:
                    single_issuer_agreement = ""

                verifier_agreement = i[52]
                if verifier_agreement is None:
                    verifier_agreement = ""

                resp_data = {"certificationId": i[1],
                             "userEmail": i[2],
                             "certificationStatus": i[3],
                             "instrumentType": i[4],
                             "certificationType": 'pre',
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
                             "gbAssuranceReport": verifier_agreement.split("/")[-1]}
                pre_certifications.append(resp_data)

            return {'recentCertifications': pre_certifications}, 200
        else:
            return {'recentCertifications': []}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def post_certifications(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"SELECT post.id, post.certification_id, post.user_email_address, post.certification_status, post.instrument_type, post.da_name, post.da_issuance_country, post.da_cusip, post.da_isin, post.da_local_currency_lc, post.da_amount_issued_lc, post.da_coupon, post.da_underwriter, post.da_issue_date, post.da_maturity_date, post.da_instrument_type, post.ps_financing_asset, post.ps_proceeds_allocation, post.pe_portfolio_approach, post.pe_assessment_procedure, post.pm_proceed_type, post.pm_proceed_detail, post.pm_proceed_timing, post.pm_proceed_use, post.ar_report_interval, post.ar_report_format, post.ar_report_access, post.ar_report_link, post.ar_report_breakdown, post.ir_report_interval, post.ir_report_format, post.ir_report_access, post.ir_report_link, post.ir_report_indicators, post.d_renewable_energy, post.d_renewable_energy_text, post.ci_address_head_office, post.ci_vat_number, post.ci_business_reg_number, post.cp_name, post.cp_position, post.cp_company, post.cp_contact_number, post.id_name, post.ca_application_date, post.ca_legal_name_issuing_entity, post.ca_unique_name_debt_instruments, post.ca_address, post.ca_email_address, post.ca_contact_person, post.ca_signature, post.single_issuer_agreement, post.verifier_agreement FROM cbi_post_issuance_certification post WHERE Not EXISTS (SELECT redeem.id, redeem.certification_id, redeem.user_email_address, redeem.certification_status, redeem.file1, redeem.file2, redeem.file3, redeem.file4, redeem.file5, redeem.application_date FROM cbi_bond_redemption redeem WHERE redeem.certification_id = post.certification_id and redeem.user_email_address='{user_email_address}') and post.certification_status='approved' and post.user_email_address='{user_email_address}';")
        data = cur.fetchall()

        con.commit()
        con.close()
        if len(data) != 0:

            post_certifications = []

            for i in data:
                da_name = i[5]
                if da_name is None:
                    da_name = ""

                da_issuance_country = i[6]
                if da_issuance_country is None:
                    da_issuance_country = ""

                da_cusip = i[7]
                if da_cusip is None:
                    da_cusip = ""

                da_isin = i[8]
                if da_isin is None:
                    da_isin = ""

                da_local_currency_lc = i[9]
                if da_local_currency_lc is None:
                    da_local_currency_lc = []
                else:
                    da_local_currency_lc = da_local_currency_lc.split("~")

                da_amount_issued_lc = i[10]
                if da_amount_issued_lc is None:
                    da_amount_issued_lc = []
                else:
                    da_amount_issued_lc = da_amount_issued_lc.split("~")

                da_coupon = i[11]
                if da_coupon is None:
                    da_coupon = ""

                da_underwriter = i[12]
                if da_underwriter is None:
                    da_underwriter = []
                else:
                    da_underwriter = da_underwriter.split("~")

                da_issue_date = i[13]
                if da_issue_date is None:
                    da_issue_date = ""

                da_maturity_date = i[14]
                if da_maturity_date is None:
                    da_maturity_date = ""

                da_instrument_type = i[15]
                if da_instrument_type is None:
                    da_instrument_type = ""

                d_renewable_energy = i[16]
                if d_renewable_energy is None:
                    d_renewable_energy = []
                else:
                    d_renewable_energy = d_renewable_energy.split("~")

                d_renewable_energy_text = i[17]
                if d_renewable_energy_text is None:
                    d_renewable_energy_text = []
                else:
                    d_renewable_energy_text = d_renewable_energy_text.split(
                        "~")

                ps_financing_asset = i[18]
                if ps_financing_asset is None:
                    ps_financing_asset = ""

                ps_proceeds_allocation = i[19]
                if ps_proceeds_allocation is None:
                    ps_proceeds_allocation = ""

                pe_portfolio_approach = i[20]
                if pe_portfolio_approach is None:
                    pe_portfolio_approach = ""

                pe_assessment_procedure = i[21]
                if pe_assessment_procedure is None:
                    pe_assessment_procedure = ""

                pm_proceed_type = i[22]
                if pm_proceed_type is None:
                    pm_proceed_type = ""

                pm_proceed_detail = i[23]
                if pm_proceed_detail is None:
                    pm_proceed_detail = ""

                pm_proceed_timing = i[24]
                if pm_proceed_timing is None:
                    pm_proceed_timing = ""

                pm_proceed_use = i[25]
                if pm_proceed_use is None:
                    pm_proceed_use = ""

                ar_report_interval = i[26]
                if ar_report_interval is None:
                    ar_report_interval = ""

                ar_report_format = i[27]
                if ar_report_format is None:
                    ar_report_format = ""

                ar_report_access = i[28]
                if ar_report_access is None:
                    ar_report_access = ""

                ar_report_link = i[29]
                if ar_report_link is None:
                    ar_report_link = ""

                ar_report_breakdown = i[30]
                if ar_report_breakdown is None:
                    ar_report_breakdown = ""

                ir_report_interval = i[31]
                if ir_report_interval is None:
                    ir_report_interval = ""

                ir_report_format = i[32]
                if ir_report_format is None:
                    ir_report_format = ""

                ir_report_access = i[33]
                if ir_report_access is None:
                    ir_report_access = ""

                ir_report_link = i[34]
                if ir_report_link is None:
                    ir_report_link = ""

                ir_report_indicators = i[35]
                if ir_report_indicators is None:
                    ir_report_indicators = ""

                ci_address_head_office = i[36]
                if ci_address_head_office is None:
                    ci_address_head_office = ""

                ci_vat_number = i[37]
                if ci_vat_number is None:
                    ci_vat_number = ""

                ci_business_reg_number = i[38]
                if ci_business_reg_number is None:
                    ci_business_reg_number = ""

                cp_name = i[39]
                if cp_name is None:
                    cp_name = ""

                cp_position = i[40]
                if cp_position is None:
                    cp_position = ""

                cp_company = i[41]
                if cp_company is None:
                    cp_company = ""

                cp_contact_number = i[42]
                if cp_contact_number is None:
                    cp_contact_number = ""

                id_name = i[43]
                if id_name is None:
                    id_name = ""

                ca_application_date = i[44]
                if ca_application_date is None:
                    ca_application_date = ""

                ca_legal_name_issuing_entity = i[45]
                if ca_legal_name_issuing_entity is None:
                    ca_legal_name_issuing_entity = ""

                ca_unique_name_debt_instruments = i[46]
                if ca_unique_name_debt_instruments is None:
                    ca_unique_name_debt_instruments = ""

                ca_address = i[47]
                if ca_address is None:
                    ca_address = ""

                ca_email_address = i[48]
                if ca_email_address is None:
                    ca_email_address = ""

                ca_contact_person = i[49]
                if ca_contact_person is None:
                    ca_contact_person = ""

                ca_signature = i[50]
                if ca_signature is None:
                    ca_signature = ""

                single_issuer_agreement = i[51]
                if single_issuer_agreement is None:
                    single_issuer_agreement = ""

                verifier_agreement = i[52]
                if verifier_agreement is None:
                    verifier_agreement = ""

                resp_data = {"certificationId": i[1],
                             "userEmail": i[2],
                             "certificationStatus": i[3],
                             "instrumentType": i[4],
                             "certificationType": 'post',
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
                             "gbAssuranceReport": verifier_agreement.split("/")[-1]}
                post_certifications.append(resp_data)

            return {'recentCertifications': post_certifications}, 200
        else:
            return {'recentCertifications': []}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422


def approved_post_certifications(user_email_address, psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT post.id, post.certification_id, post.user_email_address, post.certification_status, post.instrument_type, post.da_name, post.da_issuance_country, post.da_cusip, post.da_isin, post.da_local_currency_lc, post.da_amount_issued_lc, post.da_coupon, post.da_underwriter, post.da_issue_date, post.da_maturity_date, post.da_instrument_type, post.ps_financing_asset, post.ps_proceeds_allocation, post.pe_portfolio_approach, post.pe_assessment_procedure, post.pm_proceed_type, post.pm_proceed_detail, post.pm_proceed_timing, post.pm_proceed_use, post.ar_report_interval, post.ar_report_format, post.ar_report_access, post.ar_report_link, post.ar_report_breakdown, post.ir_report_interval, post.ir_report_format, post.ir_report_access, post.ir_report_link, post.ir_report_indicators, post.d_renewable_energy, post.d_renewable_energy_text, post.ci_address_head_office, post.ci_vat_number, post.ci_business_reg_number, post.cp_name, post.cp_position, post.cp_company, post.cp_contact_number, post.id_name, post.ca_application_date, post.ca_legal_name_issuing_entity, post.ca_unique_name_debt_instruments, post.ca_address, post.ca_email_address, post.ca_contact_person, post.ca_signature, post.single_issuer_agreement, post.verifier_agreement FROM cbi_post_issuance_certification post WHERE post.certification_status='approved' and post.user_email_address='{user_email_address}';")
        data = cur.fetchall()

        con.commit()
        con.close()
        if len(data) != 0:

            post_certifications = []

            for i in data:
                da_name = i[5]
                if da_name is None:
                    da_name = ""

                da_issuance_country = i[6]
                if da_issuance_country is None:
                    da_issuance_country = ""

                da_cusip = i[7]
                if da_cusip is None:
                    da_cusip = ""

                da_isin = i[8]
                if da_isin is None:
                    da_isin = ""

                da_local_currency_lc = i[9]
                if da_local_currency_lc is None:
                    da_local_currency_lc = []
                else:
                    da_local_currency_lc = da_local_currency_lc.split("~")

                da_amount_issued_lc = i[10]
                if da_amount_issued_lc is None:
                    da_amount_issued_lc = []
                else:
                    da_amount_issued_lc = da_amount_issued_lc.split("~")

                da_coupon = i[11]
                if da_coupon is None:
                    da_coupon = ""

                da_underwriter = i[12]
                if da_underwriter is None:
                    da_underwriter = []
                else:
                    da_underwriter = da_underwriter.split("~")

                da_issue_date = i[13]
                if da_issue_date is None:
                    da_issue_date = ""

                da_maturity_date = i[14]
                if da_maturity_date is None:
                    da_maturity_date = ""

                da_instrument_type = i[15]
                if da_instrument_type is None:
                    da_instrument_type = ""

                d_renewable_energy = i[16]
                if d_renewable_energy is None:
                    d_renewable_energy = []
                else:
                    d_renewable_energy = d_renewable_energy.split("~")

                d_renewable_energy_text = i[17]
                if d_renewable_energy_text is None:
                    d_renewable_energy_text = []
                else:
                    d_renewable_energy_text = d_renewable_energy_text.split(
                        "~")

                ps_financing_asset = i[18]
                if ps_financing_asset is None:
                    ps_financing_asset = ""

                ps_proceeds_allocation = i[19]
                if ps_proceeds_allocation is None:
                    ps_proceeds_allocation = ""

                pe_portfolio_approach = i[20]
                if pe_portfolio_approach is None:
                    pe_portfolio_approach = ""

                pe_assessment_procedure = i[21]
                if pe_assessment_procedure is None:
                    pe_assessment_procedure = ""

                pm_proceed_type = i[22]
                if pm_proceed_type is None:
                    pm_proceed_type = ""

                pm_proceed_detail = i[23]
                if pm_proceed_detail is None:
                    pm_proceed_detail = ""

                pm_proceed_timing = i[24]
                if pm_proceed_timing is None:
                    pm_proceed_timing = ""

                pm_proceed_use = i[25]
                if pm_proceed_use is None:
                    pm_proceed_use = ""

                ar_report_interval = i[26]
                if ar_report_interval is None:
                    ar_report_interval = ""

                ar_report_format = i[27]
                if ar_report_format is None:
                    ar_report_format = ""

                ar_report_access = i[28]
                if ar_report_access is None:
                    ar_report_access = ""

                ar_report_link = i[29]
                if ar_report_link is None:
                    ar_report_link = ""

                ar_report_breakdown = i[30]
                if ar_report_breakdown is None:
                    ar_report_breakdown = ""

                ir_report_interval = i[31]
                if ir_report_interval is None:
                    ir_report_interval = ""

                ir_report_format = i[32]
                if ir_report_format is None:
                    ir_report_format = ""

                ir_report_access = i[33]
                if ir_report_access is None:
                    ir_report_access = ""

                ir_report_link = i[34]
                if ir_report_link is None:
                    ir_report_link = ""

                ir_report_indicators = i[35]
                if ir_report_indicators is None:
                    ir_report_indicators = ""

                ci_address_head_office = i[36]
                if ci_address_head_office is None:
                    ci_address_head_office = ""

                ci_vat_number = i[37]
                if ci_vat_number is None:
                    ci_vat_number = ""

                ci_business_reg_number = i[38]
                if ci_business_reg_number is None:
                    ci_business_reg_number = ""

                cp_name = i[39]
                if cp_name is None:
                    cp_name = ""

                cp_position = i[40]
                if cp_position is None:
                    cp_position = ""

                cp_company = i[41]
                if cp_company is None:
                    cp_company = ""

                cp_contact_number = i[42]
                if cp_contact_number is None:
                    cp_contact_number = ""

                id_name = i[43]
                if id_name is None:
                    id_name = ""

                ca_application_date = i[44]
                if ca_application_date is None:
                    ca_application_date = ""

                ca_legal_name_issuing_entity = i[45]
                if ca_legal_name_issuing_entity is None:
                    ca_legal_name_issuing_entity = ""

                ca_unique_name_debt_instruments = i[46]
                if ca_unique_name_debt_instruments is None:
                    ca_unique_name_debt_instruments = ""

                ca_address = i[47]
                if ca_address is None:
                    ca_address = ""

                ca_email_address = i[48]
                if ca_email_address is None:
                    ca_email_address = ""

                ca_contact_person = i[49]
                if ca_contact_person is None:
                    ca_contact_person = ""

                ca_signature = i[50]
                if ca_signature is None:
                    ca_signature = ""

                single_issuer_agreement = i[51]
                if single_issuer_agreement is None:
                    single_issuer_agreement = ""

                verifier_agreement = i[52]
                if verifier_agreement is None:
                    verifier_agreement = ""

                resp_data = {"certificationId": i[1],
                             "userEmail": i[2],
                             "certificationStatus": i[3],
                             "instrumentType": i[4],
                             "certificationType": 'post',
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
                             "gbAssuranceReport": verifier_agreement.split("/")[-1]}
                post_certifications.append(resp_data)

            return {'recentCertifications': post_certifications}, 200
        else:
            return {'recentCertifications': []}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422



def delete_certification(data,psql):

    try:
        certification_id = data['certificationId']
        certification_type = data['certificationType']

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        if certification_type == 'pre':
            cur.execute(f"DELETE from cbi_certification_queue WHERE certification_id='{certification_id}' and certification_type='pre'")
            con.commit()
            cur.execute(f"DELETE from cbi_pre_issuance_certification WHERE certification_id='{certification_id}'")
            con.commit()
        elif certification_type == 'post':    
            cur.execute(f"DELETE from cbi_certification_queue WHERE certification_id='{certification_id}' and certification_type='post'")
            con.commit()
            cur.execute(f"DELETE from cbi_post_issuance_certification WHERE certification_id='{certification_id}'")
            con.commit()
        elif certification_type == 'bondRedemption':
            cur.execute(f"DELETE from cbi_certification_queue WHERE certification_id='{certification_id}' and certification_type='bond_redemption'")
            con.commit()
            cur.execute(f"DELETE from cbi_bond_redemption WHERE certification_id='{certification_id}'")
            con.commit()
        else:
            con.close()
            return {'error': 'Invalid Certification Type'}, 422

        con.close()

        return {'message': 'Certification Deleted Successfully'}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422

