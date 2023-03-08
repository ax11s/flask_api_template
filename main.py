import random
from flask import Flask, request, jsonify

app = Flask(__name__)


# Define API key
apikey = "testkey"


# Define route and API function
@app.route('/boredom')
def random_string():
    # Api key aunthentiffication
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


# Define route and API function
@app.route('/neverhaveiever')
def neverhaveiever():
    # Api key aunthentiffication
    reckey = request.headers.get('key')
    
    if reckey != apikey:
        return jsonify({'error': 'Invalid API key'}), 401
    

    #getting the string
    with open("neverhaveiever.txt", "r") as file:
        lines = file.readlines()

    index = random.randint(0, len(lines))
    print(index)
    index = index - 1
    random_line = lines[index]

    print(random_line)

    file.close()
    return random_line




if __name__ == '__main__':
    app.run()


