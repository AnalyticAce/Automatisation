from email.mime.application import MIMEApplication
from secret import info
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime

class info:
    email_sender = "test@gmail.com"
    email_receiver = "dosseh@gmail.com"
    passwd = "passwd"
    key_path = "path"
    project_id = 'projectid'

def send_email(subject, body, file_path=None):
    em = EmailMessage()
    em["From"] = info.email_sender
    em["To"] = info.email_receiver
    em["Subject"] = subject

    em.set_content(body)

    html_body = f"""
    <html>
    <body>
        <p style="font-size: 16px; color: #34495e;">Salut 👋,</p>
        <p style="font-size: 16px; color: #34495e;">{body}</p>
        <p style="font-size: 16px; color: #34495e;">Cordialement,</p>
        <p style="font-size: 16px; color: #34495e;"><strong>Votre script Python</strong> 🚀</p>
    </body>
    </html>
    """
    em.add_alternative(html_body, subtype='html')
  
    if file_path is not None:
      with open(file_path, "rb") as file:
          file_data = file.read()
          file_name = file_path.split("/")[-1]
          em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(info.email_sender, info.passwd)
        smtp.sendmail(info.email_sender, info.email_receiver, em.as_string())


file_path = "dataframe.xlsx"
subject = "🔔 Alerte de mise à jour des jeu de données Transport 🔔"
header = "📊 Statut de mise à jour des jeu de données Transport 📈"
body = f"""
En date du {datetime.now()}, il semble que certains jeux de données ou tables n'ont pas été mis à jour au cours des dernières 24 heures. Veuillez vérifier le fichier joint pour plus de détails.
"""
send_email(subject, body, file_path)
