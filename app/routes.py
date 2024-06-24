from flask import render_template, request
from app import app


user_data = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        user = {'name': name, 'city': city, 'hobby': hobby, 'age': age}
        user_data.append(user)

    return render_template('index.html', user_data=user_data)
