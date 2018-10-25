import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/ariza/Desktop/LineaBase/'
pngpath = '/home/ariza/Desktop/LineaBase/'
width = '500'
height = '200'
mailsender = "@gmail.com"
mailreceip = "@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = ''

def send_alert_attached(base, subject):
    """ Will send e-mail, attaching png
    files in the flist.
    """

    imagen =base+'.png'
    fname = base + '.rrd'
    objetoaEnviar =pngpath + imagen
    print(objetoaEnviar)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(objetoaEnviar, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)
    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()

