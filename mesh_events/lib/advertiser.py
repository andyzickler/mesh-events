import socket

from zeroconf import ServiceInfo, Zeroconf

PORTNUMBER = 80


class MDNSAdvertiser(object):
  def __init__(self):
    self.zeroconf = Zeroconf()

  def setup(self):
    desc = {}

    service_name = u"{}._ics._tcp.local.".format(socket.gethostname().split('.local')[0])
    host_name = u"{}.".format(socket.gethostname())
    host_ip = socket.gethostbyname(socket.gethostname())
    try:
      host_ip_pton = socket.inet_pton(socket.AF_INET, host_ip)
    except socket.error:
      host_ip_pton = socket.inet_pton(socket.AF_INET6, host_ip)

    self.info = ServiceInfo("_ics._tcp.local.",
                            service_name,
                            host_ip_pton, PORTNUMBER, 0, 0,
                            desc, host_name)

    self.zeroconf.register_service(self.info)

  def teardown(self):
    self.zeroconf.unregister_service(self.info)
    self.zeroconf.close()
