from flask import Flask, render_template, request
from flask_sslify import SSLify
import requests
import json
import config

app = Flask(__name__)
sslify = SSLify(app)

def get_location(ip):
    url = "https://api.apilayer.com/ip_to_location/" + ip
    payload = {}
    headers= {
    "apikey": config.APIKEY
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = json.loads(response.text)

    connection = result["connection"]

    isp = connection["isp"]

    country = result["country_name"]

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
