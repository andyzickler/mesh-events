import json
from random import random
from .calendar import MeshCalendar, MeshCalendarEncoder


class CalendarStore:
  FIRST_NAMES = ['Sophia', 'Jackson', 'Emma', 'Aiden', 'Olivia', 'Lucas', 'Ava', 'Liam', 'Mia', 'Noah', 'Isabella',
                 'Ethan', 'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Grayson',
                 'Layla', 'Jacob', 'Amelia', 'Michael', 'Emily', 'Benjamin', 'Madelyn', 'Carter', 'Aubrey', 'James',
                 'Adalyn', 'Jayden', 'Madison', 'Logan', 'Chloe', 'Alexander', 'Harper', 'Caleb', 'Abigail', 'Ryan',
                 'Aaliyah', 'Luke', 'Avery', 'Daniel', 'Evelyn', 'Jack', 'Kaylee', 'William', 'Ella', 'Owen', 'Ellie',
                 'Gabriel', 'Scarlett', 'Matthew', 'Arianna', 'Connor', 'Hailey', 'Jayce', 'Nora', 'Isaac', 'Addison',
                 'Sebastian', 'Brooklyn', 'Henry', 'Hannah', 'Muhammad', 'Mila', 'Cameron', 'Leah', 'Wyatt',
                 'Elizabeth', 'Dylan', 'Sarah', 'Nathan', 'Eliana', 'Nicholas', 'Mackenzie', 'Julian', 'Peyton', 'Eli',
                 'Maria', 'Levi', 'Grace', 'Isaiah', 'Adeline', 'Landon', 'Elena', 'David', 'Anna', 'Christian',
                 'Victoria', 'Andrew', 'Camilla', 'Brayden', 'Lillian', 'John', 'Natalie', 'Lincoln']
  _web_sockets = []
  _store = {}

  def add(self, calendar):
    self._store[calendar.id()] = calendar
    self.broadcast_changes()

  def add_ws(self, ws):
    self._web_sockets.append(ws)

  def get(self, id):
    return _store[id]

  def broadcast_changes(self):
    for ws in self._web_sockets:
      if ws.closed:
        continue
      try:
        ws.send(self.all_json())
      # HACK: multi-level hack. Should use proper error class (import :() and message comparison should use constants
      except Exception as e:
        if str(e) == "Socket is dead":
          self.remove_ws(ws)
        else:
          raise e

  def remove_ws(self, ws):
    if ws in self._web_sockets:
      self._web_sockets.remove(ws)

  def remove(self, calendar_id):
    del self._store[calendar_id]
    self.broadcast_changes()

  def all(self):
    return list(self._store.values())

  def all_json(self):
    return json.dumps(self.all(), cls=MeshCalendarEncoder)

  def set_selected(self, selected_calendar_ids):
    for calendar in self.all():
      calendar.selected = calendar.id() in selected_calendar_ids

  def generate_calendar(self):
    first_name = self.FIRST_NAMES[round(random() * len(self.FIRST_NAMES))]
    calendar = MeshCalendar(first_name + "'s Calendar")
    self.add(calendar)

  def load_seed_data(self):
    self.generate_calendar()
    self.generate_calendar()
