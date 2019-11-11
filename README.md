# AirBnB_clone 
![Flowchart](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191111T225804Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a225dce99c1826cb1a5fa7d023a7b878764ea90414980f4dc59c320fcf420c68)
 Built in python3, this project emulates the functioning of the AirBnB website.
 This version is called The Holberton B&B, and it is a project for [Holberton School Medellín](https://www.holbertonschool.com/co/campus_life/medellin).
 
## Flowchart
We will develop the backend as well as the frontend part of the website. Here is a diagram of the project and a hint of the technologies we used.
 
 ![Flowchart](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191111T225804Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e91604034c2a3d814c60c6702892b540b700456042595b75df8595fedd39bd9e)
 
 ## The Console
 There is a built-in command line interpreter (console) that provides a way to interact with the Storage-engine.
 
 Thru the console is possible to: 
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Getting started

First. Clone this repository in your machine.
```sh
$ https://github.com/carlosz22/AirBnB_clone
```
Go to the repo.

```sh
$ cd AirBnB_clone
```
After that, it is all set to start using the console like this

```sh
$ ./console.py
```

## Usage

After running the last command (./console.py), you will see a prompt.

```sh
(hbnb) 
```

This means, the console is ready to get some commands ;).

### Avaliable Commands
| Command | Arguments | Description |
| ------ | ------ | ------ |
| create | `<class name>` | Creates a new class from the available class-list ||
| show | `<class name> <id>` | Prints the string representation of an instance based on the class name and id. |
| destroy | `<class name> <id>` | Deletes an instance based on the class name and id (save the change into the JSON file). |
| all | `[ <class name>]` | Prints all string representation of all instances based or not on the class name |
| update | `<class name> <id> <attribute name> "<attribute value>"`  | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file |