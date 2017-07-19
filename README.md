Rakolighting
============

Control rako lighting via a network using a bridge.

The simplest example is to set room 0, channel 0, to level 10.
(Using Room 0, channel 0 will set all the lights to the level)
```
import Rakolighting
br = Rakolighting.Bridge()
br.level(0,0,10)
```

RestBridge
----------

Also added a super simple example of calling the Bridge from a RESTful web service.
start up a web server on listening on port 5000 (the default flask port)
```
$ FLASK_APP=Rakolighting/RestBridge.py flask run --host=0.0.0.0

* Serving Flask app "Rakolighting.RestBridge"
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Using the same room and channel as above set the level by entering the following URL into your browse:

`http://localhost:5000/level/0/0/150`
