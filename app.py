from flask import Flask, jsonify,request, make_response
from models import *

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    t  = Tasks.select()
    selector = []
    for i in range(len(t)):
        selector.append({ 
            'id':str(t[i].id),
            'title':str(t[i].title),
            'description':str(t[i].description),
            'status':str(t[i].done),
            })
    return jsonify(selector)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)

    _title = request.json.get("title")
    _description = request.json.get("Description")

    row = Tasks(
            title= _title,
            description=_description,
            done=False,
    )
    row.save()
    return jsonify({"msg" : "ok"})
  
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tsk = Tasks.get(Tasks.id == task_id).delete_instance()
    return jsonify({'result': True})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tsk = Tasks.get(Tasks.id == task_id)
    tsk.title = request.json.get('title')
    tsk.description = request.json.get('description')
    tsk.done = request.json.get('done')
    tsk.save()
    return jsonify(tsk)