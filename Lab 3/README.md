# Lab 3 - Python

## Overview
The purpose of this lab is to show the capabilities of various Python packages. 

## Required Python Packages
- [jdcal](https://pypi.org/project/jdcal/)
  - This package is used for converting between Gregorian and Julian calendar dates
- [astral](https://pypi.org/project/astral/)
  - Astral provides calucations for various astrological properties: moon phase, sunrise and sunset times, solar elevation, etc.
- [geopy](https://geopy.readthedocs.io/en/stable/)
  - Provides APIs for various gelocation services, like Google Maps
- [pytz](https://pypi.org/project/pytz/)
  - Calcuates conversions between time zones
- [psutil](https://pypi.org/project/psutil/)
  - Provides information regarding running processes, as well as system utilization statistics

## Setup
Before running the provided examples, you must first enter the correct directory. These lines change directory to the IoT directory, and then to the lesson3 directory. Sytnax for running the example scripts can be found at the bottom, using the approriate file names and inputs.
```console
cd ~\iot
cd *3

python3 julian.py
```
Documentation for installing the necessary GitHub repository can be found in [Lab 2](Lab%202\README.md)

## julian.py
This program converts the current date, which uses the Gregorian calendar, into dates using the Julian and Modified Julian calendars

![julian.py output](https://github.com/user-attachments/assets/79b246dd-33ac-44ff-bb50-7d751e3367eb)

## date_example.py
Prints out the current date, as well as the time since classes began and until they end.

![date_example.py output](https://github.com/user-attachments/assets/dfac7513-6c49-4c03-89d5-7e9b23d025f6)

## datetime_example.py
Prints the date and time repeatedlty, accurate to one thousandth of a millisecond.

![datetime_example.py output](https://github.com/user-attachments/assets/5bc1f34c-5e65-4e8c-827f-efcb7fede490)

## time_example.py
Continuously prints out the date and time every 10 seconds.

![time_example.py output](https://github.com/user-attachments/assets/d3ba1c4e-ad51-4c9e-9717-76fadf82c365)

## sun.py "New York"
Prints out the times of dawn, sunrise, noon, sunset, and dusk for New York. Various major cities also work, including Chicago, London, Cairo, Moscow, and many others.

![sun.py output](https://github.com/user-attachments/assets/823ef8ef-e802-4aba-9a5d-21cd4cda3a45)

## moon.py
Iterates through the next 30 days, and prints the corresponding moon phase for each day.

![moon.py output](https://github.com/user-attachments/assets/e7d4e685-84b3-473c-930b-80a329bc8b70)

## coordinates.py "Samuel C. Williams Library"
Prints the coordinates of the Samuel C. Williams Library

![coordinates.py output](https://github.com/user-attachments/assets/14522cd6-0cdf-45ec-a85c-93a95fccb7d5)

## address.py "40.74480675, -74.02532861159351"
Takes the given coordinates and returns the corresponding address.

![address.py output](https://github.com/user-attachments/assets/77157d76-9cc3-4feb-a734-ce1f8c4d437a)

## cpu.py
Prints the number of physical cores and logical CPUs on this computer, as well as the utilization of each one.

![cpu.py output](https://github.com/user-attachments/assets/0b0653e2-3b43-45cd-850b-503395963b6a)

## battery.py
Displays information regarding the battery of this computer, including percent charge, remaining time, and charging state.

![battery.py output](https://github.com/user-attachments/assets/ab13b618-63a4-4dbb-926a-794d801addd7)

## documentstats.py document.txt
Calculates the 10 most common words found in a text file, as well as their frequencies.

![documentstats.py output](https://github.com/user-attachments/assets/2575d16a-8683-497e-9a32-b0e45ae89c0e)

