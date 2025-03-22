# Lab 11 - Qiskit

## Generating API Token
Before using the IBM Quantum Platform, I first had to a create an IBM account [here](https://quantum-computing.ibm.com/). After the account was successfully setup, I had to copy and keep track of the API key I will be using in the python programs.

## Qiskit Installation and Setup
Before being able to use Python to interact with IBM's Quantum Platform, there were a few necessary installations. Qiskit (Quantum Information Software KIT) is a package founded by IBM to develop program that can interact with IBM's quantum computer, or in a simulated environment. The commands I used to install these packages are shown below. 

```
pip install qiskit[visualization]
pip install qiskit-aer
pip install qiskit_ibm_provider
```

To connect my account to this terminal, I ran a short python script from the terminal. Since I was using Git Bash, I had to use the command listed below, rather then just using the python command.

```
winpty python.exe
>> from qiskit_ibm_proviver import IBMProvider
>> IBMProvider.save_account("API_KEY")
>> exit()
```

## Qiskit Terra

The first example program is qiskit_terra_example.py. This file did not initially run, and after research I found that changes have been made to the Qiskit Aer package. This package is now separate from the qiskit package, ```from qiskit import aer``` to ```from qiskit_aer import aer```. Simliarly, the execute function has been replaced with the transpile function, which works in the same manner. After using transpile, I finally had to include a line running the quantum circuit (QC) before I could produce results. Additionally, I imported matplotlib to display a drawing of the QC, which is pictured below. 

![drawing of quantum circuit](https://github.com/user-attachments/assets/a2a591fa-85e0-4834-9513-9930326d57ea)

Before viewing the results of the program, I first tried to figure out how this QC works. In the drawing, there are two qubits, labeled q0 and q1, as well as two classical bits used for measuring. Q0 first goes the Hadamard (H) gate, which takes a qubit in a state of 0 or 1 into a superposition with equal probability of each. Essentially, it makes q0 equally as likely to be a 0 or a 1. After the H gate, q0 and q1 both enter into the controlled x-gate. The Hadamard gate was already hard to understand, and this gate was even less intuitive. The simplest explanation that I could find was that this gate entagles q1 to q0, making q1 match q0's value.

In order to see the results of this program I used the command ```python qiskit_terra_example.py```. 

![terra counts](https://github.com/user-attachments/assets/9818c0ba-0781-4d04-859f-28e565f3429a)

The simulation evualates the QC 1024 times, keeping a count of the measured values of each qubit. Since there is randomness involved in quantum computing, each trial of program produced a different count. However, with the knowledge of how the gates work, this makes sense. Since q1 has to match q0 because they are entangled, there are no counts in the states 01 and 10, since these states would mean q0 and q1 have different values. And, since q0 initially goes through the H gate, it has an equal probability of being 0 and 1, explaining the near 50-50 split in the counts.

## Qiskit Aer

First I had to install a new package to use the backends to simulate a noisy, more realistic simulation. In this case we use the FakeManilla backend, which is included in the qiskit_ibm_runtime. I installed this package using ```pip install qiskit_ibm_runtime``` and included this in the Python script. I also needed to include SamplerV2, which is also in this package. Similar to the previous example, I used matplotlib to generate the image below, showing the quantum circuit.

![aer quantum circuit](https://github.com/user-attachments/assets/d1eb6923-0eae-460b-8c6d-fde6515bee92)

This example is very similar to the previous one, however it involves 3 qubits. The first qubit goes through an H gate, and is then entagled with the 2 other qubits. So based on this, the expected result should be an even split of "000" and "111". Before confirming this with the program, I had to fix a few more issues. I based these changes on the documentation on the [qiskit_ibm_provider package](https://docs.quantum.ibm.com/api/qiskit-ibm-runtime/fake-provider). I used this code in place of the section where the noisy simulation is run, and the results can seen below.

![qiskit_aer_results](https://github.com/user-attachments/assets/f3c9fb77-a29a-4ec4-b765-b634c7be9ab7)
As expected, the ideal counts show an approximately even split between "000" and "111". However, the results from the FakeManilla backend show counts for other results. This showcases the noise found in quantum computers. Qubits are still very unstable and prone to error, and can sometimes produce inaccurate results.

# Qiskit Aqua

Since 2021, the Qiskit Aqua package has been depreciated. However, all of its functions have been moved into other packages. As of now, I am still working on this example program.

---
I pledge my honor that I have abided by the Stevens Honor System - _Ray Ringston_

