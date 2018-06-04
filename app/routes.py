from app import app     # 1st app: package; 2nd app: Flask instance (defined in __init__.py), a memeber of app package.

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"