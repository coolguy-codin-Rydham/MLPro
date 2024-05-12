from flask import Flask, request, jsonify
import pickle
from InferenceAgain import Inference
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



# Load the model and scaler
with open(r"D:\codes\vscode codes\vscode codes\AI\Project\Models\XGBRegressor_r2_0_953_v1.pkl", "rb") as f:
    model = pickle.load(f)

with open(r"D:\codes\vscode codes\vscode codes\AI\Project\Models\sc.pkl", "rb") as f:
    scaler = pickle.load(f)

inference = Inference(model, scaler)

@app.route('/pred', methods=['POST'])
def pred():
    print("method called")
    data = request.json
    prediction = inference.predict(data)
    print(prediction)
    return jsonify({"prediction": prediction})


@app.route('/red', methods=['GET'])
def red():
    data =  {
        "message":"Hello this is an API End Point"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
