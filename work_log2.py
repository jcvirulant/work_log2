#! usr/bin/jeffreycovington/work_log2

"""
Work Log with Database Project

Date: 3/1/17
Author: Jeffrey Covington

Description: This App is intended to be used as a work log to track Employees
and their tasks that correspond to specific dates and durations. These
tasks can be searched by any parameter including Employee Name, Task name,
Date, Duration, or simply across all content.

The tasks may also be scrolled through, edited, and deleted from a SQlite DB
using the Peewee ORM.

"""

import datetime
import os
import sys


from peewee import *


class App:
    """The Work Log with Database project for Unit 4"""

    def __init__(self):
        """Create and Connect Database if it does not already exist
            connect database if already exists"""

    def menu(self):
        """Menu to Add and Search Entries and Quit the App"""

    def clear(self):
        """Clears the screen"""

    def quit(self):
        """Quits the Instance"""

    def add_entry(self):
        """Add an Entry"""

    def edit_entry(self):
        """Edit an Entry"""

    def delete_entry(self):
        """Delete an Entry"""

    def search_entry(self, search_query):
        """Search an Entry"""

    def search_date(self):
        """Search by Date MM/DD/YYYY"""

    def search_time(self):
        """Search by Duration HH:MM"""

    def search_name(self):
        """Search by Task Name"""

    def search_notes(self):
        """Search within Notes"""

    def search_employee(self):
        """Search by Employee Name"""

    def print_record(self):
        """Prints one record at a Time"""

    def print_all_records(self):
        """Prints all records in table format"""

    def set_employee(self):
        """Select an Employee name from existing Database"""

    def create_employee(self):
        """Create new Employee"""
        self.employee = Employee()
