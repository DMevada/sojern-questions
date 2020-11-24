import flask
from flask import request
from flask import jsonify
import heapq
import math

app = flask.Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/min", methods=['POST'])
def getMin():
    header = request.headers['Content-Type']
    isJSON = request.is_json

    #checks for correct header and if data is in json format
    if header == 'application/json' and isJSON:
        postData = request.get_json()
    else:
        return jsonify(status="error", message="Please send proper headers"), 400

    if not isKeyPresent(postData, "values"):
        return jsonify(status="error", message="values key containing a list of numbers must be present in JSON body"), 400
    values = postData["values"]

    if not isKeyPresent(postData, "quantifier"):
        return jsonify(status="error", message="quantifier key containing a list of numbers must be present in JSON body"), 400
    quantifier = postData["quantifier"]

    if quantifier > len(values):
        return jsonify(status="success", minimum=values), 200

    heap = []
    for i in values:
        heapq.heappush(heap, i)

    result = []
    for i in range(0, quantifier):
        result.append(heapq.heappop(heap))

    return jsonify(status="success", mininum=result), 200

@app.route("/max", methods=["POST"])
def getMax():
    header = request.headers['Content-Type']
    isJSON = request.is_json

    #checks for correct header and if data is in json format
    if header == 'application/json' and isJSON:
        postData = request.get_json()
    else:
        return jsonify(status="error", message="Please send proper headers"), 400

    if not isKeyPresent(postData, "values"):
        return jsonify(status="error", message="values key containing a list of numbers must be present in JSON body"), 400
    values = postData["values"]

    if not isKeyPresent(postData, "quantifier"):
        return jsonify(status="error", message="quantifier key containing a list of numbers must be present in JSON body"), 400
    quantifier = postData["quantifier"]
    
    if quantifier > len(values):
        return jsonify(status="success", minimum=values), 200

    heap = []
    for i in values:
        heapq.heappush(heap, -1 * i)

    result = []
    for i in range(0, quantifier):
        result.append(-1 * heapq.heappop(heap))

    return jsonify(status="success", maximum=result), 200

@app.route("/avg", methods=["POST"])
def getAvg():
    header = request.headers['Content-Type']
    isJSON = request.is_json

    #checks for correct header and if data is in json format
    if header == 'application/json' and isJSON:
        postData = request.get_json()
    else:
        return jsonify(status="error", message="Please send proper headers"), 400

    if not isKeyPresent(postData, "values"):
        return jsonify(status="error", message="values key containing a list of numbers must be present in JSON body"), 400
    values = postData["values"]

    return jsonify(status="success", average=sum(values)/len(values)), 200

@app.route("/median", methods=["POST"])
def getMedian():
    header = request.headers['Content-Type']
    isJSON = request.is_json

    #checks for correct header and if data is in json format
    if header == 'application/json' and isJSON:
        postData = request.get_json()
    else:
        return jsonify(status="error", message="Please send proper headers"), 400

    if not isKeyPresent(postData, "values"):
        return jsonify(status="error", message="values key containing a list of numbers must be present in JSON body"), 400
    values = postData["values"]

    values = sorted(values)
    median = 0

    if len(values) % 2 == 0:
        midValue = values[len(values)//2]
        midValueBefore = values[len(values)//2 - 1]
        median = (midValue + midValueBefore)/2
    else:
        median = values[len(values)//2]
    
    return jsonify(status="success", median=median), 200

@app.route("/percentile", methods=["POST"])
def getPercentile():
    header = request.headers['Content-Type']
    isJSON = request.is_json

    #checks for correct header and if data is in json format
    if header == 'application/json' and isJSON:
        postData = request.get_json()
    else:
        return jsonify(status="error", message="Please send proper headers"), 400

    if not isKeyPresent(postData, "values"):
        return jsonify(status="error", message="values key containing a list of numbers must be present in JSON body"), 400
    values = postData["values"]

    if not isKeyPresent(postData, "quantifier"):
        return jsonify(status="error", message="quantifier key containing a list of numbers must be present in JSON body"), 400
    quantifier = int(postData["quantifier"])
    
    if quantifier > 100 or quantifier < 0:
        return jsonify(status="error", message="percentile quantifier must be an integer value between 0 and 100 inclusive, no decimal values"), 400

    percentile = sorted(values)[int(math.ceil((len(values) * quantifier) / 100)) - 1]

    return jsonify(status="success", percentile=percentile), 200

def isKeyPresent(postData, key):
    if key in postData.keys():
        return True
    return False


if __name__ == "__main__":
        app.run()