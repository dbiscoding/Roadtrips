from flask import render_template
from . import bp
from models import destination as d

@bp.route('/destination/<int:id>')
def destination(id):
    destination = d.Destination.query.get(id)
    return render_template('destination.html', destination=destination)

@bp.route('/destinations')
def destinations():
    destinations = d.Destination.query.all()
    return render_template('destinations.html', destinations=destinations)

