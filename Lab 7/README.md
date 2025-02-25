# Lab 7 - ThingSpeak and Google Sheets

## Overview
This lab shows two method of logging data, using MathWorks' ThingSpeak and Google APIs. ThingSpeak uses the IoT to update charts, while the Google APIs allow you to directly send incoming data to a Google Sheet.

## Reviewing and Running ThingSpeak
Since I already had a MathWorks account, I logged in and create a new channel called cpu_loop with fields for cpu_pc and mem_avail_mb. 

First, I copied the neccessary files, thingspeak_cpu_loop.py and thingspeak_feed.py, from the lesson 7 directory.
![copying files](https://github.com/user-attachments/assets/72902351-57b3-41ad-b597-97e525f203e0)

Before running the files I used ```cat thingspeak_cpu_loop.py thingspeak_feed.py``` to inspect them, which can be seen below. The files seem very similar, however, thingspeak_feed.py contains more code dealing with the use of the API key. Both programs measure the CPU utilzation and the available memory and upload them to the API fields every minute.

![cpu_loop cat](https://github.com/user-attachments/assets/98e167cc-6978-40d4-8864-3247e8de90e0)\
![image](https://github.com/user-attachments/assets/c49d02eb-8590-4b76-bc6c-4bad6181900a)

To run thingspeak_feed.py I used ```python3 thingspeak_feed.py```, which outputted the measurements every 60 seconds. Note: The API Key seen in the screenshot is no longer being used, I changed it after taking this screenshot. The statistics are then displayed in the ThingSpeak channel and can be seen below.

![program output](https://github.com/user-attachments/assets/3fa46adb-1e68-4a66-beb1-cb5e5fcea880)\
![channel stats](https://github.com/user-attachments/assets/139ca5dd-7148-43cd-9558-1bcc2cc68200)

## Google Sheets
First, I created a new project called cpudata on the [Google Cloud Platform IAM](https://console.cloud.google.com/projectselector2/iam-admin/iam). I enabled the Google Drive and Google Sheets API for this project. Then I create a service account key and saved the json file containing this information.

Next, I installed the necessary Python packages using ```pip install -U gspread oauth2user```

![package installs](https://github.com/user-attachments/assets/b444d590-dabd-43d5-ad82-9e1f8c346003)

I used the following commands to copy the neccesary files to my working directory. After, I moved the previously downloaded API key to the same directory using ```mv ~/Downloads/xxxx.json . ```, replacing the X's with the name of my file.

![files copying](https://github.com/user-attachments/assets/bd60afab-cc89-4bcb-b4fa-a9c3678666eb)

I then created a new Google sheet named cpudata, including my API service account as an editor. I deleted all rows except for the first, and made Date / Time, CPU Usage %, and Memory Available GB as the headers. 

![google sheet setup](https://github.com/user-attachments/assets/ac97868a-28c8-4c02-82af-34c0e4fcfdc6)

Before the program can be run I first had to edit the following lines in cpu_spreadsheet.py to match my spreadsheet and API information, using ```nano cpu_spreadsheet.py```.

![cpu_spreadsheet changes](https://github.com/user-attachments/assets/d890816a-6239-4288-87d5-6235783b3d1b)

After running the program, using ```python3 cpu_spreadsheet.py```, the CPU utilization and available memory are logged into the Google sheet, roughly every 10 seconds.

![spreadsheet updated](https://github.com/user-attachments/assets/d0d69875-0575-4736-a5a7-c909e0991bb9)

---
I pledge my Honor that I have abided by the Stevens Honor System - _Ray Ringston_
