import json
import random

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# Creates an instance of the Flask application.
#   - __name__: A special variable that represents the name of the current module.
#     It's used by Flask to determine the application's root path.


# Function to load names from a JSON file
def load_names(race):
    """Loads names from the specified race's JSON file."""
    # Opens the JSON file for the given race in read mode ('r').
    #   - f'data/{race}.json':  Uses an f-string to construct the file path.
    with open(f'data/{race}.json', 'r') as f:
        # Loads the JSON data from the opened file using json.load() and returns it.
        return json.load(f)


# Route for the main index page
@app.route('/')
def index():
    """Renders the index.html template."""
    return render_template('index.html')
    # Renders the 'index.html' template using render_template() and returns the rendered HTML.


# Route for generating a name
@app.route('/generate_name', methods=['POST'])
def generate_name():
    """Generates a random name based on selected race and gender."""
    data = request.get_json()  # Parses request data as JSON
    first_races = data.get('firstRaces', )  # Gets first name races
    first_gender = data.get('firstGender')  # Gets first name gender
    last_races = data.get('lastRaces', )  # Gets last name races

    # Validation: Check if any options are selected
    if not first_races and not last_races and not first_gender:
        return jsonify({'error': 'Please set your options below to get a name'}), 400  # Returns error if no options

    # Validation: Check if gender is selected
    if not first_gender:
        return jsonify({'error': 'Please select a gender.'}), 400  # Returns error if no gender

    # Validation: Check for multiple races
    message = ""  # Initializes message string
    if len(first_races) > 1 or len(last_races) > 1:
        message = "Selecting more than one race will randomize between the two."  # Sets message for multiple races

    # Handling cases with a single race selected for first or last name
    if len(first_races) == 1 and not last_races:
        message += " Only one race selected for first name. Using selected race for the last name."  # Appends message
        last_races = first_races  # Sets last races to first races
    elif len(last_races) == 1 and not first_races:
        message += " Only one race selected for last name. Using selected race for the first name."  # Appends message
        first_races = last_races  # Sets first races to last races

    # Select a race from the User's chosen races; If a user selects more than 1, it will randomly choose a race
    first_race = random.choice(first_races)
    # Load names for the chosen race
    first_names = load_names(first_race)

    # Select a race from the User's chosen races; If a user selects more than 1, it will randomly choose a race
    last_race = random.choice(last_races)
    # Load names for the last name's race
    last_names = load_names(last_race)

    # Select a race from the User's chosen races; If a user selects more than 1, it will randomly choose a race
    first_name = random.choice(first_names[first_gender]).capitalize()
    # Select a random last name
    last_name = random.choice(last_names['last'])

    # Return the generated first and last names along with the message
    return jsonify({'firstName': first_name, 'lastName': last_name, 'message': message})


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)