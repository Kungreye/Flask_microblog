from flask import render_template
from app import app     # 1st app: package; 2nd app: Flask instance (defined in __init__.py), a memeber of app package.

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kungreye'}
    posts = [
        {
            'author': {'username': 'Tsui'},
            'body': 'This issue is getting on my nerves!'
        },
        {
            'author': {'username': 'Feng'},
            'body': 'Apologize, man. Really sorry for that.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)