# Components
calendar server
- python
- serves iCalendar file
  - later, serves it from a live source

aggregator (server)
- uses mdns to discover calendars being offered
- concatenates them
- makes concatenated file available (also via mdns?)
- combine with the calendar server

aggregate client
- discover aggregator server
- pulls aggregated calendar file
- react frontend served from local aggregator server

user experience
- user installs the server (git clone + python)
  - package into a binary / one click install script?
- user visits localhost:OURPORT
- subscribes to calendars by generating URLs

