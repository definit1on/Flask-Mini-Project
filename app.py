from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


todo_list = [
    {'id': 1,
     'name': 'Vasya Pupkin',
     'tasks': [
        'walk the dog',
         'buy coffee'
    ]},
    {'id': 2,
     'name': 'Sveta Pupkina',
     'tasks': [
         'wash the window',
         'make dinner'
     ]},
    {'id': 3,
     'name': 'Petya Pupkin',
     'tasks': [
         'feed the cat',
         'do homework',
         'watch YouTube'
     ]},
]

@app.route("/")
def index():
    return render_template('index.html',
                           todo=todo_list)

@app.route("/member/<int:pk>")
def member_detail(pk):
    for item in todo_list:
        if item['id'] == pk:
            member = item
    return render_template('member_detail.html',
                           member=member)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/add/task", methods=["POST"])
def add_task():
    # print(request.form.POST)
    new_task = request.form.get('task')
    pk = int(request.form.get('pk'))
    for item in todo_list:
        if item['id'] == pk:
            member = item
    member['tasks'].append(new_task)
    return redirect(url_for('member_detail', pk=pk))

if __name__ == '__main__':
    app.run(port=5002, debug=True)