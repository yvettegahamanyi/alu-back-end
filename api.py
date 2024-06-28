from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
todos = [
    {'id': 1, 'task': 'Buy groceries', 'done': False},
    {'id': 2, 'task': 'Learn Flask', 'done': False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = None
    for t in todos:
        if t['id'] == todo_id:
            todo = t
            break
    if todo:
        return jsonify(todo)
    else:
        return jsonify({'error': 'Todo not found'})
    
if __name__ == '__main__':
    app.run(debug=True)
    