import psycopg2

def dashboard(data, psql):

    try:
        user_email_address = data['userEmail']

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()
        
        try:
            cur.execute(f"select ((select count(*) from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}')+(select count(*) from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}')) as total;")
            total_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            total_count = "0"

        try:
            cur.execute(f"select ((select count(*) from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='submitted')+(select count(*) from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='submitted')) as total;")
            submitted_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            submitted_count = "0"

        try:
            cur.execute(f"select ((select count(*) from cbi_pre_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='draft')+(select count(*) from cbi_post_issuance_certification WHERE user_email_address='{user_email_address}' AND certification_status='draft')) as total;")
            draft_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            draft_count = "0"

        try:
            cur.execute(
                f"SELECT * FROM cbi_pre_issuance_certification pre WHERE NOT EXISTS (SELECT * FROM cbi_post_issuance_certification post WHERE pre.certification_id = post.certification_id ) and user_email_address='{user_email_address}' and certification_status='draft' ORDER BY id DESC LIMIT 5;")
            pre_recent_five_data = cur.fetchall()

            pre_len = len(pre_recent_five_data)
            post_len = 5-pre_len

            if post_len != 0:
                cur.execute(
                    f"SELECT * FROM cbi_post_issuance_certification post WHERE EXISTS (SELECT * FROM cbi_pre_issuance_certification pre WHERE pre.certification_id = post.certification_id ) and certification_status='draft' and user_email_address='{user_email_address}' ORDER BY id DESC LIMIT '{post_len}' ;")
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
            recent_certifications = "0"

        con.close()

        if total_count == "0":
            return {'stats': {'total': '0', 'submitted': '0', 'inprogress': '0'}, 'recentCertifications': []}, 200
        else:
            return {'stats': {'total': total_count, 'submitted': submitted_count, 'inprogress': draft_count},'recentCertifications': recent_certifications}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
