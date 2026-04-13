from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "AI Model Running Successfully"
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['number']
    result = data * 2
    return jsonify({'result': result})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)