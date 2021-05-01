from flask import Flask, request, jsonify, send_from_directory

import sys

import os

from cbi_modules.issuer import user_login, user_register, pre_certification, issuer_certification_dashboard, post_certification, all_certifications, id_generator,bond_redemption, forgot_password, signed_agreement, annual_report

from cbi_modules.reviewer import reviewer_dashboard, submitted_certification_queue, workboard, approve_certificate, approved_queue

from cbi_modules.admin import all_reports, reviewer_list, admin_dashboard, teams_and_roles, admin_user_management

from flask_cors import CORS

from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/cbi_uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cors = CORS(app)


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/cbi_uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cors = CORS(app)

psql = {
    "database": "cbidatabase",
    "user": "cbiuser",
    "password": "cbipass",
    "host": "143.110.213.22",
    "port": "5432"
}
@app.route("/api/register", methods=['POST','GET'])
def register():
    if request.method == 'POST':

        data = request.json

        cbi_register_response,resp = user_register.register(data,psql)

        return cbi_register_response,resp
    else:
        invite_token = request.headers.get('inviteToken')
        cbi_verify_token, resp = admin_user_management.verify_token(invite_token,psql)
        return cbi_verify_token, resp



@app.route("/api/login", methods=['POST'])
def login():
    
    data = request.json

    cbi_login_response,resp = user_login.login(data,psql)

    return cbi_login_response,resp


@app.route("/api/climateBondInformation", methods=['POST', 'GET'])
def climateBondInformation():

    if request.method == 'POST':
        data = request.json
        cid = data['certificationId']
        val = pre_certification.validate_certification(cid, data['certificationType'], psql)
        if val == 0:
            cbi_sone_response, resp = {"error": "certification doesnt exists"}, 401
        else:
            if data['certificationType'] == 'pre':
                cbi_sone_response, resp = pre_certification.step_one(data, psql)
            elif data['certificationType'] == 'post':
                cbi_sone_response, resp = post_certification.step_one(data, psql)
    else:
        user_email_address = request.headers.get('userEmail')
        certification_id = request.headers.get('certificationId')
        val = pre_certification.validate_certification(certification_id, request.headers.get('certificationType'),psql)
        if val == 0:
            cbi_sone_response, resp = {"error": "certification doesnt exists"}, 401
        else:
            if request.headers.get('certificationType') == 'pre':
                cbi_sone_response, resp = pre_certification.step_one_get(user_email_address, certification_id, psql)
            elif request.headers.get('certificationType') == 'post':
                cbi_sone_response, resp = post_certification.step_one_get(user_email_address, certification_id, psql)

    return cbi_sone_response,resp


@app.route("/api/climateBondInformationContd", methods=['POST', 'GET'])
def climateBondInformationContd():
    if request.method == 'POST':
        data = request.json
        cid = data['certificationId']
        val = pre_certification.validate_certification(cid, data['certificationType'], psql)
        if val == 0:
            cbi_stwo_response, resp = {
                "error": "certification doesnt exists"}, 401
        else:
            if data['certificationType'] == 'pre':
                cbi_stwo_response, resp = pre_certification.step_two(data, psql)
            elif data['certificationType'] == 'post':
                cbi_stwo_response, resp = post_certification.step_two(data, psql)
    else:
        user_email_address = request.headers.get('userEmail')
        certification_id = request.headers.get('certificationId')
        val = pre_certification.validate_certification(certification_id,request.headers.get('certificationType'),psql)
        if val == 0:
            cbi_stwo_response, resp = {
                "error": "certification doesnt exists"}, 401
        else:
            if request.headers.get('certificationType') == 'pre':
                cbi_stwo_response, resp = pre_certification.step_two_get(user_email_address, certification_id, psql)
            elif request.headers.get('certificationType') == 'post':
                cbi_stwo_response, resp = post_certification.step_two_get(user_email_address, certification_id, psql)

    return cbi_stwo_response,resp
    

@app.route("/api/certificateAgreement", methods=['POST', 'GET'])
def certificateAgreement():
    if request.method == 'POST':
        data = request.json
        cid = data['certificationId']
        val = pre_certification.validate_certification(cid, data['certificationType'], psql)
        if val == 0:
            cbi_sthree_response, resp = {"error": "certification doesnt exists"}, 401
        else:
            if data['certificationType'] == 'pre':
                cbi_sthree_response,resp = pre_certification.step_three(data, psql)
            elif data['certificationType'] == 'post':
                cbi_sthree_response,resp = post_certification.step_three(data, psql)
    else:
        user_email_address = request.headers.get('userEmail')
        certification_id = request.headers.get('certificationId')
        val = pre_certification.validate_certification(certification_id, request.headers.get('certificationType'),psql)
        if val == 0:
            cbi_sthree_response, resp = {"error": "certification doesnt exists"}, 401
        else:
            if request.headers.get('certificationType') == 'pre':
                cbi_sthree_response, resp = pre_certification.step_three_get(user_email_address, certification_id, psql)
            elif request.headers.get('certificationType') == 'post':
                cbi_sthree_response, resp = post_certification.step_three_get(user_email_address, certification_id, psql)

    return cbi_sthree_response,resp


@app.route("/api/submitApplication", methods=['POST'])
def submitApplication():
    data = request.json
    cid = data['certificationId']
    val = pre_certification.validate_certification(cid, data['certificationType'], psql)
    if val == 0:
        cbi_submit_response, resp = {"error": "certification doesnt exists"}, 401
    else:
        if data['certificationType'] == 'pre':
            cbi_submit_response, resp = pre_certification.submit(data, psql)
        elif data['certificationType'] == 'post':
            cbi_submit_response, resp = post_certification.submit(data, psql)

    return cbi_submit_response, resp


@app.route("/api/issuerDashboard", methods=['POST', 'GET'])
def issuerDashboard():

    data = request.json

    issuer_certification_dashboard_response, resp = issuer_certification_dashboard.dashboard(data, psql)

    return issuer_certification_dashboard_response, resp


@app.route("/api/assuranceReport", methods=['POST', 'GET'])
def assuranceReport():
    if request.method == 'POST':
        certification_id = request.form.get('certificationId')
        user_email_address = request.form.get('userEmail')
        certification_type = request.form.get('certificationType')
        val = pre_certification.validate_certification(
            certification_id, certification_type,psql)
        if val == 0:
            cbi_files_response, resp = {"error": "certification doesnt exists"}, 401
            return cbi_files_response, resp
        else:
            if certification_type == 'pre':
                try:
                    if 'caAssuranceReport' in request.files:
                        f = request.files['caAssuranceReport']
                        fname = str(certification_id)+'_pre_caAssuranceReport.pdf'
                        file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_1)
                    else:
                        file_1 =""

                    if 'gbAssuranceReport' in request.files:
                        f = request.files['gbAssuranceReport']
                        fname = str(certification_id)+'_pre_gbAssuranceReport.pdf'
                        file_2 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_2)
                    else:
                        file_2 =""

                    cbi_files_response, resp = pre_certification.step_four(certification_id, user_email_address, file_1, file_2, psql)

                    return cbi_files_response, resp
                except Exception as e:
                    error = str(e)
                    msg = error
                    return {'error': msg}, 404
            elif certification_type == 'post':
                try:
                    if 'caAssuranceReport' in request.files:
                        f = request.files['caAssuranceReport']
                        fname = str(certification_id)+'_post_caAssuranceReport.pdf'
                        file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_1)
                    else:
                        file_1 =""

                    if 'gbAssuranceReport' in request.files:
                        f = request.files['gbAssuranceReport']
                        fname = str(certification_id)+'_post_gbAssuranceReport.pdf'
                        file_2 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_2)
                    else:
                        file_2 =""

                    cbi_files_response, resp = post_certification.step_four(certification_id, user_email_address, file_1, file_2, psql)

                    return cbi_files_response, resp
                except Exception as e:
                    error = str(e)
                    msg = error
                    return {'error': msg}, 404
    else:
        user_email_address = request.headers.get('userEmail')
        certification_id = request.headers.get('certificationId')
        val = pre_certification.validate_certification(certification_id, request.headers.get('certificationType'),psql)
        if val == 0:
            cbi_files_response, resp = {"error": "certification doesnt exists"}, 401
        else:
            if request.headers.get('certificationType') == 'pre':
                cbi_files_response, resp = pre_certification.step_four_get(user_email_address, certification_id, psql)
            elif request.headers.get('certificationType') == 'post':
                cbi_files_response, resp = post_certification.step_four_get(user_email_address, certification_id, psql)

        return cbi_files_response, resp


@app.route("/file/<files>", methods=['POST', 'GET'])
def files(files):
    return send_from_directory(directory="/var/www/html/cbi-api/cbi_uploads/", filename=files)


@app.route("/api/getCertifications", methods=['GET'])
def getCertifications():
    user_email_address = request.headers.get('userEmail')
    cbi_all_cert_response, resp = all_certifications.get_certifications(user_email_address, psql)

    return cbi_all_cert_response, resp


@app.route("/api/getPreCertifications", methods=['GET'])
def getPreCertifications():
    user_email_address = request.headers.get('userEmail')
    cbi_pre_cert_response, resp = all_certifications.pre_certifications(
        user_email_address, psql)

    return cbi_pre_cert_response, resp


@app.route("/api/getPostCertifications", methods=['GET'])
def getPostCertifications():
    user_email_address = request.headers.get('userEmail')
    cbi_post_cert_response, resp = all_certifications.post_certifications(
        user_email_address, psql)

    return cbi_post_cert_response, resp

@app.route("/api/generateCertificationId", methods=['GET'])
def generateCertificationId():
    
    user_email_address = request.headers.get('userEmail')
    certification_type = request.headers.get('certificationType')
    instrument_type = request.headers.get('instrumentType')

    if certification_type == 'pre':
        cbi_stwo_response, resp = id_generator.pre_certification_id(user_email_address, instrument_type, psql)
    elif certification_type == 'post':
        certification_id = request.headers.get('certificationId')
        cbi_stwo_response, resp = id_generator.post_certification_id(user_email_address, instrument_type, certification_id, psql)

    return cbi_stwo_response, resp

@app.route("/api/bondRedemption", methods=['POST'])
def bondRedemption():
    certification_id = request.form.get('certificationId')
    user_email_address = request.form.get('userEmail')
    val = pre_certification.validate_certification(certification_id,"br",psql)
    if val == 0:
        cbi_files_response, resp = {"error": "post certification is not completed"}, 401
        return cbi_files_response, resp
    else:
        try:
            if 'file1' in request.files:
                f = request.files['file1']
                file_name1 = request.form.get('fileName1')
                fname = str(certification_id)+f'_bond_redemption_file1_{file_name1}.pdf'
                file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                f.save(file_1)
            else:
                file_1 =""

            if 'file2' in request.files:
                f = request.files['file2']
                file_name2 = request.form.get('fileName2')
                fname = str(certification_id)+f'_bond_redemption_file2_{file_name2}.pdf'
                file_2 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                f.save(file_2)
            else:
                file_2 =""

            if 'file3' in request.files:
                f = request.files['file3']
                file_name3 = request.form.get('fileName3')
                fname = str(certification_id)+f'_bond_redemption_file3_{file_name3}.pdf'
                file_3 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                f.save(file_3)
            else:
                file_3 = ""

            if 'file4' in request.files:
                f = request.files['file4']
                file_name4 = request.form.get('fileName4')
                fname = str(certification_id)+f'_bond_redemption_file4_{file_name4}.pdf'
                file_4 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                f.save(file_4)
            else:
                file_4 = ""

            if 'file5' in request.files:
                f = request.files['file5']
                file_name5 = request.form.get('fileName5')
                fname = str(certification_id)+F'_bond_redemption_file5_{file_name5}.pdf'
                file_5 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                f.save(file_5)
            else:
                file_5 = ""

            cbi_files_response, resp = bond_redemption.redeem(certification_id, user_email_address, file_1, file_2, file_3, file_4, file_5, psql)

            return cbi_files_response, resp
        except Exception as e:
            error = str(e)
            msg = error
            return {'error': msg}, 404


@app.route("/api/forgotPassword", methods=['POST'])
def forgotPassword():
    data = request.json
    user_email_address = data['userEmail']
    cbi_forgot_password_response, resp = forgot_password.reset(user_email_address, psql)

    return cbi_forgot_password_response, resp
    

@app.route("/api/signedCertificationAgreement", methods=['POST', 'GET'])
def signedCertificationAgreement():
    if request.method == 'POST':
        certification_id = request.form.get('certificationId')
        user_email_address = request.form.get('userEmail')
        user_role = request.form.get('userRole')
        val = pre_certification.validate_certification(certification_id, "pre", psql)
        if val == 0:
            cbi_signed_agreement, resp = {"error": "certification doesnt exists"}, 401
            return cbi_signed_agreement, resp
        else:
            if user_role == 'programmaticIssuer':
                try:
                    if 'signedCertificationAgreement' in request.files:
                        f = request.files['signedCertificationAgreement']
                        fname = str(certification_id) + '_programmatic_signedCertificationAgreement.pdf'
                        file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_1)
                    else:
                        file_1 = ""

                    cbi_signed_agreement, resp = signed_agreement.programmatic_signed_doc(certification_id, user_email_address, file_1, psql)

                    return cbi_signed_agreement, resp
                except Exception as e:
                    error = str(e)
                    msg = error
                    return {'error': msg}, 404
            elif user_role == 'singleIssuer':
                try:
                    if 'signedCertificationAgreement' in request.files:
                        f = request.files['signedCertificationAgreement']
                        fname = str(certification_id) + '_single_signedCertificationAgreement.pdf'
                        file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_1)
                    else:
                        file_1 = ""

                    cbi_signed_agreement, resp = signed_agreement.single_signed_doc(certification_id, user_email_address, file_1, psql)

                    return cbi_signed_agreement, resp
                except Exception as e:
                    error = str(e)
                    msg = error
                    return {'error': msg}, 404
            elif user_role == 'verifier':
                try:
                    if 'signedCertificationAgreement' in request.files:
                        f = request.files['signedCertificationAgreement']
                        fname = str(certification_id) + '_verifier_signedCertificationAgreement.pdf'
                        file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                        f.save(file_1)
                    else:
                        file_1 = ""

                    cbi_signed_agreement, resp = signed_agreement.verifier_signed_doc(certification_id, user_email_address, file_1, psql)

                    return cbi_signed_agreement, resp
                except Exception as e:
                    error = str(e)
                    msg = error
                    return {'error': msg}, 404
    else:
        user_email_address = request.headers.get('userEmail')
        certification_id = request.headers.get('certificationId')
        val = pre_certification.validate_certification(certification_id, "pre", psql)
        if val == 0:
            cbi_signed_agreement, resp = {"error": "certification doesnt exists"}, 401
        else:
            if request.headers.get('userRole') == 'programmaticIssuer':
                cbi_signed_agreement, resp = signed_agreement.programmatic_signed_doc_get(certification_id,user_email_address, psql)
            elif request.headers.get('userRole') == 'singleIssuer':
                cbi_signed_agreement, resp = signed_agreement.single_signed_doc_get(certification_id, user_email_address,psql)
            elif request.headers.get('userRole') == 'verifier':
                cbi_signed_agreement, resp = signed_agreement.verifier_signed_doc_get(certification_id, user_email_address,psql)

        return cbi_signed_agreement, resp


@app.route("/api/reviewerDashboard", methods=['POST'])
def reviewerDashboard():
    data = request.json
    user_email_address = data['userEmail']
    filter_date = data['filterBy']
    if filter_date =='':
        date_value = ''
    else:
        date_value = f"and application_date >= '{filter_date}' "
    
    reviewer_dashboard_response, resp = reviewer_dashboard.dashboard(user_email_address, filter_date, date_value, psql)


    return reviewer_dashboard_response, resp


@app.route("/api/assignCertification", methods=['POST', 'GET'])
def assignCertification():
    if request.method == 'POST':
        data = request.json
        cid = data['certificationId']
        user_email_address = data['userEmail']
        cert_type = data['certificationType']
        val = submitted_certification_queue.validate_reviewer(user_email_address, psql)
        if val != 0:
            update_val = submitted_certification_queue.assign_reviewer(user_email_address, cert_type, cid, psql)
            if update_val != 0:
                cbi_assignment_queue, resp = submitted_certification_queue.unassigned_queue(user_email_address, psql)
                return cbi_assignment_queue, resp
            else:
                return {'error': 'cant assign User'}, 403
        else:
            return {'error': 'Invalid User'}, 401

    else:
        user_email_address = request.headers.get('userEmail')
        val = submitted_certification_queue.validate_reviewer(user_email_address, psql)
        if val != 0:
            cbi_assignment_queue, resp = submitted_certification_queue.unassigned_queue(user_email_address, psql)
            return cbi_assignment_queue, resp
        else:
            return {'error': 'Invalid User'}, 401


@app.route("/api/workBoard", methods=['POST', 'GET'])
def workBoard():
    if request.method == 'POST':
        data = request.json
        user_email_address = data['userEmail']
        notes = data['workSpace']
        val = submitted_certification_queue.validate_reviewer(
            user_email_address, psql)
        if val != 0:
            update_val = workboard.reviewer_workspace(user_email_address, notes, psql)
            if update_val != 0:
                cbi_assignment_queue, resp = workboard.assigned_queue(user_email_address, psql)
                return cbi_assignment_queue, resp
            else:
                return {'error': 'cant save Notes to workspace'}, 403
        else:
            return {'error': 'Invalid User'}, 401

    else:
        user_email_address = request.headers.get('userEmail')
        val = submitted_certification_queue.validate_reviewer(
            user_email_address, psql)
        if val != 0:
            cbi_assignment_queue, resp = workboard.assigned_queue(user_email_address, psql)
            return cbi_assignment_queue, resp
        else:
            return {'error': 'Invalid User'}, 401


@app.route("/api/approveCertification", methods=['POST'])
def approveCertification():
    if request.method == 'POST':
        data = request.json
        user_email_address = data['userEmail']
        cert_type = data['certificationType']
        cert_id = data['certificationId']
        val = submitted_certification_queue.validate_reviewer(user_email_address, psql)
        if val != 0:
            cbi_assignment_queue, resp = approve_certificate.cert(cert_type,cert_id,psql)
            return cbi_assignment_queue, resp
        else:
            return {'error': 'Invalid User'}, 401


@app.route("/api/getApprovedCertifications", methods=['GET'])
def getApprovedCertifications():
    user_email_address = request.headers.get('userEmail')
    val = submitted_certification_queue.validate_reviewer(
        user_email_address, psql)
    if val != 0:
        cbi_assignment_queue, resp = approved_queue.assigned_queue(
            user_email_address, psql)
        return cbi_assignment_queue, resp
    else:
        return {'error': 'Invalid User'}, 401


@app.route("/api/getAdminReports", methods=['GET'])
def getAdminReports():
    user_email_address = request.headers.get('userEmail')
    val = all_reports.validate_admin(user_email_address, psql)
    if val != 0:
        cbi_all_cert_response, resp = all_reports.get_certifications(psql)
        return cbi_all_cert_response, resp
    else:
        return {'error': 'Invalid User'}, 401
    

@app.route("/api/adminCertificationQueue", methods=['POST', 'GET'])
def adminCertificationQueue():
    if request.method == 'POST':
        data = request.json
        cid = data['certificationId']
        user_email_address = data['userEmail']
        reviewer_email_address = data['reviewerEmail']
        cert_type = data['certificationType']
        val = all_reports.validate_admin(user_email_address, psql)
        if val != 0:
            update_val = submitted_certification_queue.assign_reviewer(reviewer_email_address, cert_type, cid, psql)
            if update_val != 0:
                cbi_assignment_queue, resp = submitted_certification_queue.unassigned_queue(user_email_address, psql)
                reviewer_emails = reviewer_list.rev_email(psql)
                cbi_assignment_queue = {"data": cbi_assignment_queue['data'], "reviewerEmail": reviewer_emails['reviewerEmail']}
                return cbi_assignment_queue, resp
            else:
                return {'error': 'cant assign User'}, 403
        else:
            return {'error': 'Invalid User'}, 401

    else:
        user_email_address = request.headers.get('userEmail')
        val = all_reports.validate_admin(user_email_address, psql)
        if val != 0:
            cbi_assignment_queue, resp = submitted_certification_queue.unassigned_queue(user_email_address, psql)
            reviewer_emails = reviewer_list.rev_email(psql)
            cbi_assignment_queue = {"data": cbi_assignment_queue['data'], "reviewerEmail": reviewer_emails['reviewerEmail']}

            return cbi_assignment_queue, resp
        else:
            return {'error': 'Invalid User'}, 401


@app.route("/api/adminDashboard", methods=['POST'])
def adminDashboard():
    data = request.json
    user_email_address = data['userEmail']
    val = all_reports.validate_admin(user_email_address, psql)
    if val != 0:
        cbi_admin_dashboard, resp = admin_dashboard.dashboard(psql)

        return cbi_admin_dashboard, resp
    else:
        return {'error': 'Invalid User'}, 401

@app.route("/api/userManagement", methods=['GET'])
def userManagement():
    user_email_address = request.headers.get('userEmail')
    val = all_reports.validate_admin(user_email_address, psql)
    if val != 0:
        cbi_teams_and_roles, resp = teams_and_roles.stats(user_email_address,psql)
        return cbi_teams_and_roles, resp
    else:
        return {'error': 'Invalid User'}, 401


@app.route("/api/addUser", methods=['POST'])
def addUser():
    data = request.json
    admin_email_address = data['adminEmail']
    user_email_address = data['userEmail']
    val = all_reports.validate_admin(admin_email_address, psql)
    if val != 0:
        cbi_register_response, resp = user_register.management(data, psql)
        if resp == 200:
            cbi_forgot_password_response, resp1 = admin_user_management.reset(user_email_address, psql)
            if resp1 == 200:
                cbi_teams_and_roles, resp = teams_and_roles.stats(admin_email_address,psql)
                return cbi_teams_and_roles, resp
            else:
                return cbi_forgot_password_response, resp1
        else:
            return cbi_register_response, resp
    else:
        return {'error': 'Invalid User'}, 401


@app.route("/api/updateUser", methods=['POST'])
def updateUser():
    data = request.json
    admin_email_address = data['adminEmail']
    val = all_reports.validate_admin(admin_email_address, psql)
    if val != 0:
        cbi_register_response, resp = admin_user_management.update(data, psql)
        if resp == 200:
            cbi_teams_and_roles, resp = teams_and_roles.stats(admin_email_address,psql)
            return cbi_teams_and_roles, resp
        else:
            return cbi_register_response, resp
    else:
        return {'error': 'Invalid User'}, 401


@app.route("/api/removeUser", methods=['POST'])
def removeUser():
    data = request.json
    admin_email_address = data['adminEmail']
    user_email_address = data['userEmail']
    val = all_reports.validate_admin(admin_email_address, psql)
    if val != 0:
        cbi_register_response, resp = admin_user_management.remove(user_email_address, psql)
        if resp == 200:
            cbi_teams_and_roles, resp = teams_and_roles.stats(admin_email_address,psql)
            return cbi_teams_and_roles, resp
        else:
            return cbi_register_response, resp
    else:
        return {'error': 'Invalid User'}, 401


@app.route("/api/inviteIssuer", methods=['POST'])
def inviteIssuer():
    data = request.json
    admin_email_address = data['adminEmail']
    user_email_address = data['userEmail']
    val = all_reports.validate_admin(admin_email_address, psql)
    if val != 0:
        cbi_register_response, resp = admin_user_management.invite(user_email_address, psql)
        if resp == 200:
            cbi_teams_and_roles, resp = teams_and_roles.stats(admin_email_address,psql)
            return cbi_teams_and_roles, resp
        else:
            return cbi_register_response, resp
    else:
        return {'error': 'Invalid User'}, 401

@app.route("/api/submitAnnualReport", methods=['POST'])
def submitAnnualReport():
    certification_id = request.form.get('certificationId')
    certification_type = request.form.get('certificationType')
    try:
        if 'annualReport' in request.files:
            f = request.files['annualReport']
            fname = str(certification_id)+f'_{certification_type}_annual_report.pdf'
            file_1 = os.path.join(app.config['UPLOAD_FOLDER'], fname)
            f.save(file_1)
        else:
            file_1 =""

        cbi_anual_response, resp = annual_report.upload_report(certification_id, certification_type, file_1, fname, psql)

        return cbi_anual_response, resp
    except Exception as e:
        error = str(e)
        msg = error
        return {'error': msg}, 404


if __name__ == '__main__':
    # app.debug = True
    app.config['DEBUG'] = True
    app.run()
