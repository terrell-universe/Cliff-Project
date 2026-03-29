from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def check_risk():
    # 1. GET DATA FROM THE FORM
    try:
        user_income = float(request.form.get('income'))
        raise_amount = float(request.form.get('raise'))
    except (ValueError, TypeError):
        return "Error: Please enter valid numbers."

    # 2. DEFINE THE LIMITS
    snap_limit = 1696
    medicaid_limit = 1800

    # 3. CALCULATE FUTURE STATE
    new_income = user_income + raise_amount

    # SNAP

    if new_income < snap_limit:
        cliff_value = 'SAFE'
    elif user_income < snap_limit <= new_income:
        cliff_value = 'UNSAFE'
    else:
        cliff_value = 'Already above income limit'

    # MEDICAID

    if new_income < medicaid_limit:
        cliff_valueB = 'SAFE'
    elif user_income < medicaid_limit <= new_income:
        cliff_valueB = 'UNSAFE'
    else:
        cliff_valueB = 'Already above income limit'
    

    result_message = ""  

   
    result_message = f"SNAP Status: {cliff_value} <br> Medicaid Status: {cliff_valueB}"
    
    
    return f"<h1>{result_message}</h1><br><a href='/'>Check Again</a>"


if __name__ == '__main__':
    app.run(debug=True)