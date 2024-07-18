from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject='email_subject', 
                  sender='your_email@gmail.com', 
                  recipients=['recipients_email'], 
                  cc=['email_you_want_to_cc'])

    msg.html = """

    email body
    <img src="cid:screenshot"> #Position where you want the image to be in the email
    
    """

    # Attach Image
    with open(r'C:\Users\image_path\image.jpg', 'rb') as f:
        img_data = f.read()
        msg.attach('image.jpg', 'image/jpeg', img_data, headers={'Content-ID': '<image>'})

    # Attach PDF
    with open(r'C:\Users\pdf_path\your_pdf.pdf', 'rb') as f:
        pdf_data = f.read()
        msg.attach('your_pdf.pdf', 'application/pdf', pdf_data)

    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)
