# Overview
This is a super simple proof of concept decentralized calendar sharing + aggregation service for mesh networks. It also includes a simple service discovery protocol for mesh network services using multicast DNS (udp, bonjour) that could be used to allow users and other services to discover services available on mesh network.

Built as part of [{UNGLITCH} Net Neutrality Hackathon + Creative Showcase](https://www.eventbrite.com/e/unglitch-net-neutrality-hackathon-creative-showcase-registration-41476382978#).

Technology used:
- Python, Flask, Websockets
- React, React Material-UI Components

# Installation
```
# setup a virtual env
source venv/bin/activate
pip install -r requirements.txt
cd mesh_events
npm install
```

# Usage
```
./start
```

Place example calendar files to share in mesh_events/static/

Run on other computers on the same subnet to see the decentralized / discovery functionality.

Visit [http://localhost:5000](http://localhost:5000), select the calendar(s) you would like to subscribe to, add the aggregate URL to your favorite calendar program. It will dynamically update as shared calendars change and other nodes become available.

# TODO
- UI to add your calendar(s) arbitrarily
- Pull locally available calendars automatically?
- Expand to generalized discovery service with specific calendar section
  - Add a TXT key to the DNS responses that designate they are discoverable by our service
