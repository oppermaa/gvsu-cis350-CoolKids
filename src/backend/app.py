from flask import Flask, render_template, request, jsonify
from convertor import convert  # Correct function import
import ipinfo

# Flask app initialization, adjusted to find templates in the "frontend" directory
app = Flask(__name__, template_folder="../frontend")

# Configure IPInfo for location-based suggestions (replace with your actual token)
ACCESS_TOKEN = 'your_ipinfo_access_token'
handler = ipinfo.getHandler(ACCESS_TOKEN)

@app.route('/')
def home():
    """
    Route for the home page.
    """
    return render_template('index.html')

@app.route('/articles')
def articles():
    """
    Route for the articles page.
    """
    return render_template('articles.html')

@app.route('/about')
def about():
    """
    Route for the about page.
    """
    return render_template('about.html')

@app.route('/settings')
def settings():
    """
    Route for the settings page.
    """
    return render_template('settings.html')

@app.route('/convert', methods=['POST'])
def convert_value():
    """
    Handle the conversion request from the frontend.
    """
    try:
        # Retrieve data from the request
        data = request.json
        print(f"Data received: {data}")  # Debugging log
        
        from_unit = data.get('from_unit').lower()  # Normalize unit names to lowercase
        to_unit = data.get('to_unit').lower()      # Normalize unit names to lowercase
        value = data.get('value')

        # Validate input
        if not from_unit or not to_unit or value is None:
            return jsonify({'error': 'Invalid input parameters.'}), 400

        # Perform conversion
        print(f"Performing conversion: {value} {from_unit} to {to_unit}")  # Debugging log
        converted_value = convert(float(value), from_unit, to_unit)
        if converted_value is None:
            return jsonify({'error': f"Conversion not supported for {from_unit} to {to_unit}."}), 400

        # Return the converted value
        return jsonify({'result': round(converted_value, 2)})

    except Exception as e:
        print(f"Conversion error: {str(e)}")  # Debugging log
        return jsonify({'error': f'Error while performing conversion: {str(e)}'}), 500

@app.route('/get_country_system', methods=['GET'])
def get_country_system():
    """
    Get the country and suggested unit system based on the user's IP.
    """
    try:
        ip_address = request.remote_addr
        details = handler.getDetails(ip_address)
        country = details.country_name if details.country_name else "Unknown"
        unit_system = "Imperial" if country in ['United States', 'Liberia', 'Myanmar'] else "Metric"
        print(f"Detected country: {country}, Unit system: {unit_system}")  # Debugging log
        return jsonify({'country': country, 'unit_system': unit_system})
    except Exception as e:
        print(f"Error fetching country details: {str(e)}")  # Debugging log
        return jsonify({'error': f'Error while fetching country details: {str(e)}'}), 500

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """
    Error handler for 404 - Page Not Found.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """
    Error handler for 500 - Internal Server Error.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
