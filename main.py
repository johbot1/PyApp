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

    # Validation: Check if any options are selected
    if not first_races and not last_races and not first_gender:
        return jsonify({'error': 'Please set your options below to get a name'}), 400

    # Validation: Check if gender is selected
    if not first_gender:
        return jsonify({'error': 'Please select a gender.'}), 400


    # Validation: Check for multiple races
    message = ""
    if len(first_races) > 1 or len(last_races) > 1:
        message = "Selecting more than one race will randomize between the two."

    # Handling cases with a single race selected for first or last name
    if len(first_races) == 1 and not last_races:
        message += " Only one race selected for first name. Using selected race for the last name."
        last_races = first_races
    elif len(last_races) == 1 and not first_races:
        message += " Only one race selected for last name. Using selected race for the first name."
        first_races = last_races

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

    # Return the generated first and last names along with the message
    return jsonify({'firstName': first_name, 'lastName': last_name, 'message': message})


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)