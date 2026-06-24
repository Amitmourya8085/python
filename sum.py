from flask import Flask 
from flask import requests,jsonify

app = Flask(__name__)

@app.route("/sum")
def sum():
    a = requests.args.get("a")
    b = requests.args.get("b")

    if a and b:
        total=a+b
        return jsonify({
            "status":"successful",
            "sum":total
        })
    else:
        return jsonify({
            "status":"failed",
            "msg":"Please provide both a and b"
        })
    

    app.run(debug=True)