import json
import requests


class MeshCalendar():
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.content = 'Empty'
    self.selected = True
    self.mine = False

  def id(self):
    return self.name

  def get_content(self):
    if self.mine:
      with open('static/calendar.ics') as c:
        return c.read()
    print(u"http://{}:5000/static/calendar.ics".format(self.address))
    r = requests.get(u"http://{}:5000/static/calendar.ics".format(self.address))
    print(r.status_code)
    if r.status_code == 200:
      self.content = r.text

    return self.content


class MeshCalendarEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, MeshCalendar):
      return {
        'id': o.id(),
        'name': o.name,
        'address': o.address,
        'subscribed': o.subscribed
      }
    return MeshCalendarEncoder(self, o)
