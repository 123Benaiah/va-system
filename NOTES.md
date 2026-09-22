# Notes

## Day 1 - MVT
Django uses something called MVT - Model, View, Template. 
The Model is the part that talks to the database and defines what data looks like (like a table with fields).
The view is the logic layer - it takes a web request, decides what to do, grabs data from the model if needed, and then picks a Template to show. 
The template is just the HTML page that gets filled in with data and sent back to the browser. Keeping these three separate makes the code easier to manage because you know where each piece belongs.
