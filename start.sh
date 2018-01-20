#!/bin/sh

export FLASK_APP=mesh_events
export FLASK_DEBUG=1
cd mesh_events
python mesh_events.py
