import util
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

white =['http://127.0.0.1:5500']
@app.after_request
def add_cors_headers(response):
    r = request.referrer[:-1]
    if r in white:
        response.headers.add('Access-Control-Allow-Origin', r)
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
        response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
        response.headers.add('Access-Control-Allow-Headers', 'Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

@app.route('/h')
def hello():
    return "hi"

@app.route('/loc')
def get_location():
    util.load_assests()
    obj = jsonify(util.__location_list.tolist())
    return obj

@app.route('/get_price', methods=['POST'])
def get_price():
    totat_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    util.load_assests()
    price = util.get_estimated_price(location=location, bhk=bhk, bath=bath, tsqft=totat_sqft)
    return str(price)

if __name__ == "__main__":
    print("starting")
    app.run()


