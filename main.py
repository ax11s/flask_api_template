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
    index = index - 1
    random_line = lines[index]

    print(random_line)

    file.close()


if __name__ == '__main__':
    app.run()