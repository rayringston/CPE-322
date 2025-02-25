# Lab 5 - Paho-MQT

## Installing Mosquitto
Since my computer is running Windows, I downloaded Mosquitto from the [official website](https://mosquitto.org/download/)

## Testing Mosquitto
On one terminal, I established a subscriber by using the command ```mosquito_sub -h localhost -v -t test/topic```. On another separate terminal I publish a message uusing ```mosquitto_pub -h localhost -t test/topic -m "hello"```. As seen in the image below, the terminal that is the subscriber display the message sent from the publisher.

![subscriber output](https://github.com/user-attachments/assets/32b0d024-ca06-48fe-80a8-20f7aeb3fdda)

## Installing Paho

![installing paho](https://github.com/user-attachments/assets/a08d5c72-4304-461f-8866-8a8b6ab2ec11)

## Paho Test Examples
1. The first test uses ```python3 sub.py``` on one terminal and ```python3 pub.py``` on the other.
   * The output from the subscriber side shows the published message using the Paho topic
   * ![test 1 output](https://github.com/user-attachments/assets/49544d87-6fe7-4ccc-b0f0-f235548deee5)
2. The second examples tests what happens when multiple messages are published using ```python3 sub-multiple.py``` and ```python3 pub-multiple.py``` on each terminal
   * Both messages are recieved by the subscriber and can be seen below
   * ![test 2 output](https://github.com/user-attachments/assets/f7cbcd19-2cf8-4dc2-a9d8-3f9156d3b9e4)
3. The final example has messages being continuously published, using ```python3 subcpu.py``` and ```python3 pubcpu.py```
   * As seen in the images below, each message is timestamped and contains the current CPU utilization of my computer. The publisher and subscriber are able to continuously communicate and transfer data.
   * ![test 3 pub output](https://github.com/user-attachments/assets/f017ea63-fbb7-460d-9d57-08718848a3b2)
   * ![test 3 sub output](https://github.com/user-attachments/assets/8de42b17-47d6-46f1-903c-2c8e430d75c6)

---

I pledge my Honor that I have abided by the Stevens Honor System - _Ray Ringston_
