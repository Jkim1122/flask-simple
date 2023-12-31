# We import the `Flask` and `jsonify` classes from the Flask library.
from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

# Sample student data
students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
    {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
    {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
    {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
    {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
    {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
]
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    old = []
    for stud in students:
        if stud['age'] > 20:
            old.append(stud)
    return jsonify(old)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    young = []
    for stud in students:
        if stud['age'] < 21:
            young.append(stud)
    return jsonify(young)

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    advance = []
    for stud in students:
        if stud['age'] < 21 and stud['grade'] == 'A':
            advance.append(stud)
    return jsonify(advance)

@app.route('/student_names', methods=['GET'])
def get_student_names():
    names = []
    for stud in students:
        names.append({'first_name' : stud['first_name'], 'last_name' : stud['last_name']})
    return jsonify(names)

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    ages = []
    for stud in students:
         student_name = stud['first_name'] + stud['last_name']
         ages.append({'student_name' : student_name, 'age' : stud['age']})
    return jsonify(ages)
    



if __name__ == '__main__':
    app.run(debug=True)
