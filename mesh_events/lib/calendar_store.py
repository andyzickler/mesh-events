from . import Calendar

_store = {}

def add(calendar):
  _store[calendar.testid()] = calendar

def all():
  _store.values()

def load_seed_data():
  add(Calendar("James' Work Calendar"))
  add(Calendar("Neighborhood Events"))
