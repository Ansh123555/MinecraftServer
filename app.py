from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Minecraft Server Panel is Running! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
