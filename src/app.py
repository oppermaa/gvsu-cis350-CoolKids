from flask import Flask, render_template, request, jsonify
from convertor import convert
import ipinfo

app = Flask(__name__)

# Configure IPInfo for location-based suggestions (optional; replace with your IPInfo token)
ACCESS_TOKEN = 'your_ipinfo_access_token'
handler = ipinfo.getHandler(ACCESS_TOKEN)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/convert', methods=['POST'])
def convert_value():
    data = request.json
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')
    value = data.get('value')
    
    try:
        result = convert(value, from_unit, to_unit)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_country_system', methods=['GET'])
def get_country_system():
    ip_address = request.remote_addr
    country = "Unknown"
    unit_system = "Metric"

    try:
        details = handler.getDetails(ip_address)
        country = details.country_name
        # Determine the unit system based on the country (example logic)
        if country in ['United States', 'Liberia', 'Myanmar']:
            unit_system = "Imperial"
    except Exception as e:
        print(f"IPInfo error: {e}")

    return jsonify({'country': country, 'unit_system': unit_system})

# Set up error handling (optional, but recommended for debugging)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
