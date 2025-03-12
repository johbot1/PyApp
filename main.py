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
    races = data.get('races', [])
    gender = data.get('gender')

    # Check if any races are selected
    if not races:
        return jsonify({'error': 'No races selected'}), 400

    # Select a random race from the selected races
    race = random.choice(races)
    # Load names for the selected race
    names = load_names(race)

    # Select a random first name based on gender and capitalize it
    first_name = random.choice(names[gender]).capitalize()
    # Select a random last name
    last_name = random.choice(names['last'])

    # Return the generated first and last names as JSON
    return jsonify({'firstName': first_name, 'lastName': last_name})

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)