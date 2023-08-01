from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    return render_template('index.html', ip=ip)

if __name__ == '__main__':
    app.run(debug=True)
