# backend/app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/api/userData')
def get_user_data():
    # Replace this with your actual user data retrieval logic
    user_data = {
        'name': 'Kelvin Agimogim',
        'email': 'kelvinagimogim@gmail.com',
        'location': 'Abuja, Nigeria',
        'followers': 7,
        'following': 29,
        'timezone': '19:00 (UTC -12:00)',
        # Add other profile information
    }

    return render_template('index.html', userData=user_data)

if __name__ == '__main__':
    app.run(debug=True)

