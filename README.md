============
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
