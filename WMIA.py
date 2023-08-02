from flask import Flask, render_template, request
from flask_sslify import SSLify
import requests
import json

app = Flask(__name__)
sslify = SSLify(app)

def get_location(ip):
    url = "http://ip-api.com/json/" + ip

    response = requests.request("GET", url)

    result = json.loads(response.text)

    isp = result["isp"]

    country = result["country"]

    return isp, country


@app.route('/')
def index():
    ip = request.remote_addr

    location = get_location(ip)

    return render_template('index.html', ip=ip, isp=location[0], country=location[1])

@app.route('/ip')
def return_ip():
    ip = request.remote_addr
    return ip

if __name__ == '__main__':
    app.run(debug=True)
