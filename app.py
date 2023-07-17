from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Password format checker function
def check_password_format(password):
    requirements = []
    if len(password) < 8:
        requirements.append("Password should be at least 8 characters.")
    if not any(char.isupper() for char in password):
        requirements.append("Password should contain an uppercase letter.")
    if not any(char.islower() for char in password):
        requirements.append("Password should contain a lowercase letter.")
    if not password[-1].isdigit():
        requirements.append("Password should end in a number.")
    return requirements

# Route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    password_report = None
    requirements_not_met = []

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        requirements_not_met = check_password_format(password)

        if not requirements_not_met:
            password_report = "Password passed the requirements."
        else:
            password_report = "Password does not meet the requirements. Please try again."

    return render_template('index.html', password_report=password_report, requirements_not_met=requirements_not_met)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
