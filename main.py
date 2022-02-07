# 05 COVID Dashboard

from covid import download_summary, download_confirmed_per_country
# Import the object Flask from the flask module
from flask import Flask
import json

# Import and setup logging
import logging
log_format = "[%(levelname)s] - %(asctime)s : %(message)s in %(module)s:%(lineno)d"
logging.basicConfig(filename='covid.log', format=log_format, level=logging.INFO)


# Create a webserver object called 'COVID Dashboard' and keep track of it in the variable called server
server = Flask('COVID Dashboard')

# Define an HTTP route / to serve the dashboard home web page
@server.route("/")
# Define the function 'index()' and connect it to the route /
def index():
    # Return the string "A nice COVID dashboard."
    return server.send_static_file('index.html')

# Define an HTTP route /summary to serve the summary chart
@server.route("/summary")
# Define the function 'serve_summary()' and connect it to the route /summary
def serve_summary():
    # Load JSON template from summary.json
    json_template = json.load(open("templates/summary.json"))
    # Download summary from the COVID API
    summary_data = download_summary()
    # Add the data to the template
    json_template["data"]["values"] = summary_data["Countries"]
    # Send the chart description to the client
    return json_template

# Define an HTTP route /new to serve the new count worldwide chart
@server.route("/new")
# Define the function 'serve_summary_new()' and connect it to the route /new
def serve_summary_new():
    # Load json template from new.json
    json_template = json.load(open("templates/new.json"))
    # Download summary from the COVID API
    json_data = download_summary()
    # Create an empty list of value to receive filtered and formated data
    values = []
    # For all data in the "Global" structure
    for key in json_data["Global"]:
        # Keep the 'New' entries (skip overall totals)
        if key.startswith("New"):
            # Create a dictionary with 'category' and 'value'
            value = {"category": key, "value": json_data["Global"][key]}
            # Add the dictionary to the list of values
            values.append(value)
    # Add the data to the template
    json_template["data"]["values"] = values
    # Send the chart description to the client
    return json_template

# Define an HTTP route /netherlands to serve the chart of the Netherlands
@server.route("/netherlands")
# Define the function 'serve_netherlands_history()' and connect it to the route /netherlands
def serve_netherlands_history():
    # Load JSON template from history.json
    json_template = json.load(open("templates/history.json"))
    # Download the confirmed cases of the Netherlands from the COVID API
    summary_data = download_confirmed_per_country("netherlands")
    # Add the data (key "data") to the template (key "data" > "values")
    json_template["data"]["values"] = summary_data["data"]
    # Send the chart description to the client
    return json_template

# Start the webserver
server.run('0.0.0.0')