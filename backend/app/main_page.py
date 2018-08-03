# -*- encoding: utf-8 -*-
"""
Routing file for main page
"""
from flask import Blueprint, jsonify, request

from app.models.country import Country, CountrySchema
from app.database import db_session

main_page = Blueprint('main_page', __name__)


@main_page.route('/')
def index():
    return 'Hello, World!'


@main_page.route('/countries')
def get_countries():
    country_objects = db_session.query(Country).all()

    # transforming into JSON-serializable objects
    schema = CountrySchema(many=True)
    countries = schema.dump(country_objects)

    # serializing as JSON
    return jsonify(countries.data)


@main_page.route('/countries', methods=['POST'])
def add_country():
    # mount country object
    posted_country = CountrySchema(only=('name', 'capital')
                                   ).load(request.get_json())
    country = Country(**posted_country.data)

    # persist country
    db_session.add(country)
    db_session.commit()

    # return created country
    new_country = CountrySchema().dump(country).data
    return jsonify(new_country), 201
