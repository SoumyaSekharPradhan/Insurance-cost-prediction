import json
import pickle
import numpy as np

locations = None
data__columns = []
model = None


def get_locations():
    global locations
    return locations


def load_saved_artifacts():
    print("Loading saved artifacts......")
    global locations
    global data__columns
    global model

    with open("./artifacts/columns.json", 'r') as f:
        data__columns = json.load(f)['data_columns']
        locations = data__columns[5:]

    with open("./artifacts/InsuranceCostPrediction.pkl", 'rb') as f:
        model = pickle.load(f)
    print("Loading the artifacts is completed.")


def get_estimated_charges(age, bmi, children, gender, is_smoker, location):
    global data__columns
    global model
    x = np.zeros(len(data__columns))
    x[0] = age
    x[1] = bmi
    x[2] = children
    if gender == 'male':
        x[3] = 1
    if is_smoker == 'yes':
        x[4] = 1
    try:
        loc_index = data__columns.index(location.lower())
    except:
        loc_index = -1
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_locations())
    # print(get_estimated_charges(19, 27.9, 0, 'male', 'yes', 'Southwest'))
