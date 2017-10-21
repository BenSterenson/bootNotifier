import socket
from time import gmtime, strftime
import smtplib
import traceback


class MailSender():
    PASSWORD = '*****'
    USER_NAME = '***@gmail.com'
    SERVER = 'smtp.gmail.com'
    MAIL_LIST = ['yaron.y@sckipio.com', 'asaf@sckipio.com', 'ronny@sckipio.com', 'ben.s@sckipio.com']

    def __init__(self):
        self.computer_name = socket.gethostname()
        self.boot_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.mail_list = self.MAIL_LIST
        self.msg = self.build_msg()

    def build_msg(self):
        return'{0} booted successfully {1}'.format(self.computer_name, self.boot_time)

    def send_mail(self):
        try:
            print 'Connecting to mail server'
            server = smtplib.SMTP(self.SERVER, 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.USER_NAME, self.PASSWORD)
            print 'Mail server Connection accepted'

            print 'Sending message...'
            server.sendmail(self.USER_NAME, self.mail_list, self.msg)

            print 'Mail Sent!'
            server.quit()

        except:
            print 'Error: Failed sending mail'
            print traceback.print_exc()

if __name__ == '__main__':
    mail = MailSender()
    mail.send_mail()
