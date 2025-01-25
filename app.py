from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

dataset_path = 'dataset.xlsx'
dataset = pd.read_excel(dataset_path)

data_path = 'dataset0.xlsx'
data = pd.read_excel(data_path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')


@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    gender = request.form['gender']
    health_issues = request.form.getlist('health_issues')
    phone = request.form['phone']
    weight = request.form['weight']
    height = request.form['height']

    filtered_data = filter_dataset(dataset, age, gender, health_issues)
    if filtered_data.empty:
        return render_template('result.html', error_message="No diet plan found.")

    diet_plan = filtered_data.iloc[0]  # Assuming only one row is filtered
    return render_template('result.html', name=name, email=email, age=age, gender=gender, health_issues=health_issues,
                           phone=phone, weight=weight, height=height,
                           Diet_Morning_Veg=diet_plan['Diet_Morning_Veg'],
                           Diet_Morning_NonVeg=diet_plan['Diet_Morning_NonVeg'],
                           Diet_Afternoon_Veg=diet_plan['Diet_Afternoon_Veg'],
                           Diet_Afternoon_NonVeg=diet_plan['Diet_Afternoon_NonVeg'],
                           Diet_Night_Veg=diet_plan['Diet_Night_Veg'],
                           Diet_Night_NonVeg=diet_plan['Diet_Night_NonVeg'])


@app.route('/process_form1', methods=['POST'])
def process_form1():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    gender = request.form['gender']
    weight = request.form['weight']
    height = request.form['height']
    detail = request.form.getlist('detail')

    filtered = filter_dataset1(data, age, gender, detail)
    if filtered.empty:
        return render_template('result0.html', error_message="No diet plan found.")

    diet_plan = filtered.iloc[0]  # Assuming only one row is filtered
    return render_template('result0.html', name=name, email=email, age=age, gender=gender, weight=weight,
                           height=height, detail=detail,
                           morning_veg_diet=diet_plan['morning_veg_diet'],
                           morning_nonveg_diet=diet_plan['morning_nonveg_diet'],
                           afternoon_veg_diet=diet_plan['afternoon_veg_diet'],
                           afternoon_nonveg_diet=diet_plan['afternoon_nonveg_diet'],
                           night_veg_diet=diet_plan['night_veg_diet'],
                           night_nonveg_diet=diet_plan['night_nonveg_diet'])


def filter_dataset(dataset, age, gender, health_issues):
    age_range = tuple(map(int, age.split('-')))
    filtered_data = dataset[
        (dataset['age'].apply(lambda x: age_range[0] <= int(x.split('-')[0]) <= age_range[1]))
        & (dataset['gender'] == gender)
        & (dataset['health_issue'].isin(health_issues))
        ]
    return filtered_data


def filter_dataset1(data, age, gender, detail):
    age_range = tuple(map(int, age.split('-')))
    filtered = data[
        (data['age'].apply(lambda x: age_range[0] <= int(x.split('-')[0]) <= age_range[1]))
        & (data['gender'] == gender)
        & (data['detail'].isin(detail))
        ]
    return filtered


if __name__ == '__main__':
    app.run(debug=True)
