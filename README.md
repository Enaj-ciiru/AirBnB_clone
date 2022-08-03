# Description

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4. create the first abstracted storage engine of the project: File storage.
5. create all unittests to validate all our classes and storage engine

# Description of Commandline Interprator

Our command interpreter looks like a mini shell and allow us manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

# How to start the console

### Execution
Should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Works like this in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220802%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220802T175715Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a4627e137d2061959802431a83fc1d699017a880ce526570d70406bccfcccd70

### Authors
<h3> <a href="https://github.com/Enaj-ciiru">Jane Immaculate Njoroge</a> </h3>
<h3> <a href="https://github.com/WaltTersly">Walter Kifugo Chege</a> </h3>

