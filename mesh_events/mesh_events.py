from datetime import datetime

from flask import Flask, abort, flash, redirect, render_template, request, url_for

import sys
sys.path.insert(0, './lib')
import calendar_store as CalendarStore

app = Flask(__name__)
app.config['DEBUG'] = True

CalendarStore.load_seed_data()


@app.route('/')
def index():
  return render_template('index.html', calendars=CalendarStore.all())

if __name__ == '__main__':
  app.run()
