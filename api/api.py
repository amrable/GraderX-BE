from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/get_results')
def get_current_results():
    path = get_file_path_from_grader()
    return send_file(path, as_attachment=True)

def get_file_path_from_grader():
    return "hi.txt"