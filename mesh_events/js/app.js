import CalendarList from './CalendarList';
import React from 'react';
import ReactDOM from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const container = document.getElementById('reactAppContainer');

const App = () => (
  <MuiThemeProvider>
    <CalendarList calendars={JSON.parse(container.getAttribute('calendars'))} />
  </MuiThemeProvider>
);

ReactDOM.render(<App/>, container);

