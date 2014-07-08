TargetExplorer-querytest
========================

Minimal version of [TargetExplorer](https://github.com/choderalab/TargetExplorer), for developing a simple query method.

TargetExplorer is a database framework and web API, implemented using Python
Flask and SQLAlchemy.

Manifest
--------

* kinome.db - Pre-populated SQLite database
* flaskapp/ - Flask app
  * views.py - Flask methods for responding to HTTP requests
  * models.py - SQLAlchemy ORM data model
* run.py - Runs the query method directly (does not actually run the Flask HTTP server)

To install dependencies using pip:
----------------------------------

`pip install flask`

`pip install flask-sqlalchemy`

Instructions
------------

The aim is to implement a Flask method which takes a query string as input, and
returns a list of matching database entries. SQLAlchemy query syntax will be
used directly in the input query string. The query method must be able to
filter based on columns from a number of (related) tables.

The query method is to be implemented as `query_db`, within flaskapp/views.py

A placeholder method has been set up.

To run the query method (from this directory): `python run.py`
