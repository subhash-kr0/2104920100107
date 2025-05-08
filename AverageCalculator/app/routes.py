from flask import Blueprint, render_template, request, flash, jsonify
from .forms import NumberForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    average = None

    if form.validate_on_submit():
        numbers = form.numbers.data
        try:
            # Parse comma-separated numbers
            num_list = [float(n.strip()) for n in numbers.split(',')]
            average = sum(num_list) / len(num_list)
        except Exception:
            flash("Invalid input! Please enter valid numbers separated by commas.", "danger")

    return render_template("index.html", form=form, average=average)





@main.route('/average', methods=['POST', 'GET'])
def calculate_average():
    """
    Endpoint to calculate average of comma-separated numbers received in JSON.
    Input Format:
    {
        "numbers": "10, 20, 30"
    }
    Output:
    {
        "average": 20.0
    }
    """
    data = request.get_json(silent=True)

    # Validate JSON and required key
    if not data or 'numbers' not in data:
        return jsonify({'error': 'Invalid or missing "numbers" field in JSON'}), 400

    try:
        # Convert comma-separated string to a list of floats
        number_strings = map(str.strip, data['numbers'].split(','))
        numbers = list(map(float, number_strings))

        if not numbers:
            return jsonify({'error': 'List of numbers cannot be empty.'}), 400

        # Efficient average calculation
        avg = round(sum(numbers) / len(numbers), 2)  # Rounded to 2 decimals

        return jsonify({'average': avg}), 200

    except ValueError:
        return jsonify({'error': 'Ensure all inputs are valid numbers separated by commas.'}), 400

@main.errorhandler(404)
def not_found(_):
    return jsonify({'error': 'Endpoint not found'}), 404

@main.errorhandler(500)
def server_error(_):
    return jsonify({'error': 'Internal server error'}), 500