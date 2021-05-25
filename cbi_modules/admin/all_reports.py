import psycopg2


def get_certifications(psql):

    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"(select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, d_renewable_energy, d_renewable_energy_text, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement,'post' as certification_type from cbi_post_issuance_certification) UNION (select id, certification_id, user_email_address, certification_status, instrument_type, da_name, da_issuance_country, da_cusip, da_isin, da_local_currency_lc, da_amount_issued_lc, da_coupon, da_underwriter, da_issue_date, da_maturity_date, da_instrument_type, d_renewable_energy, d_renewable_energy_text, ps_financing_asset, ps_proceeds_allocation, pe_portfolio_approach, pe_assessment_procedure, pm_proceed_type, pm_proceed_detail, pm_proceed_timing, pm_proceed_use, ar_report_interval, ar_report_format, ar_report_access, ar_report_link, ar_report_breakdown, ir_report_interval, ir_report_format, ir_report_access, ir_report_link, ir_report_indicators, ci_address_head_office, ci_vat_number, ci_business_reg_number, cp_name, cp_position, cp_company, cp_contact_number, id_name, ca_application_date, ca_legal_name_issuing_entity, ca_unique_name_debt_instruments, ca_address, ca_email_address, ca_contact_person, ca_signature, single_issuer_agreement, verifier_agreement,'pre' as certification_type from cbi_pre_issuance_certification);")
        data = cur.fetchall()

        cur.execute(f"(select a.id, a.certification_id, a.user_email_address, a.certification_status, a.file1, a.file2, a.file3, a.file4, a.file5, a.application_date,b.da_name,b.instrument_type from cbi_bond_redemption a left join cbi_pre_issuance_certification b on a.certification_id=b.certification_id);")
        data1 = cur.fetchall()

        con.commit()
        con.close()
        if len(data)!=0:

            all_certifications = []

            for i in data:
                con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                       password=psql['password'], host=psql['host'], port=psql['port'])

                cur = con.cursor()

                cur.execute(f" select reviewer from cbi_certification_queue where certification_id='{i[1]}' and certification_type='{i[53]}';")
                try:
                    reviewer = str(cur.fetchone()[0])
                except:
                    reviewer= ""

                con.commit()

                cur.execute(f"SELECT string_agg(files, ',') AS file_list FROM CBI_Annual_Reports where certification_id='{i[1]}' GROUP BY certification_id;")
                try:
                    annual_reports_data = str(cur.fetchone()[0]).split(",")
                    annual_reports = []
                    for rep_value in range(len(annual_reports_data)):
                        heading = "Annual Report "+str(rep_value+1)
                        rep_data = {"name":heading,"path": annual_reports_data[rep_value]}
                        annual_reports.append(rep_data)
                except:
                    annual_reports = []
                    
                con.commit()

                cur.execute(f"SELECT user_company,user_first_name ,user_last_name,user_category,invoice_company_name from CBI_User  WHERE user_email_address='{i[2]}'")
                verifier = cur.fetchone()
                con.commit()

                if verifier is None:
                    verifier = ["", "", "", ""]

                signed_doc = None
                if verifier[3].lower() == "singleissuer":
                    cur.execute(
                        f"select signed_agreement from cbi_single_signed_agreement WHERE certification_id='{i[1]}'")
                    try:
                        signed_doc = cur.fetchone()[0]
                    except:
                        pass
                    con.commit()
                if verifier[3].lower() == "programmaticissuer":
                    cur.execute(
                        f"select signed_agreement from cbi_programmatic_signed_agreement WHERE invoice_company_name='{verifier[4]}'")
                    try:
                        signed_doc = cur.fetchone()[0]
                    except:
                        pass
                    con.commit()
                if verifier[3].lower() == "verifier":
                    cur.execute(
                        f"select signed_agreement from cbi_programmatic_signed_agreement WHERE invoice_company_name='{verifier[4]}'")
                    try:
                        signed_doc = cur.fetchone()[0]
                    except:
                        pass
                    con.commit()

                if signed_doc is None:
                    signed_doc = ""
                else:
                    annual_reports.append(
                        {"name": "Signed Agreement", "path": signed_doc.split("/")[-1]})

                con.close()

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

                    annual_reports.append({"name":"Certificate","path": certificate})
                    annual_reports.append({"name": "Approval", "path": approval})

                ca_assurance_report = single_issuer_agreement.split("/")[-1]
                if ca_assurance_report != "":
                    annual_reports.append({"name": "Assurance Report", "path": ca_assurance_report})

                gb_assurance_report = verifier_agreement.split("/")[-1]
                if gb_assurance_report != "":
                    annual_reports.append({"name": "Green Bond Framework", "path": gb_assurance_report})


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
                        "approval":approval,
                        "reviewer": reviewer,
                        "downloads":annual_reports}
                all_certifications.append(resp_data)
            if len(data1) != 0:
                for j in data1:
                    con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                           password=psql['password'], host=psql['host'], port=psql['port'])

                    cur = con.cursor()

                    cur.execute(
                        f" select reviewer from cbi_certification_queue where certification_id='{j[1]}' and certification_type='bond_redemption';")
                    try:
                        reviewer = str(cur.fetchone()[0])
                    except:
                        reviewer= ""

                    con.commit()

                    cur.execute(f"SELECT string_agg(files, ',') AS file_list FROM CBI_Annual_Reports where certification_id='{j[1]}' GROUP BY certification_id;")
                    try:
                        annual_reports_data = str(cur.fetchone()[0]).split(",")
                        annual_reports = []
                        for rep_value in range(len(annual_reports_data)):
                            heading = "Annual Report "+str(rep_value+1)
                            rep_data = {"name":heading, "path": annual_reports_data[rep_value]}
                            annual_reports.append(rep_data)
                    except:
                        annual_reports = []

                    con.commit()

                    cur.execute(
                        f"SELECT user_company,user_first_name ,user_last_name,user_category,invoice_company_name from CBI_User  WHERE user_email_address='{j[2]}'")
                    verifier = cur.fetchone()
                    con.commit()

                    if verifier is None:
                        verifier = ["", "", "", ""]

                    signed_doc = None
                    if verifier[3].lower() == "singleissuer":
                        cur.execute(
                            f"select signed_agreement from cbi_single_signed_agreement WHERE certification_id='{j[1]}'")
                        try:
                            signed_doc = cur.fetchone()[0]
                        except:
                            pass
                        con.commit()
                    if verifier[3].lower() == "programmaticissuer":
                        cur.execute(
                            f"select signed_agreement from cbi_programmatic_signed_agreement WHERE invoice_company_name='{verifier[4]}'")
                        try:
                            signed_doc = cur.fetchone()[0]
                        except:
                            pass
                        con.commit()
                    if verifier[3].lower() == "verifier":
                        cur.execute(
                            f"select signed_agreement from cbi_programmatic_signed_agreement WHERE invoice_company_name='{verifier[4]}'")
                        try:
                            signed_doc = cur.fetchone()[0]
                        except:
                            pass
                        con.commit()

                    if signed_doc is None:
                        signed_doc = ""
                    else:
                        annual_reports.append(
                            {"name": "Signed Agreement", "path": signed_doc.split("/")[-1]})



                    con.close()

                    certification_status = j[3]
                    if certification_status != "approved":
                        certificate = ""
                        approval = ""
                    else:
                        certificate = f"certificate_"+str(j[1])+"_bond_redemption.pdf"
                        approval = "approval_"+str(j[1])+"_bond_redemption.pdf.pdf"

                        annual_reports.append({"name":"Certificate","path": certificate})
                        annual_reports.append({"name":"Approval","path": approval})
                    
                    try:
                        file1 = j[4].split("/")[-1]
                        downloads_file1 = file1.split(".")[0].split("_")[-1]
                        annual_reports.append({"name":downloads_file1,"path": file1})
                    except:
                        file1 = ""
                        downloads_file1 = ""

                    try:
                        file2 = j[5].split("/")[-1]
                        downloads_file2 = file2.split(".")[0].split("_")[-1]
                        annual_reports.append({"name":downloads_file2,"path": file2})
                    except:
                        file2 = ""
                        downloads_file2 = ""

                    try:
                        file3 = j[6].split("/")[-1]
                        downloads_file3 = file3.split(".")[0].split("_")[-1]
                        annual_reports.append({"name": downloads_file3, "path": file3})
                    except:
                        file3 = ""
                        downloads_file3 = ""

                    try:
                        file4 = j[7].split("/")[-1]
                        downloads_file4 = file4.split(".")[0].split("_")[-1]
                        annual_reports.append({"name":downloads_file4,"path": file4})
                    except:
                        file4 = ""
                        downloads_file4 = ""

                    try:
                        file5 = j[8].split("/")[-1]
                        downloads_file5 = file5.split(".")[0].split("_")[-1]
                        annual_reports.append({"name":downloads_file5,"path": file5})
                    except:
                        file5 = ""
                        downloads_file5 = ""


                    resp_data1 = {"certificationId": j[1],
                                    "userEmail": j[2],
                                    "certificationStatus": j[3],
                                    "instrumentType": j[11],
                                    "certificationType": "bondRedemption",
                                    "uniqueName": j[10],
                                    "file1": file1,
                                    "file2": file2,
                                    "file3": file3,
                                    "file4": file4,
                                    "file5": file5,
                                    "applicationDate": j[9],
                                    "certificate": certificate,
                                    "approval": approval,
                                    "reviewer": reviewer,
                                    "downloads": annual_reports}
                    all_certifications.append(resp_data1)
                            
            return {'recentCertifications': all_certifications}, 200
        
        else:
            return {'recentCertifications': []}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422

def validate_admin(user_email_address, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(
            f"SELECT user_id, user_first_name, user_last_name, user_company, user_email_address, user_password, user_category, user_location, invoice_company_name, invoice_registration_number, invoice_billing_address, invoice_email_address, invoice_phone_number, user_job_title from CBI_User  WHERE user_email_address='{user_email_address}' and user_category='admin'")
        admin = cur.fetchone()
        con.commit()
        con.close()

        if admin is None:
            return 0
        else:
            return 1

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
