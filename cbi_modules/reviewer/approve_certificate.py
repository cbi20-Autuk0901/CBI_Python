import os

import psycopg2

import random

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from docxtpl import DocxTemplate


from datetime import datetime


def cert(cert_type,cert_id,psql):
    try:

        con = psycopg2.connect(database=psql['database'], user=psql['user'],
                               password=psql['password'], host=psql['host'], port=psql['port'])

        cur = con.cursor()

        now = datetime.now()
        now = str(now).split(" ")[0]

        if cert_type == 'bondRedemption':
                certification_type = 'bond_redemption'
        else:
            certification_type = cert_type

        query = f"UPDATE cbi_certification_queue SET approved_date='{now}',certification_status='approved' WHERE certification_type='{certification_type}'  AND certification_id='{cert_id}'; "
        cur.execute(query)
        con.commit()

        if cert_type == "pre":
            query = f"UPDATE cbi_pre_issuance_certification SET certification_status='approved' WHERE certification_id='{cert_id}'; "
            cur.execute(query)
            con.commit()
        elif cert_type == "post":
            query = f"UPDATE cbi_post_issuance_certification SET certification_status='approved' WHERE certification_id='{cert_id}'; "
            cur.execute(query)
            con.commit()
        elif cert_type == "bondRedemption":
            query = f"UPDATE cbi_bond_redemption SET certification_status='approved' WHERE certification_id='{cert_id}'; "
            cur.execute(query)
            con.commit()
            query1 = f"UPDATE cbi_post_issuance_certification SET certification_status='approved' WHERE certification_id='{cert_id}'; "
            cur.execute(query1)
            con.commit()

        if cert_type == "pre":
            cur.execute(f"SELECT instrument_type,ca_legal_name_issuing_entity,cp_name,ca_address,da_name, user_email_address, da_name from cbi_pre_issuance_certification WHERE certification_id='{cert_id}' ")
            data = cur.fetchone()
            con.commit()
            cur.execute(f"SELECT user_first_name,user_last_name from cbi_user WHERE user_email_address='{data[5]}' ")
            data_one = cur.fetchone()
            con.commit()
            issuer_name = data_one[0]+" "+data_one[1]

        elif cert_type == "post":
            cur.execute(f"SELECT instrument_type,ca_legal_name_issuing_entity,cp_name,ca_address,da_name, user_email_address, da_name from cbi_post_issuance_certification WHERE certification_id='{cert_id}'")
            data = cur.fetchone()
            con.commit()
            cur.execute(f"SELECT user_first_name,user_last_name from cbi_user WHERE user_email_address='{data[5]}' ")
            data_one = cur.fetchone()
            con.commit()
            issuer_name = data_one[0]+" "+data_one[1]

        elif cert_type == "bondRedemption":
            cur.execute(f"SELECT instrument_type,ca_legal_name_issuing_entity,cp_name,ca_address,da_name, user_email_address, da_name from cbi_post_issuance_certification WHERE certification_id='{cert_id}'")
            data = cur.fetchone()
            con.commit()
            cur.execute(f"SELECT user_first_name,user_last_name from cbi_user WHERE user_email_address='{data[5]}' ")
            data_one = cur.fetchone()
            con.commit()
            issuer_name = data_one[0]+" "+data_one[1]

        approval_date = now

        cp_name = data[2]
        if cp_name is None:
            cp_name = "no value"
        
        issuing_entity_legal_name = data[1]
        if issuing_entity_legal_name is None:
            issuing_entity_legal_name = "no value"

        cp_address = data[3]
        if cp_address is None:
            cp_address = "no value"

        unique_name = data[4]
        if unique_name is None:
            unique_name = "no value"

        instrument_type = data[0]
        if instrument_type is None:
            instrument_type = "no value"

        da_name = data[6]
        if da_name is None:
            da_name = "no value"


        con.close()

        generate_certificate(instrument_type, issuing_entity_legal_name, approval_date,cert_id,cert_type)
        if cert_type == "pre":
            generate_approval_pre(cert_id, cert_type, approval_date, cp_name, issuing_entity_legal_name, cp_address, unique_name)
            mail_issuer_pre(cert_id, cert_type,issuer_name, da_name,data[5])
        elif cert_type == "post":
            generate_approval_post(cert_id, cert_type, approval_date, cp_name, issuing_entity_legal_name, cp_address, unique_name)
            mail_issuer_post(cert_id, cert_type,issuer_name, da_name,data[5])
        elif cert_type == "bondRedemption":
            # mail_issuer_bond(cert_id, cert_type)
            pass



        return {'msg': "Email Sent Successfully"}, 200
    except Exception as e:
        error = str(e)
        return {'error': error}, 409

        
def mail_issuer_pre(cert_id, cert_type, issuer_name, da_name, user_email):
    try:
        paths = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

        filename1 = "certificate_"+str(cert_id)+"_"+str(cert_type)+".pdf"
        filepath1 = '/var/www/html/cbi-api/cbi_uploads/'+filename1

        filename2 = "approval_"+str(cert_id)+"_"+str(cert_type)+".pdf"
        filepath2 = '/var/www/html/cbi-api/cbi_uploads/'+filename2

        filename3 = "CBS_Certified-RGB.jpg"
        filepath3 = paths+'/template/'+filename3

        filename4 = "CBI Certification logo guidelines - 2020.pdf"
        filepath4 = paths+'/template/'+filename4

        sender = 'cbigithub@vigameq.com'
        recipient = user_email#['varunomkar007@gmail.com', 'naveenbodicherla@gmail.com','nithin.gangadhar@vigameq.com','vishwas.vidyaranya@climatebonds.net']


        body = f"""
                <html>
                <body><style> p {{ font-family: Palatino Linotype; }}</style><p>
                Dear {issuer_name}, <br> <br>
    
                We are pleased to formally confirm Pre-Issuance Certification by the Climate Bonds Standard Board of the proposed {da_name}, which will be issued by {issuer_name}. 
                <br><br>
                Please find attached the following documents for the Certification:  
                <br><br>
                1) A formal Letter of Certification for your records <br>
                2) A Certificate, for your promotional efforts <br>
                3) The Certification Mark file <br>
                4) Guidance on using the Certification Mark
                <br><br>
                Please be in touch with our communications team (leena.fatin@climatebonds.net) from the Climate Bonds Initiative Communications Team who can coordinate with you in case you plan to do any communications associated with the issuance of this bond. 
                <br><br>
                After your issuance, we will be producing an entry for our <a href="https://climatebonds.net/bond-library">Bond Library</a> and publishing the relevant documents on our <a href="https://www.climatebonds.net/certification/certified-bonds">Listing of Certified Bonds</a> on the Climate Bonds Initiative website. We will also send you an invoice for the Certification Fee, as per our signed Certification Agreement.
                <br><br>
                Please do not hesitate to contact us for clarifications or if there is anything we can do to help.  
                <br><br>
                Congratulations on your Certification! 
                <br>
                <i>The Climate Bonds Certification Team</i>
                
                </p>
                
                </body></html>
                    """
        msg = MIMEMultipart("alternative", None, [
            MIMEText(body), MIMEText(body, 'html')])
        msg['Subject'] = f"Confirmation of Pre-Issuance Certification of {da_name}"
        msg['From'] = sender
        msg['To'] = recipient#", ".join(recipient)

        attachment = open(filepath1, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename1)
        msg.attach(p)

        attachment1 = open(filepath2, "rb")
        p1 = MIMEBase('application', 'octet-stream')
        p1.set_payload((attachment1).read())
        encoders.encode_base64(p1)
        p1.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename2)
        msg.attach(p1)

        attachment2 = open(filepath3, "rb")
        p2 = MIMEBase('application', 'octet-stream')
        p2.set_payload((attachment2).read())
        encoders.encode_base64(p2)
        p2.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename3)
        msg.attach(p2)

        attachment3 = open(filepath4, "rb")
        p3 = MIMEBase('application', 'octet-stream')
        p3.set_payload((attachment3).read())
        encoders.encode_base64(p3)
        p3.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename4)
        msg.attach(p3)

        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        server.login(sender, 'Cbigithub@i2R')
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
    except Exception as e:
        error = str(e)
        return {'error': error}, 409


def mail_issuer_post(cert_id, cert_type, issuer_name, da_name, user_email):
    try:
        paths = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

        # filename1 = "certificate_"+str(cert_id)+"_"+str(cert_type)+".pdf"
        # filepath1 = '/var/www/html/cbi-api/cbi_uploads/'+filename1

        filename2 = "approval_"+str(cert_id)+"_"+str(cert_type)+".pdf"
        filepath2 = '/var/www/html/cbi-api/cbi_uploads/'+filename2

        filename3 = "CBS_Certified-RGB.jpg"
        filepath3 = paths+'/template/'+filename3

        filename4 = "CBI Certification logo guidelines - 2020.pdf"
        filepath4 = paths+'/template/'+filename4

        sender = 'cbigithub@vigameq.com'
        recipient = user_email#['varunomkar007@gmail.com', 'naveenbodicherla@gmail.com','nithin.gangadhar@vigameq.com','vishwas.vidyaranya@climatebonds.net']

        body = f"""
                <html>
                <body><style> p {{ font-family: Palatino Linotype;}}</style><p>
                Dear {issuer_name}, <br><br>
    
                We are pleased to formally confirm Post-Issuance Certification by the Climate Bonds Standard Board of the proposed {da_name}, which will be issued by {issuer_name}. 
                <br><br>
                Please find attached the following documents for the Certification:  
                <br><br>
                1) A formal Letter of Certification for your records <br>
                2) The Certification Mark file <br>
                3) Guidance on using the Certification Mark
                <br><br>
                We will proceed to add an entry for our <a href="https://climatebonds.net/bond-library">Bond Library</a> and publish the relevant documents on our <a href="https://www.climatebonds.net/certification/certified-bonds">Listing of Certified Bonds</a> on the Climate Bonds Initiative website. 
                <br><br><br>
                Please be in touch with our communications team (leena.fatin@climatebonds.net) from the Climate Bonds Initiative Communications Team who can coordinate with you in case you plan to do any communications associated with the post issuance certification of this bond. 
                <br><br>
                Please do not hesitate to contact us for clarifications or if there is anything we can do to help.   
                <br><br>
                Congratulations on your Certification! 
                <br>
                <i>The Climate Bonds Certification Team</i>
                
                </p>
                
                </body></html>
                    """
        msg = MIMEMultipart("alternative", None, [
            MIMEText(body), MIMEText(body, 'html')])
        msg['Subject'] = f"Confirmation of Post-Issuance Certification of {da_name}"
        msg['From'] = sender
        msg['To'] = recipient#", ".join(recipient)

        # attachment = open(filepath1, "rb")
        # p = MIMEBase('application', 'octet-stream')
        # p.set_payload((attachment).read())
        # encoders.encode_base64(p)
        # p.add_header('Content-Disposition',
        #              "attachment; filename= %s" % filename1)
        # msg.attach(p)

        attachment1 = open(filepath2, "rb")
        p1 = MIMEBase('application', 'octet-stream')
        p1.set_payload((attachment1).read())
        encoders.encode_base64(p1)
        p1.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename2)
        msg.attach(p1)

        attachment2 = open(filepath3, "rb")
        p2 = MIMEBase('application', 'octet-stream')
        p2.set_payload((attachment2).read())
        encoders.encode_base64(p2)
        p2.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename3)
        msg.attach(p2)

        attachment3 = open(filepath4, "rb")
        p3 = MIMEBase('application', 'octet-stream')
        p3.set_payload((attachment3).read())
        encoders.encode_base64(p3)
        p3.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename4)
        msg.attach(p3)

        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        server.login(sender, 'Cbigithub@i2R')
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
    except Exception as e:
        error = str(e)
        return {'error': error}, 409


def generate_certificate(instrument_type, issuing_entity_legal_name, approval_date, cert_id,cert_type):
    context1 = {
        'instrument_type': instrument_type.title(),
        'issuing_entity_legal_name': issuing_entity_legal_name.title(),
        'approval_date': approval_date
    }

    paths1 = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    doc_temp_paths1 = paths1+"/template/certificate.docx"
    doc1 = DocxTemplate(doc_temp_paths1)

    doc1.render(context1)
    doc_filename1 = "certificate_"+str(cert_id)+"_"+str(cert_type)+".docx"
    doc_gen_paths1 = paths1+'/template/'+doc_filename1
    doc1.save(doc_gen_paths1)

    os.system(
        f"/usr/bin/soffice --headless --convert-to pdf {doc_gen_paths1} --outdir /var/www/html/cbi-api/cbi_uploads")
    os.system(f"/bin/rm {doc_gen_paths1}")


def generate_approval_pre(cert_id, cert_type, approval_date, cp_name, legal_name_issuing_entity, cp_address, unique_name):
    context = {
        'approval_date': approval_date,
        'cp_name': cp_name.title(),
        'legal_name_issuing_entity': legal_name_issuing_entity.title(),
        'cp_address': cp_address.title(),
        'unique_name': unique_name.title()
    }

    paths = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    doc_temp_paths = paths + "/template/Climate Bonds_approving_Pre-Issuance_Certification_template.docx"
    doc = DocxTemplate(doc_temp_paths)

    doc.render(context)
    doc_filename = "approval_"+str(cert_id)+"_"+str(cert_type)+".docx"
    doc_gen_paths = paths+'/template/'+doc_filename
    doc.save(doc_gen_paths)

    os.system(
        f"/usr/bin/soffice --headless --convert-to pdf {doc_gen_paths} --outdir /var/www/html/cbi-api/cbi_uploads")
    os.system(f"/bin/rm {doc_gen_paths}")


def generate_approval_post(cert_id, cert_type, approval_date, cp_name, legal_name_issuing_entity, cp_address, unique_name):
    context = {
        'approval_date': approval_date,
        'cp_name': cp_name.title(),
        'legal_name_issuing_entity': legal_name_issuing_entity.title(),
        'cp_address': cp_address.title(),
        'unique_name': unique_name.title()
    }

    paths = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    doc_temp_paths = paths +"/template/Climate Bonds_approving_Post-Issuance_Certification_template.docx"
    doc = DocxTemplate(doc_temp_paths)

    doc.render(context)
    doc_filename = "approval_"+str(cert_id)+"_"+str(cert_type)+".docx"
    doc_gen_paths = paths+'/template/'+doc_filename
    doc.save(doc_gen_paths)

    os.system(
        f"/usr/bin/soffice --headless --convert-to pdf {doc_gen_paths} --outdir /var/www/html/cbi-api/cbi_uploads")
    os.system(f"/bin/rm {doc_gen_paths}")


