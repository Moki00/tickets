
# import secrets
from flask import Flask, make_response, redirect, render_template, request, session, url_for
from markupsafe import escape
# import werkzeug
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# app.secret_key = secrets.token_hex(32)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

# # @app.route('/user/<username>')
# # def show_user_profile(username):
# #     # show the user profile for that user
# #     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# @app.route('/')
# def index():
#     username = request.cookies.get('username')
#     # use cookies.get(key) instead of cookies[key] to not get a
#     # KeyError if the cookie is missing.

#     if username:
#         return render_template('index.html', username=username)
#     else:
#         resp = make_response(render_template('index.html'))
#         resp.set_cookie('username', 'the username')
#         return resp
#     # return 'index page at the start 001'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
    
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', person=name)

# from markupsafe import Markup
# # Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
# Markup.escape('<blink>hacker</blink>')
# Markup('&lt;blink&gt;hacker&lt;/blink&gt;')
# Markup('<em>Marked up</em> &raquo; HTML').striptags()
# 'Marked up » HTML'

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

# # login
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# # Upload files
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')
# # ...set the enctype="multipart/form-data" attribute on HTML form, or the browser will not transmit files

# # What the file was named before it was uploaded here:
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
#     ...

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return resp

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)

