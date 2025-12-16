# exercise:
# add another route called greeting()
# when users visit /greeting , it returns a greeting

## minimal flask all from the docs
# RUN THIS O

# importing Flask from the flask module
from flask import Flask
import random as rn
import pytz
from datetime import datetime as dt

# instantiating a flask app
# __name__ is by default __main__, it is a python built-in constant that tells us the module we are running from
#

GREETINGS = ["Hello", "Good Day", "Good Night", "Welcome!"]
FAREWELLS = ["Goodbye", "See you Later", "Adios"]

app = Flask(__name__)

# HELPER FUNCTIONS

def get_rand_idx(list_):
    """
    Helper function to randomly select index 
    """

    # get the random idx of the passed in list 
    rand_idx = rn.randint(0, len(list_) - 1)

    # return selected entry 
    return list_[rand_idx]

def get_tzs(list_, n=5):
    """
    Docstring for get_tzs
    
    :param list_: list of timezones
    :param n: 
    -> 

    {
  "timezones": [
    {
      "Asia/Chungking": "03:37 AM"
    },
    {
      "Asia/Brunei": "03:37 AM"
    },
    {
      "America/New_York": "02:37 PM"
    },
    {
      "Africa/Johannesburg": "09:37 PM"
    },
    {
      "Atlantic/St_Helena": "07:37 PM"
    }
  ]
}

    """

    res = {'timezones': []}

    # select 5 random timezones 
    five_tzs = rn.sample(pytz.all_timezones, k=5)
    
    # make time strings from timezones. 
    for tz_ in five_tzs:
        
        # make tz object
        tz_s = pytz.timezone(tz_)

        # generate time stamp
        ts_ = dt.now(tz_s)

        # format it
        ts_formatted = ts_.strftime("%I:%M %p")

        # make dictionary for timezone entry
        entry_ = {tz_: ts_formatted}  

        # add entry to timezones dictionary
        res['timezones'].append(entry_)
    
    return res 
    




# creating a home route that returns "Hello World"
@app.route("/") # decorater -> route
def hello_world():
    """
    When I visit the home route,
    this string is returned
    """
    return "<p>Hello, World!</p>"


@app.route('/welcome')
def welcome():
    """
    returns a welcome string when visiting the website
    """
    return "<p> Welcome, to my website </p>"


# add another greeting app 
@app.route("/greeting")
def greeting():
    """
    When I visit the greeting route, a new greeting is displayed
    """ 
    # randomly select a greeting  
    greet_ = get_rand_idx(GREETINGS)
    # return this wrapped in HTML to the user 
    return f"<h2> {greet_} </h2>"


@app.route("/farewell")
def farewell():
    """
    Docstring for farewell
    """
    
    fare_ =  greet_ = get_rand_idx(FAREWELLS)
    return f"<h5>{fare_}</h5>" 

@app.route("/time")
def time():
    """
    Docstring for /time route
    returns times for 5 different time zones
    """ 

    res_ =str()

    # select first 5
    # five_tzs = pytz.all_timezones[:5]

    all_tzs = pytz.all_timezones
    sel_tzs = get_tzs(all_tzs)
    # select 5 random timezones 
    
    
    # make time strings from timezones. 
    for tz_ in sel_tzs['timezones']:

        # get dict key and value using deconstruction

        k, v = list(tz_.items())[0]     
        # build string 
        res_ += f"<h3>Timezone: {k} {v}</h3>"
        res_ += "\n" # add new line 

    return res_


@app.route("/clock-api") 
def clock_api():

    # return dictionary (rendered as JSON in the browser)
    all_tzs = pytz.all_timezones
    return get_tzs(all_tzs)

    


# run the flask app
app.run(host="0.0.0.0", debug=True)