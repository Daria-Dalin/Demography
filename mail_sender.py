import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import schedule
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

def send_mail(email, subject, text):

    """
    Функция отправки сообщения
    email
    subject
    text
    return non
    """
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    addr_from = os.getenv('FROM')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')

#формируем сообщение
    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))

#подключаемся к серверу
    server = smtplib.SMTP_SSL(host, int(port))
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()
    return True

message = """
это проверка отправки почты моим скриптом"""

mail_list = ['a@b.ru', 'b@c.ru']

count=0 #глобальный счетчик писем

def mail_task():
    global count
    send_mail(mail_list[count], 'проверка', message)
    count += 1

while count < len(mail_list):
    schedule.every(2).seconds.do(mail_task)
    time.sleep(1) # если нужна допзадержка

print('Рассылка завершена')
