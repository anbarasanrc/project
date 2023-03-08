from flask import Flask, request, render_template, redirect
import pyshorteners

app = Flask(__name__)
s = pyshorteners.Shortener()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['url']
    short_url = s.tinyurl.short(url)
    return render_template('result.html', short_url=short_url)

@app.route('/<path:path>')
def redirect_short_url(path):
    short_url = 'http://localhost:5000/' + path
    long_url = s.tinyurl.expand(short_url)
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
