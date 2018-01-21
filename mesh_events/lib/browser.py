import socket

from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf
from lib.calendar import MeshCalendar


class MDNSBrowser(object):

  def __init__(self, calendar_store):
    self.calendar_store = calendar_store
    self.zeroconf = Zeroconf()
    self.browser = ServiceBrowser(self.zeroconf, "_ics._tcp.local.", handlers=[self._on_service_state_change])
    self.host_ip = socket.gethostbyname(socket.gethostname())

  def _on_service_state_change(self, zeroconf, service_type, name, state_change):
    print("Service %s of type %s state changed: %s" % (name, service_type, state_change))
    if state_change is ServiceStateChange.Added:
      info = zeroconf.get_service_info(service_type, name)
      if info:
        address = socket.inet_ntoa(info.address)
        self._add_calendar(name, address)
    elif state_change is ServiceStateChange.Removed:
        self._remove_from_store(name)

  def _add_calendar(self, name, address):
    calendar = MeshCalendar(name, address)
    if address == self.host_ip:
      calendar.mine = True
    self.calendar_store.add(calendar)

  def _remove_from_store(self, name):
    self.calendar_store.remove(name)
