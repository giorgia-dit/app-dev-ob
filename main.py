from flask import Flask, render_template, jsonify
import random

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

nucleotides = [('A', '#FF5722'), ('C', '#FFC107'), ('G', '#8BC34A'), ('T', '#00796B')]
stop_codons = ('TAA', 'TAG', 'TGA')
sequence = []

def random_item(items):
    return random.choice(items)

def update_triplet(last_item, triplet):
    triplet.append(last_item)
    if len(triplet) > 3:
        triplet.pop(0)

def check_triplet(triplet, stop_patterns):
    pattern = ''.join(triplet)
    if pattern in stop_patterns:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['GET'])
def update():
    nucleotide_value = random_item(nucleotides)
    update_triplet(nucleotide_value[0], sequence)
    check_result = check_triplet(sequence, stop_codons)
    return jsonify({'nucleotide': nucleotide_value[0], 'triplet': ''.join(sequence), 'check_result': check_result, 'color': nucleotide_value[1]})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
