#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9
# 参考文档： http://www.pythondoc.com/flask/quickstart.html


from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
tasks = []

# curl --location --request POST 'localhost:8383/api/task' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "id":"12",
#     "info":"test"
# }' 
@app.route('/api/task', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})

# curl --location --request GET 'localhost:8383/api/task?id=12'
@app.route('/api/task', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        print(len(tasks))
        task = filter(lambda t: int(t['id']) == int(task_id), tasks)
        # print('task:'+ task)
        return jsonify(list(task)) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)
