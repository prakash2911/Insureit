import email
from flask import Flask, redirect,request,render_template
from pip import main
from flask_mail import Mail, Message
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')
model = pickle.load(open('C:/Users/praka/Documents/GitHub/Insureit/EXL_Project/model.pkl', 'rb'))
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'quizwebsiteadp@gmail.com'
app.config['MAIL_PASSWORD'] = 'vfcjqwmfonmorbjs'
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
            recipients=[email]
        )
        msg.add_recipient(email)
        msg.body=f'''Service : {service} name : {name} Discription : {description}'''
        mail.send(msg)
    return redirect('/contact')

@app.route('/chatbot', methods=['post'])
def checking():
    age = request.form.get('Age')
    sex = request.form.get('Sex')
    bmi = request.form.get('BMI')
    email = request.form.get('inputemail') 
    name = request.form.get('name')
    children = request.form.get('noofchildren')
    smoker = request.form.get('Smoke')
    print(email)
    print(name)
    if sex == 'Male':
        sex = 1
    else:
        sex = 0
    if smoker == 'Yes':
        smoker = 1
    else:
        smoker = 0    
    final_features = [np.array((age, sex, bmi, children, smoker))]
    prediction = model.predict(final_features)
    msg = Message('Insurance Prediction',sender='quizwebsiteadp@gmail.com',recipients=[email])
    msg.body=f'''hi {name} Your predicted Insurance value is  : {prediction}'''
    mail.send(msg)
    print(prediction)
    return redirect('/')
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