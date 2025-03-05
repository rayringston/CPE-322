# Lab 9 - YANG

## Installations
The required python packages for this lab were Pyang and PlantUML. Pyang is a tool for creating data schemes, which organize data into a consistent manner. Pyang also supports conversions between various data types, like .yin and .uml. PlantUML primarily handles the latter, and is used to create system diagrams from UML files. The commands below were used to install these packages.

```
pip install pyang
pip install plantuml
```
## Yang
To begin, I created a new directory called Lab 9 and copied the necessary YANG file to this directory using ```cp ~/iot/lesson9/intrusiondetection.yang . ```. Displaying this file using the cat command resulted in the following output.

![yang file output](https://github.com/user-attachments/assets/30350959-f494-4d0c-8fb2-0860b5611370)


Then I used ```pyang -f yin -o intrusiondetection.yin``` to convert the YANG file into a YIN file. The contents of this format is displayed below.

![yin file output](https://github.com/user-attachments/assets/4c3c4d74-9b8a-4857-8c24-1c6eeeaddf17)

Similarly, to convert the YANG file into a UML format, I used ```pyang -f uml -o intrusiondetections.uml --uml-no=stereotypes,annotation,typedef```.

![uml file output](https://github.com/user-attachments/assets/0a842e81-2c06-400b-839f-38d449838a0e)

Finally, I used PlantUML to create a diagram from this .uml file, with the command ```python -m plantuml intrusiondetection.uml```. The resulting diagram can be seen below, which matches the data found in the three previous files.

![intrusiondetection](https://github.com/user-attachments/assets/7a31e153-c932-4fce-9579-1bac05bc10a3)

---

I pledge my honor that I have abided by the Stevnes Honor System - _Ray Ringston_
