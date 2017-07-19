from flask import Flask
import Bridge

app = Flask(__name__)


@app.route("/level/<int:room>/<int:channel>/<int:level>")
def rako(room, channel, level):
    return Bridge.Bridge().level(room, channel, level)
