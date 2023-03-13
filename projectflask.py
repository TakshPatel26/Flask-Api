from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'name': u'Hetal',
        'contact': u'9979898905',
        'done':False
    },
     {
        'id':2,
        'name': u'Jatin',
        'contact': u'9979898906',
        'done':False
    }
]
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the Name and Number"
        },404)
    task={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False 
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"Task Added Succesfully!"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
            "data":tasks
        })
if (__name__== "__main__"):
    app.run(debug=True)