from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])

    sum_result = add(num1, num2)
    difference_result = subtract(num1, num2)
    product_result = multiply(num1, num2)
    quotient_result = divide(num1, num2)

    return render_template('result.html', num1=num1, num2=num2, sum_result=sum_result, difference_result=difference_result, product_result=product_result, quotient_result=quotient_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
