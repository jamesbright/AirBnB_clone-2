# Web Framework developed using flask

# Tasks covered
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

if python file creates a flask server covering a specified task. below is some instruction on example files

## Write a script that starts a Flask web application:
 - [0-hello_route](0-hello_route.py)
   - web application listening on 0.0.0.0, port 5000
   - Routes:
     - ```/``` :display “Hello HBNB!”
     - uses the option strict_slashes=False in your route definition

 - [1-hbnb_route](1-hbnb_route.py)
   - web application listening on 0.0.0.0, port 5000
   - Routes:
     - ```/``` : display “Hello HBNB!”
     - ```/hbnb``` : display “HBNB”
