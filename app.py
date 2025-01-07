# app.py
from flask import Flask, request, jsonify
from evaluator import prefix_to_postfix

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    expression = data.get('expression')
    
    if not expression:
        return jsonify({'result': 'Expression is required!'}), 400

    try:
        # Convert prefix to postfix
        result = prefix_to_postfix(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)
