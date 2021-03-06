# Package Requirements
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local Requirements
from ..models import db, River


# Blueprint Declaration
river = Blueprint('rivers', __name__)


@river.route('/', methods=["GET", "POST"])
@jwt_required()
def get_rivers():

    # POST path
    if request.method == "POST":
        data = request.get_json()
        river = River(
            name=data["name"],
            class_designation=data["class"],
            description=data["description"],
            region=data["region"]
        )
        db.session.add(river)
        db.session.commit()
        return jsonify(message="River Successfully Added"), 200

    # GET path
    else:
        # return all rivers ordered by name
        rivers = []
        river_objects = River.query.order_by(River.name).all()
        for river_obj in river_objects:
            river = river_obj.to_dict()
            rivers.append(river)
        return jsonify(rivers=rivers), 200


@river.route('/<id>', methods=["GET", "PUT"])
@jwt_required()
def get_rivers(id):
    river_obj = River.query.filter_by(id=id).first()

    # PUT path
    if request.method == "PUT":
        data = request.get_json()
        river_obj.name = data["name"]
        river_obj.class_designation = data["class"]
        river_obj.description = data["description"]
        river_obj.region = data["region"]
        db.session.commit()
        return jsonify(message="River Successfully Updated"), 200

    # GET path
    else:
        return jsonify(river_obj.to_dict()), 200


@river.route('/accesses/<id>/', methods=["GET"])
@jwt_required()
def accesses_by_river(id):

    # GET path
    access_list = []
    river_obj = River.query.filter_by(id=id).first()
    access_objects = river_obj.accesses
    for access in access_objects:
        access_list.append(access.to_dict())
    return jsonify(accesses=access_list), 200
