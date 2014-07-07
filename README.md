TargetExplorer-QLtest
=====================

Minimal Flask/SQLAlchemy app for developing a simple query language

Manifest
--------

* kinome.db - Pre-populated SQLite database
* flaskapp/ - Flask app
  * views.py - Flask methods for responding to HTTP requests
  * models.py - SQLAlchemy data models
* run.py - Runs the Flask app server at localhost:5000

Installing dependencies
-----------------------

pip install flask
pip install flask-sqlalchemy

Instructions
------------

To run the Flask app (from this directory):
python run.py

To send an HTTP query to the Flask app:
curl localhost:5000'/search?query=family=CK1'
