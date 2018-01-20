import json


class MeshCalendar():
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def id(self):
    return self.name


class MeshCalendarEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, MeshCalendar):
      return {
        'id': o.id(),
        'name': o.name,
      }
    return MeshCalendarEncoder(self, o)
