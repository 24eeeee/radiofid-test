import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.utils import ExecutableUtil


class Notifier(ExecutableUtil):
    """
    DOCUMENTME
    """
    def __init__(self, cfg):
        super().__init__()
        self.config = cfg.get("mail-server")
        
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.notify(*args)
        
    def notify(self, mail: str, lst: dict[str, str]) -> None:
        """
        Отправка отвалидированного списка на почту.

        Args:
            mail: адрес электронной почты получателя.
            lst: список пар (слово, статус).
        """

        sender = self.config.get('user')

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Спасибо за прохождение опроса!"
        msg['From'] = sender
        msg['To'] = mail

        html = '<p>Спасибо за прохождение опроса!</p><p>Ваш ввод:</p>'
        html += '<table><tr><th>' + '</th><th>'.join(['Слово', 'Статус']) + '</th></tr>'
        for word, status in lst.items():
            html += '<tr><td>' + word + '</td><td>' + status + '</td></tr>'
        html += '</table>'

        payload = MIMEText(html, 'html')

        msg.attach(payload)

        s = smtplib.SMTP_SSL(self.config.get('host'), port=self.config.get('port', 587))
        s.ehlo()
        s.login(sender, self.config.get('pass'))
        s.sendmail(sender, mail, msg.as_string())
        s.quit()
