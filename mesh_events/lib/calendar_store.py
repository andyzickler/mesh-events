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
  _store = {}
  _change_number = 0

  def add(self, calendar):
    self._store[calendar.id()] = calendar
    self._change_number += 1

  def all(self):
    return list(self._store.values())

  def all_json(self):
    return json.dumps(self.all(), cls=MeshCalendarEncoder)

  def change_number(self):
    return self._change_number

  def generate_calendar(self):
    first_name = self.FIRST_NAMES[round(random() * len(self.FIRST_NAMES))]
    calendar = MeshCalendar(first_name + "'s Calendar")
    self.add(calendar)

  def load_seed_data(self):
    self.generate_calendar()
    self.generate_calendar()
