from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

def load_names(race):
    with open(f'data/{race}.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_name', methods=['POST'])
def generate_name():
    data = request.get_json()
    races = data.get('races', [])
    gender = data.get('gender')

    if not races:
        return jsonify({'error': 'No races selected'}), 400

    race = random.choice(races)
    names = load_names(race)

    first_name = random.choice(names[gender]).capitalize()
    last_name = random.choice(names['last'])

    return jsonify({'firstName': first_name, 'lastName': last_name})

if __name__ == '__main__':
    app.run(debug=True)