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

    // Connect web socket
    let socket = new WebSocket("ws://" + location.host + "/calendars.socket");

    let that = this;
    socket.onmessage = function(message){
      let { data } = message
      let calendars = JSON.parse(data);
      that.updateCalendars(calendars);
    }

    this.state = {
      calendars: props.calendars,
      socket: socket,
    };
  }

  handleRowSelection(rows) {
    let { socket } = this.state;

    var selectedCalendars;
    if (rows == "all") {
      selectedCalendars = this.state.calendars;
    } else {
      selectedCalendars = rows.map((rowIndex) => {
        return this.state.calendars[rowIndex];
      });
    }

    let socketCommand = JSON.stringify({
      action: 'set_selected',
      ids: selectedCalendars.map((calendar) => {
        return calendar.id
      })
    });
    socket.send(socketCommand);
  }

  updateCalendars(calendars) {
    this.setState({
      calendars: calendars,
    });
  }

  renderRows() {
    let { calendars } = this.state;

    return calendars.map((calendar, index) => {
      return (
        <TableRow
          key={index}
          selected={calendar.selected}
        >
          <TableRowColumn key="id">
            {calendar.id}
          </TableRowColumn>
          <TableRowColumn>
            {calendar.name}
          </TableRowColumn>
          <TableRowColumn>
            {calendar.address}
          </TableRowColumn>
        </TableRow>
      );
    });
  };

  renderTable() {
    let { handleRowSelection } = this;

    return (
      <Table
        selectable={true}
        multiSelectable={true}
        onRowSelection={handleRowSelection.bind(this)}
      >
        <TableHeader>
          <TableRow>
            <TableHeaderColumn>ID</TableHeaderColumn>
            <TableHeaderColumn>Name</TableHeaderColumn>
            <TableHeaderColumn>Address</TableHeaderColumn>
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
        {this.renderTable()}
      </div>
    );
  }
};

