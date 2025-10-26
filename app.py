from flask import Flask, render_template
from forms import Loginform, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'defngguuehf23uurugrug43ijff'

details = {}
details['email'] = 'password'
@app.route('/register', methods = ['GET', 'POST'])
def Register():
    form = RegistrationForm()
    return render_template('register.html', form=form)
    

@app.route('/login', methods = ['GET', 'POST'])
def Login():
    form = Loginform()
    return render_template('login.html', form = form)

if __name__ == "__main__":
    app.run(debug = True)