import psycopg2


def dashboard(psql):

    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        # Total
        try:
            cur.execute(f"select count(*) from cbi_certification_queue")
            total_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            total_count = "0"

        # Completed/approved
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where certification_status='approved'")
            approved_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            approved_count = "0"

        # in review
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where certification_status='in-review'")
            in_review_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            in_review_count = "0"

        # unassigned
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where certification_status='submitted'")
            unassigned_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            unassigned_count = "0"

        # bond
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where instrument_type='bond';")
            bond_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            bond_count = "0"

        # loan
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where instrument_type='loan';")
            loan_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            loan_count = "0"

        #deposit
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where instrument_type='deposit';")
            deposit_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            deposit_count = "0"

        # others
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where instrument_type='others';")
            others_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            others_count = "0"

        # Low
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where extract(day from current_timestamp - assigned_date)>= 0 and extract(day from CURRENT_DATE - assigned_date)<= 5;")
            low_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            others_count = "0"

        # Medium
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where extract(day from current_timestamp - assigned_date)>= 6 and extract(day from CURRENT_DATE - assigned_date)<= 9;")
            medium_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            others_count = "0"

        # High
        try:
            cur.execute(f"select count(*) from cbi_certification_queue where extract(day from current_timestamp - assigned_date)>= 10;")
            high_count = str((cur.fetchone()[0]))
            con.commit()
        except:
            high_count = "0"

        # Reviewer stats
        try:
            cur.execute(f"select reviewer, count(*) from cbi_certification_queue group by reviewer;")
            reviewer_count = cur.fetchall()
            con.commit()
            reviewer_stats = []
            for i in reviewer_count:
                reviewer_stats.append({i[0]:i[1]})
        except:
            reviewer_count = "0"
            reviewer_stats = []

        # Months stats
        try:
            cur.execute('''
            SELECT to_char(current_timestamp, 'MONTH YYYY'), count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =0
            UNION
            SELECT to_char(current_timestamp- '1 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =1 
            UNION
            SELECT to_char(current_timestamp- '2 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =2 
            UNION
            SELECT to_char(current_timestamp- '3 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =3 
            UNION
            SELECT to_char(current_timestamp- '4 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =4
            UNION
            SELECT to_char(current_timestamp- '5 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =5
            UNION
            SELECT to_char(current_timestamp- '6 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =6
            UNION
            SELECT to_char(current_timestamp- '7 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =7
            UNION
            SELECT to_char(current_timestamp- '8 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =8
            UNION
            SELECT to_char(current_timestamp- '9 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =9
            UNION
            SELECT to_char(current_timestamp- '10 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =10
            UNION
            SELECT to_char(current_timestamp- '11 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =11
            UNION
            SELECT to_char(current_timestamp- '12 month'::interval, 'MONTH YYYY'),count(*) from cbi_certification_queue where (DATE_PART('month', current_timestamp)-DATE_PART('month', application_date)) =12

            ''')
            months_count = cur.fetchall()
            con.commit()
            months_stats = []
            for i in months_count:
                months_stats.append({i[0]: i[1]})
        except:
            months_count = "0"
            months_stats = []


        con.close()

        return {'dashboardStats': [{'total': total_count, 'completed': approved_count, 'in-review': in_review_count,"unassigned":unassigned_count,"bond":bond_count,"loan":loan_count,"deposit":deposit_count, "others":others_count, "low":low_count, "high":high_count,"medium":medium_count}], "reviewerStats":reviewer_stats,"monthlyStats":months_stats}, 200

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
