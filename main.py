import random
from flask import Flask, request, jsonify

app = Flask(__name__)


apikey = "testkey"


# API function and route
@app.route('/boredom')
def random_string():

    reckey = request.headers.get('key')
    
    if reckey != apikey:
        return jsonify({'error': 'Invalid API key'}), 401
    

    #getting the string
    with open("boredom.txt", "r") as file:
        lines = file.readlines()

    index = random.randint(0, len(lines))
    print(index)
    index = index - 1
    random_line = lines[index]

    print(random_line)

    file.close()
    return random_line


@app.route('/neverhaveiever')
def neverhaveiever():
    reckey = request.headers.get('key')
    
    if reckey != apikey:
        return jsonify({'error': 'Invalid API key'}), 401
    
    with open("neverhaveiever.txt", "r") as file:
        lines = file.readlines()

    index = random.randint(0, len(lines))
    print(index)
    index = index - 1
    random_line = lines[index]

    print(random_line)

    file.close()
    return random_line


# curl -H "key:testkey" http://127.0.0.1:5000/boredom

if __name__ == '__main__':
    app.run()


