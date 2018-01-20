from .calendar import MeshCalendar

_store = {}

def add(calendar):
  _store[calendar.id()] = calendar

def all():
  return _store.values()

def load_seed_data():
  add(MeshCalendar("James' Work Calendar"))
  add(MeshCalendar("Neighborhood Events"))
