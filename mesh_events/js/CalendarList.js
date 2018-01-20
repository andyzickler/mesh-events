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

  renderRows() {
    return this.props.calendars.map((calendar, index) => {
      return (
        <TableRow id="{index}">
          <TableRowColumn>
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

