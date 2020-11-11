from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
from models.member import Member
from models.booking import Booking

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository