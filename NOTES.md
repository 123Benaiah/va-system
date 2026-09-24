# Notes

## Day 1 - MVT
Django uses something called MVT - Model, View, Template. 
The Model is the part that talks to the database and defines what data looks like (like a table with fields).
The view is the logic layer - it takes a web request, decides what to do, grabs data from the model if needed, and then picks a Template to show. 
The template is just the HTML page that gets filled in with data and sent back to the browser. Keeping these three separate makes the code easier to manage because you know where each piece belongs.

## Day 2 - Migrations

A migration is a Python file that describes a change to the database schema,
such as creating a table or adding a column. Django builds it from the models
and then applies it to the database. The database is not edited by hand because
the migration file keeps the schema in sync with the code. This makes changes
recorded, repeatable, and easy to share with other developers.

## Day 3 - View vs Template

A view is Python code that handles a request. It fetches data from the models,
applies logic, and returns a response. A template is an HTML file that defines
how the response looks. The view chooses which template to render and passes
data to it, while the template only handles layout and display. Keeping them
separate means the logic and the presentation can change independently.

## Day 4 - Deploying

Deploying means moving the project from a local machine to a server that is
online, so the app is reachable through a public URL. The code is pushed to
GitHub and then pulled onto the server, which installs the dependencies and
runs the app. Git is used because it keeps the code in one place, tracks every
change, and makes it easy to move the same version from local to server.
