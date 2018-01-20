import atexit
from datetime import datetime

from flask import Flask, abort, flash, redirect, render_template, request, url_for

from lib.advertiser import MDNSAdvertiser
import lib.calendar_store as CalendarStore

app = Flask(__name__)
app.config['DEBUG'] = True

CalendarStore.load_seed_data()
advertiser = MDNSAdvertiser()

@app.route('/')
def index():
  return render_template('index.html', calendars=CalendarStore.all(), calendars_json=CalendarStore.all_json())


@atexit.register
def stop_advertiser():
  advertiser.teardown()


if __name__ == '__main__':
  advertiser.setup()
  app.run()
