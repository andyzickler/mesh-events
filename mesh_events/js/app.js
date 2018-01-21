import CalendarList from './CalendarList';
import {Card, CardTitle, CardActions, CardHeader, CardText} from 'material-ui/Card';
import React from 'react';
import ReactDOM from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const container = document.getElementById('reactAppContainer');

const App = () => (
  <MuiThemeProvider>
    <div>
      <Card>
        <img src="/static/cal_logo.svg" height="80px" style={{
          float: 'right',
          margin: '7px',
        }}/>
        <CardTitle title="Calendars" subtitle="Share and aggregate calendars" />
        <CardText>
          <CalendarList calendars={JSON.parse(container.getAttribute('calendars'))} />
        </CardText>
      </Card>
      <br />
      <br />
      <Card>
        <CardTitle title="Other Mesh Services" subtitle="Services disocvered using Unglitch Mesh Discovery Protocol" />
        <CardText>
          <em>No other services found</em>
        </CardText>
      </Card>
    </div>
  </MuiThemeProvider>
);

ReactDOM.render(<App/>, container);

