import psycopg2


def dashboard(user_email_address, filter_date, date_value, psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        # Total
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}';")
            total_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            total_count = "0"

        # Completed
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and certification_status='approved';")
            approved_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            approved_count = "0"

        # in review
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and certification_status='in-review';")
            in_review_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            in_review_count = "0"

        # Assigned_certification
        try:
            cur.execute(f"select user_company, certification_id, application_date, assigned_date,certification_company ,certification_type from cbi_certification_queue where reviewer='{user_email_address}' and certification_status='in-review';")
            my_certifications = cur.fetchall()
            con.commit()

            assigned_certifications = []
            # if len(my_certifications) ==0:
            for i in my_certifications:
                if i[5]=='bond_redemption':
                    cert_type = 'bondRedemption'
                else:
                    cert_type = i[5]
                data = {'userCompany': i[0],'certificationId': i[1], 'applicationDate': i[2],'assignedDate': i[3],'certificationCompany': i[4], 'certificationType': cert_type}
                assigned_certifications.append(data)
        except:
            assigned_certifications = "0"

        # debt instrument pie chart
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and instrument_type='bond' {date_value};")
            bond_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bond_count = "0"

        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and instrument_type='loan' {date_value};")
            loan_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            loan_count = "0"

        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and instrument_type='deposit' {date_value};")
            deposit_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            deposit_count = "0"

        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and instrument_type='others' {date_value};")
            others_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            others_count = "0"

        # Certification type bar chart
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and certification_type='pre' {date_value};")
            pre_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            pre_count = "0"

        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and certification_type='post' {date_value};")
            post_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            post_count = "0"

        try:
            cur.execute(f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and certification_type='bond_redemption' {date_value};")
            bond_redemption_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bond_redemption_count = "0"

        # underwriter bar chart
        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%AECLU%' {date_value};")
            AECLU_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            AECLU_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%bam%' {date_value};")
            bam_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bam_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%bzgfcl%' {date_value};")
            bzgfcl_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bzgfcl_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%blockc%' {date_value};")
            blockc_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            blockc_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%bsu%' {date_value};")
            bsu_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bsu_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%bvBrazil%' {date_value};")
            bvBrazil_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bvBrazil_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%bvUK%' {date_value};")
            bvUK_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bvUK_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%cca%' {date_value};")
            cca_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            cca_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%ct%' {date_value};")
            ct_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            ct_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%cecep%' {date_value};")
            cecep_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            cecep_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%ccx%' {date_value};")
            ccx_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            ccx_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%clEIA%' {date_value};")
            clEIA_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            clEIA_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%cqc%' {date_value};")
            cqc_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            cqc_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%deloitte%' {date_value};")
            deloitte_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            deloitte_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%dnv%' {date_value};")
            dnv_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            dnv_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%dqs%' {date_value};")
            dqs_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            dqs_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%evi%' {date_value};")
            evi_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            evi_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%epicsustainability%' {date_value};")
            epicsustainability_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            epicsustainability_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%eqa%' {date_value};")
            eqa_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            eqa_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%ermCvs%' {date_value};")
            ermCvs_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            ermCvs_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%ey%' {date_value};")
            ey_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            ey_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%fe%' {date_value};")
            fe_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            fe_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%gcs%' {date_value};")
            gcs_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            gcs_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%gs%' {date_value};")
            gs_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            gs_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%hkqaa%' {date_value};")
            hkqaa_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            hkqaa_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%hrRatings%' {date_value} {date_value};")
            hrRatings_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            hrRatings_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%ibis%' {date_value} {date_value};")
            ibis_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            ibis_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%iGreenBank%' {date_value} {date_value};")
            iGreenBank_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            iGreenBank_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%induforOy%' {date_value};")
            induforOy_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            induforOy_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%iss%' {date_value};")
            iss_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            iss_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%jcr%' {date_value};")
            jcr_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            jcr_count = "0"
            
        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%kestrelVerifiers%' {date_value};")
            kestrelVerifiers_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            kestrelVerifiers_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%KPMG%' {date_value};")
            KPMG_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            KPMG_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%multiconsultASA%' {date_value};")
            multiconsultASA_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            multiconsultASA_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%NSFCertification%' {date_value};")
            NSFCertification_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            NSFCertification_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%pcr%' {date_value};")
            pcr_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            pcr_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%PwC%' {date_value};")
            PwC_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            PwC_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%raisingCleantech%' {date_value};")
            raisingCleantech_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            raisingCleantech_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%ramSustainability%' {date_value};")
            ramSustainability_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            ramSustainability_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%rsmAustralia%' {date_value};")
            rsmAustralia_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            rsmAustralia_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%rubicola%' {date_value};")
            rubicola_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            rubicola_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%scopeGroup%' {date_value};")
            scopeGroup_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            scopeGroup_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%sgs%' {date_value};")
            sgs_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            sgs_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%sinoCarbon%' {date_value};")
            sinoCarbon_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            sinoCarbon_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%sitawi%' {date_value};")
            sitawi_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            sitawi_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%sustainAdvisory%' {date_value};")
            sustainAdvisory_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            sustainAdvisory_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%sustainalytics%' {date_value};")
            sustainalytics_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            sustainalytics_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%synTaoGreenFinance%' {date_value};")
            synTaoGreenFinance_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            synTaoGreenFinance_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%trisRating%' {date_value};")
            trisRating_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            trisRating_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%tuvNord%' {date_value};")
            tuvNord_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            tuvNord_count = "0"

        try:
            cur.execute(
                f"select count(*) from cbi_certification_queue where reviewer='{user_email_address}' and underwriter ilike '%vigeoEiris%' {date_value};")
            vigeoEiris_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            vigeoEiris_count = "0"


        con.close()

        return {
            'dashboardStats': {'total': total_count, 'completed': approved_count, 'in-review': in_review_count},
            'assignedCertifications': assigned_certifications,
            'chartData': {'certificationType': [{'name': 'preIssuance', 'value': pre_count}, {'name': 'postIssuance', 'value': post_count}, {'name': 'bondRedemption', 'value': bond_redemption_count}],
            'debtInstruments': [{'name': 'bond', 'value': bond_count}, {'name': 'loan', 'value': loan_count}, {'name': 'deposit', 'value': deposit_count}, {'name': 'others', 'value': others_count}],'underwriter': [{'name': 'AECLU', 'value': AECLU_count}, {'name': 'BAM', 'value': bam_count}, {'name': 'Beijing Zhongcai Green Financing Consultants Ltd', 'value': bzgfcl_count}, {'name': 'BlockC', 'value': blockc_count}, {'name': 'Blue Snow Consulting', 'value': bsu_count}, {'name': 'Bureau Veritas (Brazil)', 'value': bvBrazil_count}, {'name': 'Bureau Veritas', 'value': bvUK_count}, {'name': 'Carbon Care Asia Limited', 'value': cca_count}, {'name': 'Carbon TrustCarbon Trust', 'value': ct_count}, {'name': 'CECEP', 'value': cecep_count}, {'name': 'China Chengxin Credit Management Co.', 'value': ccx_count}, {'name': 'China Lianhe EIA', 'value': clEIA_count}, {'name': 'China Quality Certification Centre', 'value': cqc_count}, {'name': 'Deloitte', 'value': deloitte_count}, {'name': 'DNV.GL', 'value': dnv_count}, {'name': 'DQS CFS', 'value': dqs_count}, {'name': 'Emergent Ventures India', 'value': evi_count}, {'name': 'EPIC Sustainability', 'value': epicsustainability_count}, {'name': 'EQA Spain', 'value': eqa_count}, {'name': 'ERM CVS', 'value': ermCvs_count}, {'name': 'EY', 'value': ey_count}, {'name': 'First Environment', 'value': fe_count}, {'name': 'Golden Credit Service Co. Ltd.', 'value': gcs_count}, {'name': 'Greensolver', 'value': gs_count}, {'name': 'HKQAA', 'value': hkqaa_count}, {'name': 'HR Ratings', 'value': hrRatings_count}, {'name': 'IBIS ESG Consulting', 'value': ibis_count}, {'name': 'iGreenBank', 'value': iGreenBank_count}, {'name': 'Indufor Oy', 'value': induforOy_count}, {'name': 'ISS ESG', 'value': iss_count}, {'name': 'Japan Credit Rating Agency, Ltd.', 'value': jcr_count}, {'name': 'Kestrel Verifiers', 'value': kestrelVerifiers_count}, {'name': 'KPMG', 'value': KPMG_count}, {'name': 'Multiconsult ASA', 'value': multiconsultASA_count}, {'name': 'NSF Certification, LLC', 'value': NSFCertification_count}, {'name': 'Pacific Credit Rating', 'value': pcr_count}, {'name': 'PwC', 'value': PwC_count}, {'name': 'Raising Clean-tech Investment Consulting Co., Ltd.', 'value': raisingCleantech_count}, {'name': 'RAM Sustainability', 'value': ramSustainability_count}, {'name': 'RSM Australia', 'value': rsmAustralia_count}, {'name': 'Rubicola Consulting', 'value': rubicola_count}, {'name': 'Scope Group', 'value': scopeGroup_count}, {'name': 'SGS Hong Kong', 'value': sgs_count}, {'name': 'SinoCarbon', 'value': sinoCarbon_count}, {'name': 'SITAWI', 'value': sitawi_count}, {'name': 'SustainAdvisory', 'value': sustainAdvisory_count}, {'name': 'Sustainalytics', 'value': sustainalytics_count}, {'name': 'SynTao Green Finance', 'value': synTaoGreenFinance_count}, {'name': 'TRIS Rating', 'value': trisRating_count}, {'name': 'TÜV NORD CERT', 'value': tuvNord_count}, {'name': 'Vigeo Eiris', 'value': vigeoEiris_count} ]}
                          
        }, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
