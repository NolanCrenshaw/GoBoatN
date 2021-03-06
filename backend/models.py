from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()


# Class Definitions
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.Binary(100), nullable=False)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    zipcode = db.Column(db.String(20))
    about = db.Column(db.Text)
    skill = db.Column(db.Integer)
    profile_pic = db.Column(db.String(255))
    banner_pic = db.Column(db.String(255))
    sprite = db.Column(db.String(255))
    updated_at = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    date_added = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    boats = db.relationship("Boat", backref="user", lazy=True)
    vehicles = db.relationship("Vehicle", backref="user", lazy=True)
    invites = db.relationship("Invite", backref="user", lazy=True)
    boaters = db.relationship("Boater", backref="user", lazy=True)
    friends = db.relationship("Friend", backref="user", lazy=True)

    def to_safe_object(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "zipcode": self.zipcode,
            "about": self.about,
            "skill": self.skill,
            "profile_pic": self.profile_pic,
            "banner_pic": self.banner_pic,
            "sprite": self.sprite,
            "date_added": self.date_added,
        }


class River(db.Model):
    __tablename__ = "rivers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    class_designation = db.Column(db.Integer)
    length = db.Column(db.Integer)
    description = db.Column(db.Text)
    region = db.Column(db.String(255))
    # latitude = db.Column(db.Integer)
    # longitude = db.Column(db.Integer)

    accesses = db.relationship("Access", backref="user", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "class_designation": self.class_designation,
            "length": self.length,
            "description": self.description,
            "region": self.region,
            # "latitude": self.latitude,
            # "longitude": self.longitude,
        }


class Access(db.Model):
    __tablename__ = "accesses"

    id = db.Column(db.Integer, primary_key=True)
    river_id = db.Column(db.Integer, db.ForeignKey(
        "rivers.id"), nullable=False)
    name = db.Column(db.String(255), default="unnamed")
    put_in_option = db.Column(db.Boolean)
    take_out_option = db.Column(db.Boolean)
    latitude = db.Column(db.Numeric(8, 6))
    longitude = db.Column(db.Numeric(9, 6))

    def to_dict(self):
        return {
            "id": self.id,
            "river": self.river_id,
            "name": self.name,
            "put_in_option": self.put_in_option,
            "take_out_option": self.take_out_option,
            "latitude": str(self.latitude),
            "longitude": str(self.longitude),
        }


class Boat(db.Model):
    __tablename__ = "boats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    occupancy = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String(255))
    date_added = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return f"{self.name}, {self.make}, {self.user}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user": self.user_id,
            "occupancy": self.occupancy,
            "sprite": self.sprite,
            "date_added": self.date_added,
        }


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    make = db.Column(db.String(255), nullable=False)
    occupancy = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String(255))
    date_added = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "make": self.make,
            "user": self.user_id,
            "occupancy": self.occupancy,
            "sprite": self.sprite,
            "date_added": self.date_added,
        }


class Friend(db.Model):
    __tablename__ = "friends"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    friend_id = db.Column(db.Integer, nullable=False)
    date_added = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    def to_int(self):
        return self.friend_id


class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String, nullable=False)
    scheduled_time = db.Column(db.DateTime)
    river_id = db.Column(db.Integer, db.ForeignKey(
        "rivers.id"), nullable=False)
    trip_leader = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    put_in = db.Column(db.Integer, db.ForeignKey("accesses.id"))
    take_out = db.Column(db.Integer, db.ForeignKey("accesses.id"))
    date_added = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    invites = db.relationship("Invite", backref="trip", lazy=True)
    boaters = db.relationship("Boater", backref="trip", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "scheduled_time": self.scheduled_time,
            "river_id": self.river_id,
            "trip_leader": self.trip_leader,
            "put_in": self.put_in,
            "take_out": self.take_out,
            "date_added": self.date_added,
        }


class Invite(db.Model):
    __tablename__ = "invites"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"), nullable=False)
    sender_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    date_added = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "trip_id": self.trip_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "date_added": self.date_added,
        }


class Boater(db.Model):
    __tablename__ = "boaters"

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey("trips.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    boat_id = db.Column(db.Integer, db.ForeignKey("boats.id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    driver = db.Column(db.Boolean)
    meet_at = db.Column(db.String(255))
    date_added = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "trip_id": self.trip_id,
            "user_id": self.user_id,
            "boat_id": self.boat_id,
            "vehicle_id": self.vehicle_id,
            "driver": self.driver,
            "meet_at": self.meet_at,
            "date_added": self.date_added,
        }
