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
0. [Lab 0](https://github.com/rayringston/CPE-322/edit/main/README.md) *(Completed 1/27/2025)*
   * Create GitHub Repo for this course
1. [Lab 1](Lab%201/lab1.md) *(Completed 2/3/2025)*
   * Use GHDL and GTKWave to create output waveforms of the example files
   * Tested the Half Adder file and the 4 to 1 Multiplexer
2. [Lab 2](Lab%202/README.md) *(Completed 2/24/2025)*
   * Tested the functions of various terminal commands
3. [Lab 3](Lab%203/README.md) *(Completed 2/25/2025)*
   * Installed various Python packages and ran example scripts to see their capabilities
4. [Lab 4](Lab%204/README.md) *(Completed 2/25/2025)*
   * Used Django, Django REST, and Flask in Pyhton to host Wepages
5. Lab 5
6. Lab 6
7. Lab 7
8. Lab 8
9. Lab 9
10. Lab 10
    
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
  
