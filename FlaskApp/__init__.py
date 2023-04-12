from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect
import forms


app = Flask(__name__)

app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    comment_form = forms.CommentForm()
    title = "FlaskRogeRRR"
    return render_template ('index.html', title=title, form=comment_form)

if __name__ == '__main__':
    app.run (debug=True, port=8001)