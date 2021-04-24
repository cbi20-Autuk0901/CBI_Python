import psycopg2

def rev_email(psql):
    try:
        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                                password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        cur.execute(f"SELECT user_email_address from CBI_User  WHERE user_category='reviewer'")
        user_data = cur.fetchall()
        temp = [i[0] for i in user_data]

        con.close()

        return {'reviewerEmail': temp}

    except Exception as e:
        error = str(e)
        msg = error

        return {'error': msg}, 422
