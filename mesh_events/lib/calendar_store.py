import json
from .calendar import MeshCalendar, MeshCalendarEncoder

_store = {}

def add(calendar):
  _store[calendar.id()] = calendar

def all():
  return list(_store.values())

def all_json():
  return json.dumps(all(), cls=MeshCalendarEncoder)

def load_seed_data():
  add(MeshCalendar("James' Work Calendar"))
  add(MeshCalendar("Neighborhood Events"))
