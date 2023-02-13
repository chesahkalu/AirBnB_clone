# AirBnB Clone :city_sunrise:
The AirBnb clone is a simple copy of the AirBnB website. It is a complete web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## 1st - The console :trident:
The console is a command line interpreter that will take in commands used to manage various data and objects
on the storeage engine for the backend part of the website. It should be able to ;

- manage and manipulate data models and object (create, update, destroy, etc) objects
- retrieve, store and persist objects to a file (JSON file)
- operate on objects  (count, compute stats, etc...)
- Update attributes of an object

### Data diagram  :beginner:  
![My Image](back_tools/data_map.jpeg)

### To start and use the console:
* Clone this repo: `git clone "https://github.com/chesahkalu/AirBnB_clone.git"`
* Enter AirBnb_clone directory: `cd AirBnB_clone`
* To Run the console(interactively): enter `./console.py`
	- A prompt `(hbnb)` is displayed for input, then enter command. Example::memo:
		- (hbnb) `show <user>` : Prints the string representation of an instance based on the class name and id.
		- (hbnb) `EOF` : exits console
		- (hbnb) `create <class>` : Create an object (prints its id)
		- (hbnb) `all` or `all <class>` : Show all objects, or all instances of a class
	
* To Run hbnb(non-interactively): `echo "<command>" | ./console.py`. Example::memo:
	- `echo "help" | ./console.py`
		- It shows the list of commands available. If you include a command you want help on,
		the output is more verbose and restricted to details of that command, when available.
	- `echo "count place" | ./console.py`
		- Retrieves the number of instances of a given class : place
