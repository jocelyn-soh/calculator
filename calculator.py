from flask import Flask, render_template, request, jsonify 
import math

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1']) if request.form['num1'] else 0
    num2 = float(request.form['num2']) if request.form['num2'] else 0
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    else: 
        result = num1 - num2
        
    if result >= 1e308:
        return jsonify({'error': 'Result exceeds maximum representable value of 1e308'})
        
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()

