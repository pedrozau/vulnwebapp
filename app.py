from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Define as portas para cada aplicação vulnerável
    apps = [
        {"name": "DVWA", "port": 8081},
        {"name": "Juice Shop", "port": 8082},
        {"name": "Mutillidae", "port": 8083},
        {"name": "WebGoat", "port": '8084/WebGoat/'},
        {"name": "bWAPP", "port": 8085},
        {"name": "Hackazon", "port": 8086},
        {"name": "XVWA", "port": 8087},
    
    ]

    # Gera as URLs dinamicamente com base no host atual
    for app in apps:
        app["url"] = f"{request.host_url.rstrip('/')}:{app['port']}"

    return render_template('index.html', apps=apps)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
