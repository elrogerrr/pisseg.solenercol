from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import make_response
from flask import render_template
from flask_wtf.csrf import CSRFProtect
import forms


app = Flask(__name__)

app.secret_key = 'poiuytrewqasdfghjklñlkmnbvcxz'
csrf = CSRFProtect(app)

@app.route('/', methods = ['GET','POST'])
def index():
    if 'username' in session:
        username = session['username']
        print (username)

    custome_cookie = request.cookies.get('custome_cookie')
    print (custome_cookie)
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST':
        print (comment_form.username.data)
        print (comment_form.edad.data)
        print (comment_form.email.data)
    title = "FlaskRogeRRR"
    return render_template ('index.html', title=title, form=comment_form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET','POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data
    return render_template('login.html', form = login_form)
    

@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie','No comeremos Mañana ni hoy Mami')
    return response

if __name__ == '__main__':
    app.run (debug=True, port=8003)