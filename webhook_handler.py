from flask import Flask, request
import json
import subprocess

app = Flask(__name__)  # Standard Flask app

@app.route("/", methods=['GET', 'POST'])        # Standard Flask endpoint
def hello_world():
    content_type = request.headers["content_type"]
    event_type = request.headers["X-Github-Event"]
    data = json.loads(request.form.to_dict(flat=True)[
        "payload"]) if content_type == "application/x-www-form-urlencoded" else request.get_json()
    err = None
    if event_type == "push":
        err = on_push(data)

    return "success" if err is None else err


def on_push(data):
    if data["repository"]["id"] == 277559260:
        subprocess.run("chmod +x ./pull.sh", shell=True)
        subprocess.run("chmod +x ./makeapp.sh", shell=True)
        flag = 0
        while (flag < 3):
            if subprocess.call("./pull.sh", shell=True) == 0:
                flag = 69
            else:
                flag += 1
        if flag != 69:
            return "Some error occured"
        subprocess.call("./makeapp.sh", shell=True)
    return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
