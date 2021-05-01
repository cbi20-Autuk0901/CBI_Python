import psycopg2

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def upload_report(certification_id, certification_type, file_1, fname, psql):

    con = psycopg2.connect(database=psql['database'], user=psql['user'],
                           password=psql['password'], host=psql['host'], port=psql['port'])

    cur = con.cursor()

    cur.execute(f"select id, certification_id, certification_type, certification_status, reviewer, application_date, assigned_date, approved_date, user_company, certification_company, instrument_type, underwriter from cbi_certification_queue where certification_id='{certification_id}' and certification_type='{certification_type}';")
    user = cur.fetchone()

    con.close()

    if user is None:
        return {"error": "Invalid Certification"}, 401
    else:
        mail_annual_report(file_1,fname,user[4],certification_id, certification_type)
        return {'certificationId': user[1], 'certificationType': user[2]}, 200


def mail_annual_report(file_1,fname,reviewer,certification_id, certification_type):

    filename =  fname
    filepath = file_1

    sender = 'cbigithub@vigameq.com'
    recipient = reviewer

    body = f"""
            <html>
            <body><style> p {{ font-family: Palatino Linotype; }}</style><p>
            Hello, <br> <br>

            Annual Report has been submitted for certification Type : {certification_type} and Cerification ID : {certification_id}.
 
            
            <br><br> <br>
            <i>The Climate Bonds Certification Team</i>
            
            </p>
            
            </body></html>
                """
    msg = MIMEMultipart("alternative", None, [
        MIMEText(body), MIMEText(body, 'html')])
    msg['Subject'] = f"Annual Report of {certification_id}"
    msg['From'] = sender
    msg['To'] = recipient

    attachment = open(filepath, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',
                 "attachment; filename= %s" % filename)
    msg.attach(p)

    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    server.login(sender, 'Vigameq@i2R')
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
