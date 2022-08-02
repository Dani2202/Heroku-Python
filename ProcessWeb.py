from unittest import result
from flask import Flask, jsonify

from pip import main
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum== copy_n):
        print(f"{copy_n} is an armstrong number")
        result ={
            "Number":copy_n,
            "Armstrong": True,
            "Server IP": "192.234.432.523"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result ={
            "Number":copy_n,
            "Armstrong": False
        }
    
    return jsonify(result)

@app.route('/data')
def data():
    return jsonify({
        "Data": {
            "a": 1,
            "b": 2,
            "c": 3,
        }})

if __name__ == "__main__":
    app.run(debug=True)