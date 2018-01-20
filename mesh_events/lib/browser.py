import socket

from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf


class MDNSBrowser(object):

  def __init__(self):
    self.calendar_servers = {}
    self.zeroconf = Zeroconf()
    self.browser = ServiceBrowser(self.zeroconf, "_ics._tcp.local.", handlers=[self._on_service_state_change])

  def _on_service_state_change(self, zeroconf, service_type, name, state_change):
    print("Service %s of type %s state changed: %s" % (name, service_type, state_change))
    if state_change is ServiceStateChange.Added:
      info = zeroconf.get_service_info(service_type, name)
      if info:
        address = socket.inet_ntoa(info.address)
        self.calendar_servers[name] = address
        print(self.calendar_servers)
    elif state_change is ServiceStateChange.Removed:
      del self.calendar_servers[name]

    def get_calendar_servers(self):
      return self.calendar_servers
