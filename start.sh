#!/bin/sh

export FLASK_APP=mesh_events
export FLASK_DEBUG=1
cd mesh_events
node_modules/webpack/bin/webpack.js --watch &
WEBPACK_PID=$!
python mesh_events.py
kill $WEBPACK_PID
