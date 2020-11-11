from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass

import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes = gym_classes)

@gym_classes_blueprint.route("/gym_classes/new")
def new_gym_class():
    class_types = gym_class_repository.select_types()
    return render_template("gym_classes/new.html", class_types = class_types)

@gym_classes_blueprint.route("/gym_classes", methods=['POST'])
def add_gym_class():
    class_type = request.form["gym_class_type"]

    check = gym_class_repository.check_type_exists(class_type)
    if check == False:
        gym_class_repository.new_type(class_type)

    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    duration = request.form["duration"]
    new_class = GymClass(class_type, date, time, capacity, duration)
    gym_class_repository.save(new_class)
    return redirect("/gym_classes")

@gym_classes_blueprint.route("/gym_classes/<id>")
def show(id):
    gym_class = gym_class_repository.select(id)
    members = booking_repository.members(id)
    return render_template("gym_classes/show.html", gym_class = gym_class, members = members)

@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    class_types = gym_class_repository.select_types()
    return render_template("gym_classes/edit.html", gym_class = gym_class, class_types = class_types)

@gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
def update_gym_class(id):
    class_type = request.form["gym_class_type"]

    check = gym_class_repository.check_type_exists(class_type)
    if check == False:
        gym_class_repository.new_type(class_type)

    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    duration = request.form["duration"]
    edited_class = GymClass(class_type, date, time, capacity, duration, id)
    gym_class_repository.update(edited_class)

    redirect_gym_class = gym_class_repository.select(id)
    redirect_class_types = gym_class_repository.select_types()
    return redirect("/gym_classes/" + id)

@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=['POST'])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")