from flask import Flask, render_template, request, redirect
from flask.blueprints import Blueprint

app = Flask(__name__)
tasks = []

tasks_bp = Blueprint('tasks_bp', __name__)

@tasks_bp.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@tasks_bp.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect('/')


app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    app.run(debug=True)
