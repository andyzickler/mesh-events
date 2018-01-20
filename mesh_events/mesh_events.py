import atexit
import os
from datetime import datetime

from flask import Flask, abort, jsonify, flash, redirect, render_template, request, url_for
from flask_sockets import Sockets

from lib.advertiser import MDNSAdvertiser
from lib.browser import MDNSBrowser
from lib.calendar_store import CalendarStore

import time

app = Flask(__name__)
sockets = Sockets(app)

app.config['DEBUG'] = True

calendar_store = CalendarStore()

calendar_store.load_seed_data()
# This is a hack, we're at a hackathon
if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
  advertiser = MDNSAdvertiser()
  advertiser.setup()
  browser = MDNSBrowser()


@app.route('/')
def index():
  return render_template('index.html', calendars=calendar_store.all(), calendars_json=calendar_store.all_json())

@app.route('/calendars.json')
def calendars_json():
  return calendar_store.all_json()

@sockets.route('/calendars.socket')
def calendars_socket(ws):
  change_number = -1
  while not ws.closed:
    # current_change_number = calendar_store.change_number()
    # if change_number < current_change_number:
    #   ws.send(calendar_store.all_json())
    #   change_number = current_change_number
    # time.sleep(5)

    current_change_number = calendar_store.change_number()
    if change_number < current_change_number:
      ws.send(calendar_store.all_json())
      change_number = current_change_number

    # message = ws.receive()
    # ws.send(message)

@app.route('/generate-calendar')
def generate_calendar():
  return calendar_store.generate_calendar()



@atexit.register
def stop_advertiser():
  advertiser.teardown()


if __name__ == '__main__':
  # app.run()
  from gevent import pywsgi
  from geventwebsocket.handler import WebSocketHandler
  server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
  server.serve_forever()
