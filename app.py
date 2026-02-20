import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    # Render provides PORT as an environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
