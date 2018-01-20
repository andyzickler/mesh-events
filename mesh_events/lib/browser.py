import socket

from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf


class MDNSBrowser(object):
  def __init__(self):
    self.zeroconf = Zeroconf()
    self.browser = ServiceBrowser(self.zeroconf, "_ics._tcp.local.", handlers=[self._on_service_state_change])

  def _on_service_state_change(self, zeroconf, service_type, name, state_change):
    print("Service %s of type %s state changed: %s" % (name, service_type, state_change))

    if state_change is ServiceStateChange.Added:
      info = zeroconf.get_service_info(service_type, name)
      if info:
        print("  Address: %s:%d" % (socket.inet_ntoa(info.address), info.port))
        print("  Weight: %d, priority: %d" % (info.weight, info.priority))
        print("  Server: %s" % (info.server,))
        if info.properties:
          print("  Properties are:")
          for key, value in info.properties.items():
            print("    %s: %s" % (key, value))
        else:
            print("  No properties")
      else:
          print("  No info")
      print('\n')
