# Lab 7 - ThingSpeak and Google Sheets

## Reviewing and Running ThingSpeak
Since I already had a MathWorks account, I logged in and create a new channel called cpu_loop with fields for cpu_pc and mem_avail_mb. 

First, I copied the neccessary files, thingspeak_cpu_loop.py and thingspeak_feed.py, from the lesson 7 directory.
![copying files](https://github.com/user-attachments/assets/72902351-57b3-41ad-b597-97e525f203e0)

Before running the files I used ```cat thingspeak_cpu_loop.py thingspeak_feed.py``` to inspect them, which can be seen below. The files seem very similar, however, thingspeak_feed.py contains more code dealing with the use of the API key. Both programs measure the CPU utilzation and the available memory and upload them to the API fields every minute.

![cpu_loop cat](https://github.com/user-attachments/assets/98e167cc-6978-40d4-8864-3247e8de90e0)
![image](https://github.com/user-attachments/assets/c49d02eb-8590-4b76-bc6c-4bad6181900a)

To run thingspeak_feed.py I used ```python3 thingspeak_feed.py```, which outputted the measurements every 60 seconds. Note: The API Key seen in the screenshot is no longer being used, I changed it after taking this screenshot. The statistics are then displayed in the ThingSpeak channel and can be seen below.

![program output](https://github.com/user-attachments/assets/3fa46adb-1e68-4a66-beb1-cb5e5fcea880)
![channel stats](https://github.com/user-attachments/assets/139ca5dd-7148-43cd-9558-1bcc2cc68200)
