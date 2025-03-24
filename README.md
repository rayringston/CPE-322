# CPE 322: Engineering Design VI
GitHub Repository for CPE 322\
[Syllabus Link](https://sit.instructure.com/courses/77142)\
[Group Website](https://sites.google.com/stevens.edu/cpe322-group/home)

---

# Table of Contents
1. [Lab Assignments](#lab-assignments)
2. [Portfolio](#portfolio)
3. [Useful Resources](#useful-resources)
   
---

# Lab Assignments
0. [Lab 0 - Create GitHub Repository](https://github.com/rayringston/CPE-322/edit/main/README.md) *(Completed 1/27/2025)*
   * Create GitHub Repo for this course
1. [Lab 1 - GHDL and GTKWave](Lab%201/lab1.md) *(Completed 2/3/2025)*
   * Use GHDL and GTKWave to create output waveforms of the example files
   * Tested the Half Adder file and the 4 to 1 Multiplexer
2. [Lab 2 - Command Line](Lab%202/README.md) *(Completed 2/24/2025)*
   * Tested the functions of various terminal commands
3. [Lab 3 - Python](Lab%203/README.md) *(Completed 2/25/2025)*
   * Installed various Python packages and ran example scripts to see their capabilities
4. [Lab 4 - Django and Flask](Lab%204/README.md) *(Completed 2/25/2025)*
   * Used Django, Django REST, and Flask in Pyhton to host Wepages
5. [Lab 5 - Paho-MQTT](Lab%205/README.md) *(Completed 2/25/2025)*
   * Used Mosquitto and Paho-MQTT to transfer messages over a network
6. [Lab 6 - Node.js and Pystache](Lab%206/README.md) *(Completed 2/25/2025)*
   * Used Node.js to run a webpage that reacts to changes on the client side
   * Also used Pystache to create templates to parse and render input data
7. [Lab 7 - ThingSpeak and Google Sheets](Lab%207/README.md) *(Completed 2/25/2025)*
   * Implemented ThingSpeak and Google APIs to continuously log and monitor data over the internet
8. [Lab 8 - Data Analysis](Lab%208/README.md) *(Completed 3/3/2025)*
   * Analyzed system data from lab 7 using various python packages, like matplotlib, scipy, scikit-learn, etc.
9. [Lab 9 - YANG](Lab%209/README.md) *(Completed 3/3/2025)*
   * Used Pyang to convert between .yang, .yin, and .uml data schemes
   * Used PlantUML to generate diagrams from UML files
10. [Lab 10 - Blockchain](Lab%2010/README.md) *(Completed 3/3/2025)*
    * Used Python to run a simple blockchain server, allowing user to mine through an internet connection
    * Ran a more complicated system, that provided users a form to fill out attaching their names to their transactions
11. [Lab 11 - Qiskit](Lab%2011/README.md) *(Completed 3/22/2025)*
    * Used the Qiskit library to simulate a quantum computer circuit
    * Current programs are depreciated, functional versions are attached
    
--- 

# Portfolio
**About Me**
- Raymond Ringston
- Computer Engineering Major
- Junior at Stevens Institute of Technology

**Current Courses**
- CPE 322: Design VI
- CPE 462: Introduction to Image Processing and Coding
- CPE 345: Modeling and Simulation
- CPE 487: Design of Digital Systems
- IDE 399: Project Managements and Engineering Economics
- BT 244: Microeconomics

**Progamming Languages**
- Python
- C++
- ARMv7
- VHDL
- Arduino
- MATLAB

```c++
Mat invert(Mat image) {
   Mat temp = image.clone();
   for (int i = 0; i < image.rows; i++) {
      for (int j = 0; j < image.cols; j++) {
         temp.at<Vec3b>(i, j)[0] = 255 - image.at<Vec3b>(i,j)[0];
         temp.at<Vec3b>(i, j)[1] = 255 - image.at<Vec3b>(i, j)[1];
         temp.at<Vec3b>(i, j)[2] = 255 - image.at<Vec3b>(i, j)[2];
     }
   }
   return temp;
}
```
> Short sample of code written in C++ using the OpenCV2 library\
> This function takes an image and inverts the colors
---

# Useful Resources
- Markdown Cheatsheet
   - ![Cheatsheet showing the various details in markdown](https://github.com/user-attachments/assets/53080796-c119-4275-80ef-203584271114)

 
---
  
