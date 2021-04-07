import flask

app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='static')

@app.route('/')
def root():
    s = 'Flask'
    s_desc = 'web framework'
    s_auth = 'Pallets'
    return flask.render_template('index.html',
                                 subject=s,
                                 subject_description=s_desc,
                                 subject_author=s_auth)

@app.route('/404')
def _404():
    return '<h1>Oops!</h1><p>Sorry, you need to go back to your main page</p><p><a href="../">Main page</a></p>'

@app.route('/whatis/<query>')
def query_response(query):
    if query == 'this-site':
        return '<h1>The flask practice site!</h1>'
    return flask.redirect('/404')

@app.route('/double-calcium/<int:amount>')
def double_calcium(amount):
    return f'<p>{amount * 2}</p>'

@app.route('/anything/<path:anything>')
def route_anything(anything):
    return '<p>Works!</p>'

@app.route('/<page>')
def webpage(page):
    if page in ['index.html', 'left-sidebar.html', 'right-sidebar.html', 'no-sidebar.html', 'contact.html']:
        if page == 'index.html':
            return flask.redirect('/')
        else:
            return flask.render_template(page)
    return None
