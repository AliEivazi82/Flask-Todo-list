from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("localhost", 27017)
db = client['flask_app_db']
todos = db['todos']

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_page():
    all_tasks = todos.find()
    return render_template("index.html", tasks=all_tasks)


@app.route('/', methods=['POST'])
def add_tasks():
    task_title = request.form.get("task_title")
    todos.insert_one({"task":task_title})
    return redirect(url_for("main_page"))

@app.post("/del/<id>")
def delete(id):
    todos.delete_one({"_id":ObjectId(id)})
    return redirect(url_for("main_page"))

if __name__ == "__main__":
    app.run(debug=True)
