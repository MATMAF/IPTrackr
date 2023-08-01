from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    ip = requests.get("https://api.ipify.org/?format=json").json()['ip']
    return render_template('index.html', ip=ip)

if __name__ == '__main__':
    app.run(debug=True)
