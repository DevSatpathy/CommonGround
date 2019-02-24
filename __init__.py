from backend.aggregation import data
from backend.aggregation.locationfinder import generate_coordinates
from flask import Flask
app = Flask(__name__)

generate_coordinates()
app.run()