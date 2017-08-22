#!/usr/bin/python
import socket


class Bridge(object):
    """Connectionless control of a rako bridge using UDP"""
    def __init__(self, port=9761):
        super(Bridge, self).__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # bind to the default ip address using a system provided ephemeral port
        self._socket.bind(('', 0))
        self._port = port
        self._socket.sendto('D', ('255.255.255.255', self._port))
        self._socket.sendto('D', ('255.255.255.255', self._port))
        resp = self._socket.recvfrom(256)
        print(resp)
        if resp:
            _, self._address = resp
        else:
            raise Exception('Cannot find a rakobrige')

    def __send(self, command):
        checksum = 256
        for b in command[1:]:
            checksum = checksum - b

        command.append(checksum % 256)
        self._socket.sendto("".join(map(chr, command)), self._address)
        data, __ = self._socket.recvfrom(128)
        return "{}".format(data)

    def level(self, room, channel, level):
        """Set the level for room and channel.
        All values are unsigned chars, eg 0-255"""
        return self.__send([0x52, 7, 0, room % 256, channel % 256, 12, level % 256, 0])

    def fade_up(self, room, channel):
        """Fade up to full-on"""
        return self.__send([0x52, 5, 0, room % 256, channel % 256, 1, 0])

    def fade_down(self, room, channel):
        """ Fade down to full-off"""
        return self.__send([0x52, 5, 0, room % 256, channel % 256, 2, 0])
