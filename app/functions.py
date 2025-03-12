#!/usr/bin/env python3

import os, sys





"""
-- Example code using datetime object to generate current time as formatted string
cur_time_string = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

-- Example code using datetime library to convert formatted string back into datetime object
datetime_object = datetime.datetime.strptime(cur_time_string, "%m/%d/%Y %H:%M:%S")

-- Example code to add 'User' record to DB 
# with scheduler.app.app_context() is required if working from schedular endpoint 
with app.app_context()
    try:
        new_user = User(username='test', email='test@some.domain', password=generate_password_hash('test'))
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print(f"Error occurred trying to add record to db: {e.message}")
    
        
-- Example code to update 'User' record to DB 
# with scheduler.app.app_context() is required if working from schedular endpoint 
with app.app_context()
    cur_user = Users.query.filter_by(id=1).first()      ## This assumes the user exists, there should be check that cur_user != None
    cur_user.email = 'new_email@some_domain
    cur_user.username = "Batman"
    db.session.commit()

"""