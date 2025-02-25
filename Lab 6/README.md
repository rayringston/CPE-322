# Lab 6 - Node.js and Pystache

## Installing Node.js
To intstall node.js for Windows, I downloaded it directly from the [Node JS website](https://nodejs.org/en/download/). The following commands show the current version of Node and npm, the package manager for node. Since the versions are displayed, Node was installed properly. The final command prints a list of options for Node, which I cut out for the sake of readability.

![node versions](https://github.com/user-attachments/assets/7abbe566-bf9e-4985-9661-821a964627b5)

## Running Examples
Since the examples are all in the lesson6 directory, I first used ```cd ~/iot/lesson6``` to access them.

1. The first example is a simple program displaying "hello world" onto the webpage. I ran the script using ```node hello-world.js```
   * ![example 1 output](https://github.com/user-attachments/assets/3eef49fe-c89f-4316-a1c9-0bce78348050)

2. The second example is similar to the first, but shows a reaction on the server side everytime the user refreshes the page. This was run using ```node hello.js```
   * ![example 2 output](https://github.com/user-attachments/assets/a4a7cfcf-0d0e-48f0-ac35-5ca0f0715f39)

3. The final example changes output based on the number of times the user refreshes the page. On the server side, the number of times the page has been refreshed is outputted. I ran this program using ```node http.js```. After further experimentation, I found that the number of refreshes persists even after the Node program has been closed. The number refreshes is stored separately in a file name test.txt.
   * ![example 3 output](https://github.com/user-attachments/assets/726b4c76-09bb-4a27-9e3a-7053c564f04f)


The following image shows the server outputs for each of the example programs. 
![server response](https://github.com/user-attachments/assets/5abe3869-3ad5-4098-980f-d7235736368a)

## Installing Pystache
