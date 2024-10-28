from flask import Flask, render_template, request, jsonify
import convertor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    value = float(data['value'])
    conversion_type = data['conversion_type']
    
    if conversion_type == 'miles-to-kilometers':
        result = convertor.miles_to_kilometers(value)
    elif conversion_type == 'kilometers-to-miles':
        result = convertor.kilometers_to_miles(value)
    # Add more conversions as needed
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)


