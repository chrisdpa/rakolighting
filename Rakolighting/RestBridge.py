from flask import Flask
import Bridge

app = Flask(__name__)
bridge = Bridge.Bridge()


@app.route("/level/<int:room>/<int:channel>/<int:level>")
def rako(room, channel, level):
    return bridge.level(room, channel, level)


@app.route("/fade_down/<int:room>/<int:channel>")
@app.route("/fade_down")
def fade_down(room=0, channel=0):
    return bridge.fade_down(room, channel)


@app.route("/fade_up/<int:room>/<int:channel>")
@app.route("/fade_up")
def fade_up(room=0, channel=0):
    return bridge.fade_up(room, channel)
