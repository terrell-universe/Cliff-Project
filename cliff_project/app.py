from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = 'dev-secret-key'


@app.route('/', methods=['GET'])
def home():
    result = session.pop('result', None)
    return render_template('index.html', result=result)


@app.route('/', methods=['POST'])
def submit():
    try:
        user_income = float(request.form.get('income'))
        raise_amount = float(request.form.get('raise'))
    except (ValueError, TypeError):
        session['result'] = '<p>Error: Please enter valid numbers.</p>'
        return redirect(url_for('home'))

    snap_limit = 1696
    medicaid_limit = 1800
    new_income = user_income + raise_amount

    if new_income < snap_limit:
        snap_status = 'SAFE'
    elif user_income < snap_limit <= new_income:
        snap_status = 'UNSAFE'
    else:
        snap_status = 'Already above income limit'

    if new_income < medicaid_limit:
        medicaid_status = 'SAFE'
    elif user_income < medicaid_limit <= new_income:
        medicaid_status = 'UNSAFE'
    else:
        medicaid_status = 'Already above income limit'

    session['result'] = (
        f'<div>SNAP Status: {snap_status}</div>'
        f'<div>Medicaid Status: {medicaid_status}</div>'
    )
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)