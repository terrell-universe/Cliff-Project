from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        try:
            user_income = float(request.form.get('income'))
            raise_amount = float(request.form.get('raise'))
        except (ValueError, TypeError):
            result = '<p>Error: Please enter valid numbers.</p>'
            return render_template('index.html', result=result)

        snap_limit = 1696
        medicaid_limit = 1800
        new_income = user_income + raise_amount

        if new_income < snap_limit:
            snap_status = 'SAFE'
        elif user_income < snap_limit <= new_income:
            snap_status = 'AT RISK'
        else:
            snap_status = 'Already above income limit'

        if new_income < medicaid_limit:
            medicaid_status = 'SAFE'
        elif user_income < medicaid_limit <= new_income:
            medicaid_status = 'AT RISK'
        else:
            medicaid_status = 'Already above income limit'

        result = (
            f'<div>SNAP Status: {snap_status}</div>'
            f'<div>Medicaid Status: {medicaid_status}</div>'
        )

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)