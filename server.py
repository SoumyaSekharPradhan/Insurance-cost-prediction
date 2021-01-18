from flask import Flask, jsonify, request, render_template, url_for
import util
app = Flask(__name__, template_folder='../Client')


@app.route('/')
def home():
    return render_template('app.html')


@app.route('/get_locations')
def get_locations():
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_insurance_cost', methods=['POST'])
def predict_insurance_cost():
    age = int(request.form['age'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    gender = request.form['gender']
    is_smoker = request.form['is_smoker']
    location = request.form['loc']

    response = jsonify({
        'estimated_charges': util.get_estimated_charges(age, bmi, children, gender, is_smoker, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting server")
    util.load_saved_artifacts()
    app.run(debug=True)
