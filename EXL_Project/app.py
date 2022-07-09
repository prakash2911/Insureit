from flask import Flask, redirect,request,render_template
from pip import main
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='template')
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'quizwebsiteadp@gmail.com'
app.config['MAIL_PASSWORD'] = 'fsjhfqzqkplqtzlc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/mail',methods=['post'])
def send_mail():
    name = request.form['name_of_user']
    email = request.form['email']
    description= request.form['message']
    service = request.form['service']
    if email and name and description:
        msg = Message(
            subject=service,
            sender='quizwebsiteadp@gmail.com',
            recipients=['quizwebsiteadp@gmail.com']
        )
        # msg.add_recipient(email)
        msg.body=description
        mail.send(msg)
    return redirect('/contact')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():  
    return render_template('contact.html')

if __name__== "__main__":
    app.run(debug=True)