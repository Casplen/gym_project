from flask import Flask, render_template

from controllers.gym_class_controller import gym_classes_blueprint
from controllers.member_controller import member_blueprint
from controllers.booking_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(gym_classes_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)