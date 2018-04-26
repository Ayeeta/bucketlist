from src.user import User
from src.bucketlist import Bucketlist
from flask import Flask, render_template, json, request, url_for, redirect, flash
from flask import Flask, Markup

app = Flask(__name__, template_folder='UI')
USER = User()

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        result = USER.login(request.form['email_address'], request.form['passwd'])
        if result == 'email and password incorrect':
            return render_template('register.html') 
        else:
            message = Markup("<h1>User Registered</h1>")
            flash(message)
            return redirect(url_for('/create_bucketlist.html'))
    return render_template('index.html')

@app.route('/register.html', methods=['GET', 'POST'])
def showsignUp():
    if request.method == 'POST':
        _fname = request.form['FName']
        _lname = request.form['LName']
        _email= request.form['Email']
        _password = request.form['PWD']
        USER.create_account(_fname, _lname, _email, _password)
        return redirect(url_for('/index.html'))
    return render_template('register.html') 

@app.route('/create_bucketlist.html', methods=['GET','POST'])
def showCreateB():
    return render_template('create_bucketlist.html')   
    
if __name__ == "__main__":
    app.debug= True
    app.run()
