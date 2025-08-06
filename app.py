from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    projects = [
        {"name": "Project One", "desc": "Description of project one.", "link": "#"},
        {"name": "Project Two", "desc": "Description of project two.", "link": "#"},
        # Add more projects as needed
    ]
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
