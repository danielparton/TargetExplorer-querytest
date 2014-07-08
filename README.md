TargetExplorer-querytest
========================

Minimal Flask/SQLAlchemy app for developing a simple query method

Manifest
--------

* kinome.db - Pre-populated SQLite database
* flaskapp/ - Flask app
  * views.py - Flask methods for responding to HTTP requests
  * models.py - SQLAlchemy ORM data model
* run.py - Runs the query method directly (does not actually run the Flask HTTP server)

To install dependencies:
------------------------

pip install flask

pip install flask-sqlalchemy

Instructions
------------

The query method is to be implemented as query\_db, within flaskapp/views.py

To run the placeholder query method (from this directory):
python run.py
