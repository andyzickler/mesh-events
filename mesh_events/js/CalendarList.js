import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import React, {Component} from 'react';
import {
  Table,
  TableBody,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';


export default class CalendarList extends Component {

  constructor(props) {
    super(props);
    this.state = {
      calendars: props.calendars,
    };
  }

  componentDidMount() {
    console.log("mounting");
    let socket = new WebSocket("ws://" + location.host + "/calendars.socket");

    socket.onopen = function(){
      console.log("Socket has been opened!");
    }

    let { setState } = this;
    let that = this;
    socket.onmessage = function(message){
      let { data } = message
      let calendars = JSON.parse(data);
      that.updateCalendars(calendars)
    }
  };

  updateCalendars(calendars) {
    this.setState({
      calendars: calendars,
    });
  }

  renderRows() {
    let { calendars } = this.state;
    return calendars.map((calendar, index) => {
      return (
        <TableRow key={index}>
          <TableRowColumn key="id">
            {calendar.id}
          </TableRowColumn>
          <TableRowColumn>
            {calendar.name}
          </TableRowColumn>
          <TableRowColumn>
            fake
          </TableRowColumn>
        </TableRow>
      );
    });
  };

  renderTable() {
    return (
      <Table>
        <TableHeader>
          <TableRow>
            <TableHeaderColumn>ID</TableHeaderColumn>
            <TableHeaderColumn>Name</TableHeaderColumn>
            <TableHeaderColumn>Status</TableHeaderColumn>
          </TableRow>
        </TableHeader>
        <TableBody>
          {this.renderRows()}
        </TableBody>
      </Table>
    );
  };

  render() {
    return (
      <div>
        <h1>Calendars</h1>
        {this.renderTable()}
      </div>
    );
  }
};

