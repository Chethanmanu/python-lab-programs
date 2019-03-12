#sending mail using python



import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='chethanmanu7777@gmail.com'
receiver='chandanabhat163@gmail.com'
msg="hii chandanna"
s.login(sender,'7760651660')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()