from flask import render_template, request, current_app
from . import bp
from models import destination as d
import requests

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        location = request.form.get('location')
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": location,
            "radius": 482803,  #300 miles in meters
            "type": "park",
            "key": current_app.config['GOOGLE_MAPS_API_KEY']
        }
        response = requests.get(url, params=params)
        places = response.json()['results']
        
        return render_template('results.html', places=places, api_key=current_app.config['GOOGLE_MAPS_API_KEY'])
    return render_template('search.html')