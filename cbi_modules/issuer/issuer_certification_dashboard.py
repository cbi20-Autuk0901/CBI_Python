import psycopg2

def dashboard(data, psql):

    try:
        user_email_address = data['userEmail']

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()
        
        try:
            cur.execute(f"select ((select count(*) from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}' and certification_status!='draft')+(select count(*) from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}' and certification_status!='draft')+(select count(*) from cbi_bond_redemption WHERE user_email_address='{user_email_address}')) as total;")
            total_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            total_count = "0"

        try:
            cur.execute(
                f"select ((select count(*) from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='approved')+(select count(*) from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='approved')+(select count(*) from cbi_bond_redemption WHERE user_email_address='{user_email_address}' AND certification_status='approved')) as total;")
            submitted_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            submitted_count = "0"

        try:
            cur.execute(
                f"select ((select count(*) from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='in-review')+(select count(*) from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='in-review')+(select count(*) from cbi_bond_redemption WHERE user_email_address='{user_email_address}' AND certification_status='in-review')) as total;")
            draft_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            draft_count = "0"

        try:
            cur.execute(
                f"SELECT pre.id, pre.certification_id, pre.user_email_address, pre.certification_status, pre.instrument_type, pre.da_name, pre.da_issuance_country, pre.da_cusip, pre.da_isin, pre.da_local_currency_lc, pre.da_amount_issued_lc, pre.da_coupon, pre.da_underwriter, pre.da_issue_date, pre.da_maturity_date, pre.da_instrument_type, pre.d_renewable_energy, pre.d_renewable_energy_text, pre.ps_financing_asset, pre.ps_proceeds_allocation, pre.pe_portfolio_approach, pre.pe_assessment_procedure, pre.pm_proceed_type, pre.pm_proceed_detail, pre.pm_proceed_timing, pre.pm_proceed_use, pre.ar_report_interval, pre.ar_report_format, pre.ar_report_access, pre.ar_report_link, pre.ar_report_breakdown, pre.ir_report_interval, pre.ir_report_format, pre.ir_report_access, pre.ir_report_link, pre.ir_report_indicators, pre.ci_address_head_office, pre.ci_vat_number, pre.ci_business_reg_number, pre.cp_name, pre.cp_position, pre.cp_company, pre.cp_contact_number, pre.id_name, pre.ca_application_date, pre.ca_legal_name_issuing_entity, pre.ca_unique_name_debt_instruments, pre.ca_address, pre.ca_email_address, pre.ca_contact_person, pre.ca_signature, pre.single_issuer_agreement, pre.verifier_agreement FROM cbi_pre_issuance_certification pre WHERE NOT EXISTS (SELECT post.id, post.certification_id, post.user_email_address, post.certification_status, post.instrument_type, post.da_name, post.da_issuance_country, post.da_cusip, post.da_isin, post.da_local_currency_lc, post.da_amount_issued_lc, post.da_coupon, post.da_underwriter, post.da_issue_date, post.da_maturity_date, post.da_instrument_type, post.ps_financing_asset, post.ps_proceeds_allocation, post.pe_portfolio_approach, post.pe_assessment_procedure, post.pm_proceed_type, post.pm_proceed_detail, post.pm_proceed_timing, post.pm_proceed_use, post.ar_report_interval, post.ar_report_format, post.ar_report_access, post.ar_report_link, post.ar_report_breakdown, post.ir_report_interval, post.ir_report_format, post.ir_report_access, post.ir_report_link, post.ir_report_indicators, post.d_renewable_energy, post.d_renewable_energy_text, post.ci_address_head_office, post.ci_vat_number, post.ci_business_reg_number, post.cp_name, post.cp_position, post.cp_company, post.cp_contact_number, post.id_name, post.ca_application_date, post.ca_legal_name_issuing_entity, post.ca_unique_name_debt_instruments, post.ca_address, post.ca_email_address, post.ca_contact_person, post.ca_signature, post.single_issuer_agreement, post.verifier_agreement FROM cbi_post_issuance_certification post WHERE pre.certification_id = post.certification_id ) and pre.user_email_address='{user_email_address}' and pre.certification_status='draft' ORDER BY pre.id DESC LIMIT 5;")
            pre_recent_five_data = cur.fetchall()

            pre_len = len(pre_recent_five_data)
            post_len = 5-pre_len

            if post_len != 0:
                cur.execute(
                    f"SELECT post.id, post.certification_id, post.user_email_address, post.certification_status, post.instrument_type, post.da_name, post.da_issuance_country, post.da_cusip, post.da_isin, post.da_local_currency_lc, post.da_amount_issued_lc, post.da_coupon, post.da_underwriter, post.da_issue_date, post.da_maturity_date, post.da_instrument_type, post.ps_financing_asset, post.ps_proceeds_allocation, post.pe_portfolio_approach, post.pe_assessment_procedure, post.pm_proceed_type, post.pm_proceed_detail, post.pm_proceed_timing, post.pm_proceed_use, post.ar_report_interval, post.ar_report_format, post.ar_report_access, post.ar_report_link, post.ar_report_breakdown, post.ir_report_interval, post.ir_report_format, post.ir_report_access, post.ir_report_link, post.ir_report_indicators, post.d_renewable_energy, post.d_renewable_energy_text, post.ci_address_head_office, post.ci_vat_number, post.ci_business_reg_number, post.cp_name, post.cp_position, post.cp_company, post.cp_contact_number, post.id_name, post.ca_application_date, post.ca_legal_name_issuing_entity, post.ca_unique_name_debt_instruments, post.ca_address, post.ca_email_address, post.ca_contact_person, post.ca_signature, post.single_issuer_agreement, post.verifier_agreement FROM cbi_post_issuance_certification post WHERE EXISTS (SELECT pre.id, pre.certification_id, pre.user_email_address, pre.certification_status, pre.instrument_type, pre.da_name, pre.da_issuance_country, pre.da_cusip, pre.da_isin, pre.da_local_currency_lc, pre.da_amount_issued_lc, pre.da_coupon, pre.da_underwriter, pre.da_issue_date, pre.da_maturity_date, pre.da_instrument_type, pre.d_renewable_energy, pre.d_renewable_energy_text, pre.ps_financing_asset, pre.ps_proceeds_allocation, pre.pe_portfolio_approach, pre.pe_assessment_procedure, pre.pm_proceed_type, pre.pm_proceed_detail, pre.pm_proceed_timing, pre.pm_proceed_use, pre.ar_report_interval, pre.ar_report_format, pre.ar_report_access, pre.ar_report_link, pre.ar_report_breakdown, pre.ir_report_interval, pre.ir_report_format, pre.ir_report_access, pre.ir_report_link, pre.ir_report_indicators, pre.ci_address_head_office, pre.ci_vat_number, pre.ci_business_reg_number, pre.cp_name, pre.cp_position, pre.cp_company, pre.cp_contact_number, pre.id_name, pre.ca_application_date, pre.ca_legal_name_issuing_entity, pre.ca_unique_name_debt_instruments, pre.ca_address, pre.ca_email_address, pre.ca_contact_person, pre.ca_signature, pre.single_issuer_agreement, pre.verifier_agreement FROM cbi_pre_issuance_certification pre WHERE pre.certification_id = post.certification_id ) and post.certification_status='draft' and post.user_email_address='{user_email_address}' ORDER BY id DESC LIMIT '{post_len}' ;")
                post_recent_five_data = cur.fetchall()

            con.commit()

            recent_certifications = []
            for i in pre_recent_five_data:
                data = {'certificationId': i[1], 'instrumentType': i[4],'certificationType':'pre'}
                recent_certifications.append(data)
            if post_len !=0:
                for i in post_recent_five_data:
                    data = {'certificationId': i[1], 'instrumentType': i[4],'certificationType':'post'}
                    recent_certifications.append(data)
        except:
            recent_certifications = []


        try:
            cur.execute(
                f"select t1.certification_id,t1.certification_status,t2.certification_status,t3.certification_status,t1.instrument_type from cbi_pre_issuance_certification t1 left join cbi_post_issuance_certification t2 on t1.certification_id=t2.certification_id left join cbi_bond_redemption t3 on t1.certification_id=t3.certification_id where t1.user_email_address = '{user_email_address}' order by t1.ca_application_date desc limit 1;")
            data = cur.fetchone()
            recent_cert_status = {"certificationId": data[0], "pre": data[1], "post": data[2], "bondRedemption": data[3], "instrumentType": data[4]}
            con.commit()
        except:
            recent_cert_status = "0"

        con.close()

        if total_count == "0":
            return {'stats': {'total': '0', 'approved': '0', 'inprogress': '0'}, 'recentCertifications': recent_certifications, 'recentCertificationStatus': {"certificationId": None, "pre": None, "post": None, "bondRedemption": None}}, 200
        else:
            return {'stats': {'total': total_count, 'approved': submitted_count, 'inprogress': draft_count},'recentCertifications': recent_certifications,'recentCertificationStatus':recent_cert_status}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
