from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Simple Web Page</title>
        </head>
        <body>
            <h1>Welcome to my simple web page!</h1>
            <p>This is a simple page running on port 5050.</p>
            <img src="author.png" alt="Surya Nallamothu" style="border: 2px solid black; border-radius: 5px;">
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
