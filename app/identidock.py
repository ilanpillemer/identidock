from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_Spocker():
    return 'Hello Spocker!\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  
