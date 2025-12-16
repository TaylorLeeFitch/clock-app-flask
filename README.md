# clock-app-flask
Flask app for seeing clock times in 5 random places in the world, includes API Endpoint


## Running Bash script to test clock-api

```
$ bash api-smoke-test.sh
```
returns 
```
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

```
