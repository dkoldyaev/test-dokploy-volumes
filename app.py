from flask import Flask
import os

app = Flask(__name__)

FILE_PATH = "/data/secrets/secret.txt"

@app.route('/')
def get_val():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            content = f.read().strip()
        return f"File value: {content}"
    return "No file!", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
