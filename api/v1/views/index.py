#!/usr/bin/python3
""" Results Indexing """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    model_classes = [Amenity, City, Place, Review, State, User]
    model_names = ["amenities", "cities", "places", "reviews", "states", "users"]

    object_counts = {}
    for i in range(len(model_classes)):
        object_counts[model_names[i]] = storage.count(model_classes[i])

    return jsonify(object_counts)
