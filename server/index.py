import os
from flask import Flask, send_file, redirect


STATIC_FOLDER_NAME = "dist"
IS_PRODUCTION = os.environ.get("MODE") == "production"
PORT = os.environ.get("SERVER_PORT")

app = Flask(__name__, static_url_path="", static_folder=STATIC_FOLDER_NAME)

@app.route("/")
def index():
    if (IS_PRODUCTION):
        return send_file(f"{STATIC_FOLDER_NAME}/index.html")
    return redirect("http://localhost:3000")
        


@app.route("/api/auth/is-authenticated")
def is_authenticated():
    # TODO: do authentication
    return {
        "authenticated": True,
        "user": {
            "name": "DEV"
        }
    }

if __name__ == "__main__":
    if (IS_PRODUCTION):
        from waitress import serve
        serve(app, host="0.0.0.0", port=PORT)
    else:
        print(f">>> {PORT}")
        app.run(debug=True, port=PORT)