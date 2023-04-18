from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask_wtf.csrf import CSRFProtect
import forms


app = Flask(__name__)

app.secret_key = 'poiuytrewqasdfghjklñlkmnbvcxz'
csrf = CSRFProtect(app)

@app.route('/', methods = ['GET','POST'])
def index():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST':
        print (comment_form.username.data)
        print (comment_form.edad.data)
        print (comment_form.email.data)
    title = "FlaskRogeRRR"
    return render_template ('index.html', title=title, form=comment_form)

@app.route('/cookie')
def cookie():
    response = 
    return render_template('cookie.html')

if __name__ == '__main__':
    app.run (debug=True, port=8003)