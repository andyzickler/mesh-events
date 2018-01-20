#!/usr/bin/env python3

""" Example of announcing a service (in this case, a fake HTTP server) """

import logging
import socket
import sys
from time import sleep

from zeroconf import ServiceInfo, Zeroconf

PORTNUMBER = 8080

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) > 1:
        assert sys.argv[1:] == ['--debug']
        logging.getLogger('zeroconf').setLevel(logging.DEBUG)

    desc = {}

    service_name = u"{}._ics._tcp.local.".format(socket.gethostname().split('.local')[0])
    host_name = u"{}.".format(socket.gethostname())

    info = ServiceInfo("_ics._tcp.local.",
                       service_name,
                       socket.inet_aton("127.0.0.1"), PORTNUMBER, 0, 0,
                       desc)

    zeroconf = Zeroconf()
    print("Registration of a service, press Ctrl-C to exit...")
    zeroconf.register_service(info)
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(info)
        zeroconf.close()
