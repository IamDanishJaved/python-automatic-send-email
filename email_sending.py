import smtplib, ssl

def SendEmail(email, password , recipients=[], message='Empty Message'):
	try:
		server = smtplib.SMTP_SSL("smtp.gmail.com", port)
		server.login(email, password)
		server.sendmail(email, recipients, message)
		server.close()
		print('Successfully sent the email')
	except Exception as e:
		raise
		print("Following error occured while sending email\n{}".format(e))


# set parameters
email = 'email@gmail.com'
password = '********'
port = 465
to_email = ['recipient1@gmail.com', 'recipient2@gmail.com']
subject = 'Python Email Code Testing'
content = """
Hi,

This is Danish Javed. Sending you email from new account to test python automatic email sending code.

Regards,
Danish Javed
"""
message = 'Subject: {}\n\n{}'.format(subject, content)

SendEmail(email=email, password=password, recipients=to_email, message=content)
