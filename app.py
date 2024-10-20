from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Route to serve favicon.png
@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')

# Route to serve author.png
@app.route('/author.png')
def author_image():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'author.png')

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Simple Web Page</title>
            <link rel="icon" href="/favicon.png" type="image/png">
        </head>
        <body>
            <h1>Welcome to my simple Python web page!</h1>
            <p>This is a simple page running on port 5050.</p>
            <img src="/author.png" alt="Surya Nallamothu" style="align-items:center" >
        </body>
    </html>
    '''

if __name__ == '__main__':
    # Create a static folder to serve your image and favicon
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(host='0.0.0.0', port=5050)
