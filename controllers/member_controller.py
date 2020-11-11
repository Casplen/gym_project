from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member

import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

import datetime

member_blueprint = Blueprint("members", __name__)

@member_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members= members)

@member_blueprint.route("/member/<id>")
def show(id):
    member = member_repository.select(id)
    membership_types = member_repository.select_types()
    gym_classes = booking_repository.gym_classes(id)
    return render_template("/members/show.html", member = member, membership_types = membership_types, gym_classes = gym_classes)

@member_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete(id):
    member_repository.delete(id)
    return redirect("/members")

@member_blueprint.route("/members/new")
def new_member():
    membership_types = member_repository.select_types()
    date_today = datetime.date.today()
    return render_template("/members/new.html", membership_types = membership_types, date_today = date_today)

@member_blueprint.route ("/members", methods=['POST'])
def add_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    start_date = request.form["start_date"]
    membership_type = request.form["membership_type"]
    new_member = Member(first_name, last_name, membership_type, start_date)
    member_repository.save(new_member)
    return redirect("/members")

@member_blueprint.route("/members/<id>/edit")
def edit_member(id):
    membership_types = member_repository.select_types()
    member = member_repository.select(id)
    return render_template("/members/edit.html", member= member, membership_types = membership_types)

@member_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    start_date = request.form["start_date"]
    membership_type = request.form["membership_type"]
    active_status = request.form["active_status"]
    updated_member = Member(first_name, last_name, membership_type, start_date, active_status, id)
    member_repository.update(updated_member)
    return redirect("/members/" + id)