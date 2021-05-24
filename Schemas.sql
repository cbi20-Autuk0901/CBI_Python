-- certification Queue
CREATE TABLE CBI_Certification_Queue (
	id serial PRIMARY KEY,
	certification_id VARCHAR(50),
    certification_type VARCHAR(50),
    certification_status VARCHAR(50),
    reviewer VARCHAR (255),
    application_date TIMESTAMP,
    assigned_date TIMESTAMP,
    approved_date TIMESTAMP,
    user_company VARCHAR(100),
    certification_company VARCHAR(100),
    instrument_type VARCHAR(20),
    underwriter VARCHAR
);


-- pre-issuance
CREATE TABLE cbi_pre_issuance_certification (
	id serial PRIMARY KEY,
	certification_id VARCHAR(50) UNIQUE,
	user_email_address VARCHAR (255),
	certification_status VARCHAR (20),
	instrument_type VARCHAR (20),
	da_name VARCHAR (50),
	da_issuance_country VARCHAR (50),
	da_cusip VARCHAR (50),
	da_isin VARCHAR (50),
	da_local_currency_lc VARCHAR (50),
	da_amount_issued_lc VARCHAR (50),
	da_coupon VARCHAR (50),
	da_underwriter VARCHAR,
	da_issue_date TIMESTAMP,
	da_maturity_date TIMESTAMP,
	da_instrument_type VARCHAR (50),
    d_renewable_energy VARCHAR,
	d_renewable_energy_text VARCHAR,
	ps_financing_asset VARCHAR (50),
	ps_proceeds_allocation VARCHAR (50),
	pe_portfolio_approach VARCHAR (50),
	pe_assessment_procedure VARCHAR (200),
	pm_proceed_type VARCHAR (50),
	pm_proceed_detail VARCHAR (200),
	pm_proceed_timing VARCHAR (20),
	pm_proceed_use VARCHAR (200),
	ar_report_interval VARCHAR (50),
	ar_report_format VARCHAR (50),
	ar_report_access VARCHAR (50),
	ar_report_link VARCHAR(200),
	ar_report_breakdown VARCHAR (200),
	ir_report_interval VARCHAR (50),
	ir_report_format VARCHAR(50),
	ir_report_access VARCHAR (50),
	ir_report_link VARCHAR (200),
	ir_report_indicators VARCHAR (50),
	ci_address_head_office VARCHAR (300),
	ci_vat_number VARCHAR (50),
	ci_business_reg_number VARCHAR (50),
	cp_name VARCHAR (50),
	cp_position VARCHAR (50),
	cp_company VARCHAR (50),
	cp_contact_number VARCHAR (50),
	id_name VARCHAR (50),
	ca_application_date TIMESTAMP,
	ca_legal_name_issuing_entity VARCHAR (50),
	ca_unique_name_debt_instruments VARCHAR (50),
	ca_address VARCHAR(300),
	ca_email_address VARCHAR (255),
	ca_contact_person VARCHAR (50),
	ca_signature VARCHAR (50),
	single_issuer_agreement VARCHAR (200),
	verifier_agreement VARCHAR (1200)
);


-- post-issuance
CREATE TABLE cbi_post_issuance_certification (
	id serial PRIMARY KEY,
	certification_id VARCHAR(50) UNIQUE,
	user_email_address VARCHAR (255),
	certification_status VARCHAR (20),
	instrument_type VARCHAR (20),
	da_name VARCHAR (50),
	da_issuance_country VARCHAR (50),
	da_cusip VARCHAR (50),
	da_isin VARCHAR (50),
	da_local_currency_lc VARCHAR (50),
	da_amount_issued_lc VARCHAR (50),
	da_coupon VARCHAR (50),
	da_underwriter VARCHAR,
	da_issue_date TIMESTAMP,
	da_maturity_date TIMESTAMP,
	da_instrument_type VARCHAR (50),
	ps_financing_asset VARCHAR (50),
	ps_proceeds_allocation VARCHAR (50),
	pe_portfolio_approach VARCHAR (50),
	pe_assessment_procedure VARCHAR (200),
	pm_proceed_type VARCHAR (50),
	pm_proceed_detail VARCHAR (200),
	pm_proceed_timing VARCHAR (20),
	pm_proceed_use VARCHAR (200),
	ar_report_interval VARCHAR (50),
	ar_report_format VARCHAR (50),
	ar_report_access VARCHAR (50),
	ar_report_link VARCHAR(200),
	ar_report_breakdown VARCHAR (200),
	ir_report_interval VARCHAR (50),
	ir_report_format VARCHAR(50),
	ir_report_access VARCHAR (50),
	ir_report_link VARCHAR (200),
	ir_report_indicators VARCHAR (50),
    d_renewable_energy VARCHAR,
	d_renewable_energy_text VARCHAR,
	ci_address_head_office VARCHAR (300),
	ci_vat_number VARCHAR (50),
	ci_business_reg_number VARCHAR (50),
	cp_name VARCHAR (50),
	cp_position VARCHAR (50),
	cp_company VARCHAR (50),
	cp_contact_number VARCHAR (50),
	id_name VARCHAR (50),
	ca_application_date TIMESTAMP,
	ca_legal_name_issuing_entity VARCHAR (50),
	ca_unique_name_debt_instruments VARCHAR (50),
	ca_address VARCHAR(300),
	ca_email_address VARCHAR (255),
	ca_contact_person VARCHAR (50),
	ca_signature VARCHAR (50),
	single_issuer_agreement VARCHAR (200),
	verifier_agreement VARCHAR (1200),
	FOREIGN KEY(certification_id) REFERENCES cbi_pre_issuance_certification(certification_id)
);

-- bond-redemption
CREATE TABLE cbi_bond_redemption (
	id serial PRIMARY KEY,
	certification_id VARCHAR(50) UNIQUE,
	user_email_address VARCHAR (255),
	certification_status VARCHAR (20),
	file1 VARCHAR (200),
	file2 VARCHAR (200),
	file3 VARCHAR (200),
	file4 VARCHAR (200),
	file5 VARCHAR (200),
	application_date TIMESTAMP,
	FOREIGN KEY(certification_id) REFERENCES cbi_post_issuance_certification(certification_id)
);


--  issuer invitation  table
CREATE TABLE cbi_issuer_invitation (
	id serial PRIMARY KEY,
    user_email_address VARCHAR (255),
    invite_token VARCHAR(20),
    invite_time TIMESTAMP
);


--  reviewer workspace
CREATE TABLE cbi_reviewer_workspace(
	id serial PRIMARY KEY,
	user_email_address VARCHAR (255),
	work_notes VARCHAR,
    last_modified_date TIMESTAMP
);

-- programmatic issuer
CREATE TABLE cbi_programmatic_signed_agreement (
	id serial PRIMARY KEY,
	invoice_company_name VARCHAR (50),
	user_email_address VARCHAR (255),
	signed_agreement VARCHAR (200),
	application_date TIMESTAMP
);

-- single issuer
CREATE TABLE cbi_single_signed_agreement (
	id serial PRIMARY KEY,
	certification_id VARCHAR(50) UNIQUE,
	user_email_address VARCHAR (255),
	signed_agreement VARCHAR (200),       
	application_date TIMESTAMP
	FOREIGN KEY(certification_id) REFERENCES cbi_pre_issuance_certification(certification_id)
);


-- User
CREATE TABLE CBI_User (
	user_id serial PRIMARY KEY,
	user_first_name VARCHAR ( 50 ) NOT NULL,
	user_last_name VARCHAR (50) NOT NULL,
	user_company VARCHAR (50) NOT NULL,
	user_email_address VARCHAR ( 255 ) UNIQUE NOT NULL,
	user_password VARCHAR ( 100 ) NOT NULL,
	user_category VARCHAR (20) NOT NULL,
	user_location VARCHAR (100) NOT NULL,
	invoice_company_name VARCHAR (50) NOT NULL,
	invoice_registration_number VARCHAR (50) NOT NULL,
	invoice_billing_address VARCHAR (100) NOT NULL,
	invoice_email_address VARCHAR ( 255 ) NOT NULL,
	invoice_phone_number VARCHAR (50) NOT NULL,
	user_job_title VARCHAR (50)
);


-- Annual reports
CREATE TABLE CBI_Annual_Reports (
	id serial PRIMARY KEY,
	certification_id VARCHAR(50),
    files VARCHAR (200)
);