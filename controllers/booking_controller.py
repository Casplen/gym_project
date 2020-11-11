from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
from models.member import Member
from models.booking import Booking

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("/bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("/bookings/new.html", members = members, gym_classes = gym_classes)

@bookings_blueprint.route("/bookings", methods=['POST'])
def add_booking():
    member_id = request.form["member"]
    gym_class_id = request.form["gym_class"]
    booked_gym_class = gym_class_repository.select(gym_class_id)
    booked_member = member_repository.select(member_id)
    booking = Booking(booked_member, booked_gym_class)
    booking_repository.save(booking)
    return redirect("/bookings")

