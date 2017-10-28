import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.starttls()
smtp_obj.login('nat.tiutiunnyk@gmail.com', 'natalka2411')
smtp_obj.sendmail(from_addr='nat.tiutiunnyk@gmail.com', to_addrs='nat.tiutiunnyk@ukr.net', msg='First turn')
smtp_obj.quit()