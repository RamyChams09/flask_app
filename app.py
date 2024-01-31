from flask import Flask, render_template
from datetime import datetime
from good_morning.app import good_morning_bp
from good_afternoon.app import good_afternoon_bp
from good_evening.app import good_evening_bp
from good_night.app import good_night_bp

app = Flask(__name__)

def get_greeting_app():
    current_time = datetime.now().time()
    if datetime.strptime('05:00', '%H:%M').time() <= current_time < datetime.strptime('11:00', '%H:%M').time():
        return good_morning_bp
    elif datetime.strptime('11:00', '%H:%M').time() <= current_time < datetime.strptime('19:00', '%H:%M').time():
        return good_afternoon_bp
    elif datetime.strptime('19:00', '%H:%M').time() <= current_time <= datetime.strptime('23:59', '%H:%M').time():
        return good_evening_bp
    else:
        return good_night_bp

app.register_blueprint(get_greeting_app(), url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)