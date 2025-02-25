# Lab 2 - Command Line

## hostname
The hostname command displays the name assigned to the computer on the network. Instead of displaying the IP address, it shows a more readable "nickname" for the device.

![hostname output](https://github.com/user-attachments/assets/8c4c0b77-6a78-4f40-970f-001e94b8182f)

## env
The env command list all of the environment variables stored on the computer. Environment variables allow a user to create custom names for certain paths that the computer can easily access. This enables an easier access for programs that need specific files or directories, such as a code editor using a new library.

![env output](https://github.com/user-attachments/assets/fd138fb9-9a29-4231-ae46-6c9bc8c54671)

## ps
The ps command stands for "process status", and displays information regarding the running processes.
- PID: Process ID
- PPID: Parent Process ID
- PGID: Process Group ID
- WINPID: Windows Process ID, this is associated with the information displayed on Task Manager
- TTY: This descibres what terminal the process is running on
- UID: User ID of the user who started the process
- STIME: Start Time
- COMMAND: The actual name of the process
  
![ps output](https://github.com/user-attachments/assets/75b02310-44a1-4505-a0a4-e84dc10aaf26)

## pwd
PWD simply prints the directory that you are currently in

![pwd output](https://github.com/user-attachments/assets/899a2606-b2e0-47e5-947e-8d9b18795b65)


## git clone
This command allows you to create a copy of a GitHub repository from another location. In this example, I created a copy of [Professor Lu's IoT repository](https://github.com/kevinwlu/iot.git).

![git clone output](https://github.com/user-attachments/assets/fe202e3e-b18b-431d-9d7c-590326f213f1)

## cd iot
The cd command stands for "change directory", which allows you to move between directories. The image below shows my directory change from ~ to ~/iot

![image](https://github.com/user-attachments/assets/9b764752-da9a-43a2-b162-e3d5f5531ee1)

## ls
This command prints the contents of the current directory

![ls output](https://github.com/user-attachments/assets/82cf5275-60a5-454f-bfea-c13c8a50e3ca)

## cd
If a specific directory is not including while using cd, it returns the user to their home directory. This image shows my working directory changing from ~/iot back to ~.

![image](https://github.com/user-attachments/assets/0a8d69d9-3487-4fcc-84f5-c656396682d7)

## df
df stands for "disk free", and displays information on all of the connected file systems. It shows information like the system name, used space, and available space.

![df output](https://github.com/user-attachments/assets/9bc35a0a-034c-42cf-a68e-5f310c1cd22f)

## mkdir demo
mkdir create a new directory in your current working directory, in this example called demo.

![mkdir demo output](https://github.com/user-attachments/assets/978a6da4-0db5-4829-acbc-0ad45c22e2ff)

## cd demo
This moves me into the new demo directory

![cd demo output](https://github.com/user-attachments/assets/0c3e5eba-c304-4561-8146-c56f09fc5204)


## nano file
nano allows the user to create and edit text file from the terminal. This created a file named "file", that I wrote text into.

![nano file](https://github.com/user-attachments/assets/5852e45e-eee3-40e6-b17c-9f616167b659)

## cat file
The cat command prints the contents of its input files. The text I wrote during the nano command is now printed back to the screen, and can be seen below.

![cat file output](https://github.com/user-attachments/assets/f95b0bc6-dea7-411d-b17a-169c098f9b38)

## cp file file1
cp is short for copy, and creates a duplicate of a file. This created a copy of file names file1.

![cp proof](https://github.com/user-attachments/assets/2193572a-e711-47be-92bb-e61b5d732d5c)

## mv file file2
mv is short for move, and is used for moving or renaming files. Since the command didn't provide a new directory, it remained in the same location but changed names from file to file2

![mv proof](https://github.com/user-attachments/assets/9f30cbe1-024a-458d-9103-e71d5893ad99)

## rm file2
rm is short for remove, and is uesd for deleting files and directories. As seen below, file2 has been deleted

![rm proof](https://github.com/user-attachments/assets/629fb099-f3ec-4e57-9c28-fc660fb45804)

## clear
clear removes all previous commands from the screen

![clear output](https://github.com/user-attachments/assets/f6f5b14c-ea18-40ee-b162-c3eb14e4d9e7)

## man uname
man is short for manual, and provides detailed information regarding the commands. In order to use this command, you must install the manual database first. Alternatively, I used the command ```bash uname --help``` to learn about the uname command.

![uname --help output](https://github.com/user-attachments/assets/717ffb87-d5f6-427a-bf27-df7342acfbeb)

