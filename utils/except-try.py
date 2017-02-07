import logging
import logging.handlers
import smtplib

s = smtplib.SMTP_SSL("smtp.gmail.com", 587)
s.login('xyz@gmail.com', 'myPassword')
s.starttls()

logger = logging.getLogger()
logger.addHandler(s)

try:
	a = 2/0
except Exception as e:
  logger.exception('Unhandled Exception')
  s.sendmail('xyz@gmail.com', 'xyz@gmail.com', 'Hi')
  s.close()