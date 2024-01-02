from flask import Flask, render_template, request, redirect
from models import db, StudentModel
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/setup')
def create_table():
    with app.app_context():
        db.create_all()
    return redirect('/')


@app.route('/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        student = StudentModel(name=name, email=email, gender=gender)
        db.session.add(student)
        db.session.commit()
        return redirect('/')


@app.route('/<int:id>/delete')
def delete_item(id):
    student = StudentModel.query.filter_by(id=id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
    return redirect('/')

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_item(id):
    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('update.html', student=student)
    if request.method =='POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.gender = request.form['gender']
        db.session.add(student)
        db.session.commit()
        return redirect('/')


@app.route('/')
def hello_world():
    students = StudentModel.query.all()
    return render_template('index.html', students=students)


if __name__ == "__main__":
    app.run(debug=True)