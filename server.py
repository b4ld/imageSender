#!flask/bin/python
import base64
from flask import Flask, jsonify
import asyncio


app = Flask(__name__)

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]


#Send image in STRING from an byte array "str"
@app.route('/image', methods=['GET'])
def get_image():
    with open("_images/img1.png", "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
    image = [
        {
            "base64": str.decode("utf-8"),
            "name":"First image",
            "description":"This is an image in Base 64"
        }
    ]
    return jsonify({'image': image})

# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     task = {
#         'id': tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)

#DO THE ML HERE, MUST WAIT SYNC CALL

# async def g():
#     # Pause here and come back to g() when f() is ready
#     r = await f()
#     return r

#     return jsonify({'task': task}), 201


# pip3 install --upgrade pip3 aiohttp aiofiles












#if __name__ == '__main__':
app.run(debug=True)