from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def get_ip():
    # Caddy Server: header_up X-Forwarded-For {remote_host}
    forwarded_for = request.headers.get('X-Forwarded-For')
    client_ip = forwarded_for.split(',')[0].strip()
    return client_ip

def get_location(ip):
    url = "http://ip-api.com/json/" + ip
    response = requests.request("GET", url)
    result = json.loads(response.text)
    isp = result["isp"]
    country = result["country"]
    return isp, country


@app.route('/')
def index():
    ip = get_ip()
    location = get_location(ip)
    return render_template('index.html', ip=ip, isp=location[0], country=location[1])

@app.route('/ip')
def return_ip():
    ip = get_ip()
    return ip

if __name__ == '__main__':
    app.run(debug=True, port=5000)