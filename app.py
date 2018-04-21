from flask import Flask, render_template, request
from flask import Flask

app = Flask(__name__, template_folder='UI')

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/signUp')
def signUp():
    return render_template('register.html')

@app.route('/register')
def register():
    return render_template('register.html')


    
if __name__ == "__main__":
    app.debug= True
    app.run()