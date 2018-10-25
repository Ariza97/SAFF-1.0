import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/stefan/Desktop/Oblivion/'
pngpath = '/home/stefan/Desktop/Oblivion/'
fname = 'netP.rrd'
width = '500'
height = '200'
mailsender = "stefan170992@gmail.com"
mailreceip = "stefan170992@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'FerStefan10'

def send_alert_attached(subject, archivo):
    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    path = pngpath + archivo
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(path, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()

