# python-coding-exercise

Python coding exercise for ACME employees payment calculation example.

This example is a demonstration of my coding expertise as a Python Developer. The code is based on the requirements defined in the email submitted before.


The code is organized in 3 main classes:

Parser: Input text parsing process
Shift: Information about shifts and schedules defined in the initial parameters
Payments: For calculation of the payments of each employee, based in shifts and hour costs

Also there is included a a function in the helpers.py file, which is used in the different classes to parse the time strings and convert it to time in seconds. Also in the file params.py there are set the variables needed to run the program, which setups the schedules, and costs per hour depending on the day and time.

# Program execution

As defined in the requirement, the code must include a text file with data to be processed, where each line corresponds to a employee work record similar to this:

```
PATRICIO=MO07:00-09:00,WE12:00-15:00,SU14:00-16:00
```

To run the program, you can clone this repository and use the following command from the src/ folder:

```
python main.py data.txt
```

# Unit Tests

To run the defined tests (using pytest) use the following command inside de src/ folder

```
pytest test
```

# Coding considerations

- The Parser class, analizes that the codes for the days of the workday are the same as the defined in the params file, and that the arrive and leave time for the shift are correct. If is there any inconsistence in the day code or the times (ex. leave time sooner than arrive time), the record is marked as invalid, returning an error message when that line is processed, instead of the calculated payment
- The payment is rounded to a integer value, but arrive and leave times for each record, can be set to minute intervals (internally all the code uses time in seconds)
- The params.py file allows to modify the parameters of the application, which are used in the program classes internally. You can modify costs and time ranges for normal and weekend days and schedules
- Due to time calculation, there was an adjustment made to the schedules defined in the requirement, because as example, starting a shift at 9:01, there will be a inconsistency in the data input when the real shift starts at 9:00, because of the time rounding to minutes and it can lead to miscalculations in the payment total

