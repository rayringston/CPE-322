# Lab 8 - Data Analysis

## Overview
This lab introduces various methods of data analysis, using the system data obtained in lab 7. By using various python packages, like numpy, scipy, and matplotlib, these programs anaylzed the input data and visualized with numerous plots. After, the programs used the Keras package to produce a linear regression model to predict future values.

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

![google sheets charts](https://github.com/user-attachments/assets/30384c47-2b36-45e4-8c81-5c9e40c96d90)


First I moved to my directory called demo, and copied the necessary python files using ```cp ~/iot/*8/plt_final.py . ``` and ```cp ~/iot/*8/plt_cv2.py . ```. 

In plt_final.py, I first needed to change the name of the spreadsheet to allow the program to access the correct csv file, which is shown below. Similarly, I edited the plot titles and axis labels to display 'Memory Available GB' instead of 'Temperature C'.

![plt_final.py changes](https://github.com/user-attachments/assets/9ea19653-a188-4ca5-bb97-81ef2b28e2d7)

Similarly, for plt_cv2.py, the changes necessary for function can be seen below. I also updated the plot titles and axes to match the data in my spreadsheet. The updated files that were used for this lab can be found in this repository.

![plt_cv2.py changes](https://github.com/user-attachments/assets/434d8a13-d51d-4fec-a62d-257995e8b708)

After running these two files, you can see the outputted charts below. The first program, plt_final.py, produced various charts comparing the two variables CPU usage, and memory available. The second program, plt_cv2.py, used scikit-learn to produce a linear regression model for the available memory data. However, this data is not as linear as temperature data, so these regression models do not produce very accurate results.

![plt_final 4/6](https://github.com/user-attachments/assets/147c7fe1-9d03-4c8e-8e69-18a8ba03f4b0)

![plt_final 6/6](https://github.com/user-attachments/assets/579f9b36-c852-4082-9ece-e7cabf9b2d80)

![plt_cv2 output](https://github.com/user-attachments/assets/dca4f3e1-efd2-4b52-a50d-22294c4f25d2)


As an experiment, I modified plt_cv2.py to print the R sqaured value of the data set. These modifications are shown below. The resulting R squared value for this dataset was 0.5188724002732852, which doesn't support a very strong correlation. However, this value was obtained after producing 300 samples of data. When running this program with only 50 samples, I obtained a negative R squared value. So, with more samples, the correlation of the model significantly increased.

![plt_cv2 modifications](https://github.com/user-attachments/assets/c4f6cc6e-63d5-4d72-abfd-9684b7c2dab6)

---

I pledge my honor that I have abided by the Stevnes Honor System - _Ray Ringston_

