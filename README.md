# trainscheduler

The service manages the schedules of different trains that run through a specific station. The service runs in Python 3.9. Start the service after setting the PythonPATH variable in the shell and run the server using:

```bash
python app.py
```

The service supports two Requests:
<ol>

<li>'/add': This is a POST request and accepts JSON data. The data is expected to be a list of dictionaries. Each dictionary has two keys: </li>
    <ol>
        <li> 'name': Accepts a string value of the name of the arriving train. </li>
        <li> 'time': Accepts a list of times when the train is scheduled to arrive. Time is accepted in 12 hour format. (HH:MM AM/PM) </li>
    </ol>

Example:
```json
[
    {
        "name": "104t",
        "time": ["12:31 AM", "12:00 AM", "7:00 AM"]
    },
    {
        "name": "fr34",
        "time": ["07:00 AM"]
    }
]
```

<li>'/fetch': This is a GET request and expects a 'time' as an input argument to fetch the next time multiple trains will arrive at the station. Similar to the previous request, time is accepted in 12 hour format. (HH:MM AM/PM) </li>

</ol>
