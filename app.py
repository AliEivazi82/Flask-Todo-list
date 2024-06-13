from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client['flask_app_db']
todos = db['todos']

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def test():
    if request.method == "POST":
        task_title = request.form.get("task_title")
        todos.insert_one({"task":task_title})
    all_tasks = todos.find()
    return render_template("index.html", tasks=all_tasks)

if __name__ == "__main__":
    app.run(debug=True)
