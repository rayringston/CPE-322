# Lab 8 - Data Analysis

## Overview
This lab introduces various methods of data analysis 

Note: get more data and update pics

## Installations
To install the necessary python pacakges, I used the command ```pip install -U numpy scipy scikit-learn matplotlib pandas keras```. Since tensorflow 
did not install properly I instead had to install a docker desktop and install the tensorflow image there. The command I used are listed below, and more detailed instructions can be found [here.](https://github.com/kevinwlu/iot/tree/master/lesson8#on-windows-with-wsl-open-an-ubuntu-terminal-and-install-python-packages-as-follows)

```console
$docker pull tensorflow/tensorflow
$docker run -it tensorflow/tensorflow bash
  #apt update
  #apt full-upgrade
  #apt install git-all
  #git clone https://github.com/kevinwlu/iot.git
  #pip install keras
  #cd iot/lesson8
  #python keras_diabetes.py
  #python keras_first_network.py
  #exit
```

For these two test programs, keras_diabetes.py and keras_first_network.py respectively, the outputs displayed in the terminal can be seen below.
![keras_diabetes output](https://github.com/user-attachments/assets/b7ecb11e-d46d-4702-ba9f-9df0234e3690)

![keras_first_network output](https://github.com/user-attachments/assets/6aa12452-9e17-4e71-91be-b2f2ef319466)

## Data Anaylsis
Since I used cpu_spreadsheet.py in the previous lab, I did not have the temperature data in my Google Sheet. Instead I used the available memory for my anaylsis, and the charts on my Google Sheet are shown below. 

![google sheets charts](https://github.com/user-attachments/assets/5bf73d80-b60f-4ee4-8b6d-678256638a77)

First I moved to my directory called demo, and copied the necessary python files using ```cp ~/iot/*8/plt_final.py . ``` and ```cp ~/iot/*8/plt_cv2.py . ```. 

In plt_final.py, I first needed to change the name of the spreadsheet to allow the program to access the correct csv file, which is shown below. Similarly, I edited the plot titles and axis labels to display 'Memory Available GB' instead of 'Temperature C'.

![plt_final.py changes](https://github.com/user-attachments/assets/9ea19653-a188-4ca5-bb97-81ef2b28e2d7)

Similarly, for plt_cv2.py, the changes necessary for function can be seen below. I also updated the plot titles and axes to match the data in my spreadsheet.

![plt_cv2.py changes](https://github.com/user-attachments/assets/434d8a13-d51d-4fec-a62d-257995e8b708)

After running these two files, you can see the outputted charts below. The first program, plt_final.py, produced various charts comparing the two variables CPU usage, and memory available. The second program, plt_cv2.py, used scikit-learn to produce a linear regression model for the available memory data. However, this data is not as linear as temperature data, so these regression models do not produce very accurate results.

![plt_final.py 4/6](https://github.com/user-attachments/assets/d88db452-8ad0-4bf4-8b64-208f778fbea6)\
![plt_final.py 6/6](https://github.com/user-attachments/assets/9ad95c0e-dab4-4137-84dd-e9e8eb0ecc64)

![plt_cv2.py](https://github.com/user-attachments/assets/5754af4f-99bd-49fb-917d-e99608220e6e)

As an experiment, I modified plt_cv2.py to print the R sqaured value of the data set. These modifications are shown below. The resulting R squared value for this dataset was -0.4190340357860467, which indicates a very poor fit. If an R squared value is negative, it means that the produced linear regression model is worse at predicting the data than a horizontal line. Since the memory available data is not linear, a linear trendline will not produce accurate results.

![plt_cv2 modifications](https://github.com/user-attachments/assets/c4f6cc6e-63d5-4d72-abfd-9684b7c2dab6)

---

I pledge my honor that I have abided by the Stevnes Honor System - _Ray Ringston_

