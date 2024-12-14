from flask import Flask, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def guesstimation():
    time = datetime.now()
    min = random.randint(0,10)
    sec = random.randint(0,59)
    if random.randint(0,1) == 1:
        min = (-1)*min
    if random.randint(0,1) == 1:
        sec = (-1)*sec

    new_time = time + timedelta(minutes=min,seconds=sec)

    return str(new_time)

@app.route('/api/get_time', methods=['GET'])
def get_items():
    guess = guesstimation().split()[1][:8]

    return "Your shrimp whispers: \"It's about: "+ guess + "\""

if __name__ == '__main__':
    app.run(debug=True)
