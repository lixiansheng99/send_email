import smtplib
from email.header import Header
from email.mime.text import MIMEText

class send_email():
    #参数含义：发信人用户名，密码，接收人账户，主题，正文
    def __init__(self,user,password,receiver,project,countent):
        mailhost = 'smtp.qq.com'
        qqmail = smtplib.SMTP()
        qqmail.connect(mailhost,25)

        qqmail.login(user,password)

        message = MIMEText(countent,'plain','utf-8')
        message['Subject'] = Header(project,'utf-8')
        try:
            qqmail.sendmail(user,receiver,message.as_string())
            print('邮件发送成功')
        except:
            print('邮件放松失败')
        qqmail.quit()

