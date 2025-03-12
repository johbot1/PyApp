from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Function to load names from a JSON file
def load_names(race):
    """Loads names from the specified race's JSON file."""
    with open(f'data/{race}.json', 'r') as f:
        return json.load(f)

# Route for the main index page
@app.route('/')
def index():
    """Renders the index.html template."""
    return render_template('index.html')

# Route for generating a name
@app.route('/generate_name', methods=['POST'])
def generate_name():
    """Generates a random name based on selected race and gender."""
    data = request.get_json()
    first_races = data.get('firstRaces', [])
    first_gender = data.get('firstGender')
    last_races = data.get('lastRaces', [])

    # Check if races are selected for both first and last names
    if not first_races or not last_races:
        return jsonify({'error': 'Please select races for both first and last names'}), 400

    # Select a random race for the first name
    first_race = random.choice(first_races)
    # Load names for the first name's race
    first_names = load_names(first_race)

    # Select a random race for the last name
    last_race = random.choice(last_races)
    # Load names for the last name's race
    last_names = load_names(last_race)

    # Select a random first name based on gender and capitalize it
    first_name = random.choice(first_names[first_gender]).capitalize()
    # Select a random last name
    last_name = random.choice(last_names['last'])

    # Return the generated first and last names as JSON
    return jsonify({'firstName': first_name, 'lastName': last_name})

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)