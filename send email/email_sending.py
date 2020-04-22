import smtplib


def send_email(email, password, recipients=None, message='Empty Message'):
	"""
	:param email: your email
	:param password: your email's password
	:param recipients: to whom you want to send email
	:param message:
	:return:
	"""
	if recipients is None:
		recipients = []
	try:
		server = smtplib.SMTP_SSL("smtp.gmail.com", port)
		server.login(email, password)
		server.sendmail(email, recipients, message)
		server.close()
		print('Successfully sent the email')
	except Exception as e:
		print("Following error occurred while sending email\n{}".format(e))
		return


# set parameters
your_email = 'email@gmail.com'
your_password = '********'
port = 465
to_email = ['recipient1@gmail.com', 'recipient2@gmail.com']
subject = 'Python Email Code Testing'
content = """
Hi,

This is Danish Javed. Sending you email from new account to test python automatic email sending code.

Regards,
Danish Javed
"""
your_message = 'Subject: {}\n\n{}'.format(subject, content)

send_email(email=your_email, password=your_password, recipients=to_email, message=your_message)
