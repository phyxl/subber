from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
@app.route('/index.html')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')
	
@app.route('/<page>')
def show_page(page):
	return render_template(page)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
