from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Funkcje pomocnicze do obsługi danych użytkowników
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=2)

# Funkcje pomocnicze do obsługi danych
def load_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

# Strona główna
@app.route('/')
def home():
    return render_template('index.html')

# Strona rejestracji
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        if username in users:
            flash('Username already exists', 'danger')
        else:
            users[username] = password
            save_users(users)
            flash('Registration successful', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# Strona logowania
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# Strona wylogowania
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('home'))

# Strona danych
@app.route('/data')
def data():
    data = load_data()
    return render_template('data.html', data=data)

# Strona dodawania nowych danych
@app.route('/data/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        new_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'pesel': request.form['pesel'],
            'birth_date': request.form['birth_date'],
            'order': request.form['order']
        }

        data_list = load_data()
        data_list.append(new_data)
        save_data(data_list)

        flash('Data added successfully', 'success')
        return redirect(url_for('data'))

# Strona edycji danych
@app.route('/data/edit/<int:index>', methods=['GET', 'POST'])
def edit_data(index):
    data_list = load_data()
    if request.method == 'POST':
        edited_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'pesel': request.form['pesel'],
            'birth_date': request.form['birth_date'],
            'order': request.form['order']
        }

        data_list[index] = edited_data
        save_data(data_list)

        flash('Data edited successfully', 'success')
        return redirect(url_for('data'))

# Strona usuwania danych
@app.route('/data/delete/<int:index>', methods=['DELETE'])
def delete_data(index):
    data_list = load_data()
    if index < len(data_list):
        del data_list[index]
        save_data(data_list)
        return jsonify({'message': 'Data deleted successfully'})
    else:
        return jsonify({'error': 'Invalid index'}), 400  # Bad Request

if __name__ == '__main__':
    app.run(debug=True)
