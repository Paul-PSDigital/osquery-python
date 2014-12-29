
# osquery-python

Python bindings for OSQuery

## README

This is the README file for osquery-python

Example Usage:
from osquery import osquery

osquery = osquery()
print osquery.setOutputMode("--json").query("SELECT * from etc_hosts")

## Todo

[ ] Add SWIG Interfaces
[ ] Package
