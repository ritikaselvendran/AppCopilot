from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user for demonstration
users = {
    "example@gmail.com": "password123",
    "ritikajiggy@gmail.com": "riti@05"
}

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # You can add registration logic here
        return redirect(url_for('login'))
    return render_template('Register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            return "Logged in successfully!"
        else:
            error = "Invalid email or password."
    return render_template('Login.html', error=error)

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        # You can add logic to send reset link here
        return f"Reset link sent to {email}"
    return render_template('ResetPassword.html')

if __name__ == '__main__':
    app.run(debug=True)
