# General way to serve different pages on a site:

from Flask import Flask
app = Flask('__main__')


@app.route('/')
def yay_it_works():
    return Flask.render_template('hello.html')

app.run(debug=true)
