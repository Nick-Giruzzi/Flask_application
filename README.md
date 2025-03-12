# Flask_application

## Description

This code will handle running a bare-bones Flask Website. It does not contain endpoints or any real functionality. It only sets up two base blueprints (main and auth) where main is the `unauthorized` blueprint that contains routes users would interact with before doing any kind of login and `auth` would contain routes that would be visible and usable by 
user after they complete their authentication.

The website is pre-configured to run with a SQLite DB, and if there isnt one it will create the DB based on the class configuration in the `models.py` to create the tables.
