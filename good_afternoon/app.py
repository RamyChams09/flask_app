from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        current_time = datetime.now().time()
        greeting, image_filename = get_greeting(current_time)
        return render_template('index.html', greeting=greeting, user_name=user_name, image_filename=image_filename)

    return render_template('index.html')

def get_greeting(current_time):
    return 'Good Afternoon', 'afternoon.jpg'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
