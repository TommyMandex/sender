import smtplib
import email.message
import tempmail
import tolist
import database
server = smtplib.SMTP('80.89.229.229:25')


def start_send():
    tolist.get_all_email()
    get_len_list = tolist.get_len_list()
    for i in range(get_len_list):
        msg = email.message.Message()
        msg['Subject'] = tempmail.subject
        msg['From'] = 'office@pring.fun'
        msg['To'] = tolist.all_mail[i]
        password = "irifeg84"
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(tempmail.email_content)
        #Server
        s = smtplib.SMTP('mail.teverise.com:25')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        #database and i
        database.addlog(msg['To'])
        i += 1

start_send()