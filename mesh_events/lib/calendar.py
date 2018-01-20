import json

class MeshCalendar():

  def __init__(self, name):
    self.name = name

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
