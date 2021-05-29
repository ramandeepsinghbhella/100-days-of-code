from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["get", "post"])
def login():
    login_data = request.form
    EMAILS = []
    PASSWORDS = []
    with open('account_data.csv', 'r') as r_csv:
        csv_reader = csv.reader(r_csv)
        for row in csv_reader:
            emails = row[0]
            EMAILS.append(emails)
            passwords = row[1]
            PASSWORDS.append(passwords)
        if login_data["email"] in EMAILS:
            if login_data["password"] in PASSWORDS:
                return render_template('login_successful.html')
            else:
                return render_template('wrong_password.html')
        else:
            return render_template('wrong_email.html')


@app.route('/signup', methods=["get", "post"])
def signup():
    return render_template('sign_up.html')


@app.route('/successful', methods=["get", "post"])
def successful():
    if request.method == "POST":
        data = request.form
        with open('account_data.csv', 'a', newline='') as csv_file:
            writer_object = csv.writer(csv_file)
            writer_object.writerow([data["email"], data["password"]])
    return render_template('successful.html')



if __name__ == '__main__':
    app.stop()