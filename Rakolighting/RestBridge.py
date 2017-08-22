from flask import Flask
import Bridge

app = Flask(__name__)
bridge = Bridge.Bridge()


@app.route("/level/<int:room>/<int:channel>/<int:level>")
def rako(room, channel, level):
    return bridge.level(room, channel, level)
