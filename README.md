# AirBnB_clone_v2
AirBnB_clone_v2

[![CodeStyle](https://github.com/B3zaleel/AirBnB_clone_v2/actions/workflows/codestyle.yml/badge.svg)]

## Description

## :page_facing_up: This project is thinking as a whole for a software developer, to learn and become a full-stack developer, gluing alltogether the infrastructure of the Airbnb from back to front, including databases, static and dynamic content, web frameworks, APIs, and web infrastructure.

- MySQL
    > *Group project* *Python* *OOP* *Back-end* *SQL* *MySQL* *ORM* *SQLAlchemy*
- Web Framework
    > *Python* *Back-end* *Webserver* *Flask*

### How To Use

1. First clone this repository.

2. Once the repository is cloned locate the "[console.py](console.py)" file and run it as follows:
   ```powershell
   ➜  AirBnB_clone_v2 git:(master) ✗ ./console.py
   ```

4. When this command is run the following prompt should appear:
   ```
   (hbnb)
   ```

5. This prompt designates that you are in the "HBnB" console. There are a variety of commands available within the console program.

## Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

## Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

 #### Create
  `create <class name>`
  Ex:
  `create BaseModel`

  #### Show
  `show <class name> <object id>`
  Ex:
  `show User my_id`

  #### Destroy
  `destroy <class name> <object id>`
  Ex:
  `destroy Place my_place_id`

  #### All
  `all` or `all <class name>`
  Ex:
  `all` or `all State`

  #### Quit
  `quit` or `EOF

 #### Help
  `help` or `help <command>`
  Ex:
  `help` or `help quit`

## Alternate Syntax
Additionally the console supports 
- ##### `<class name>.<command>(<parameters>)` syntax.
  **Ex:** `City.show(my_city_id)`
- #### Named Parameters
  ##### `<command> <class name> (<named_parameters>)` syntax.
  **Ex:** `create Amenity name="WiFi"`


**NOTE:** Before you push any commit, please run the script `./test.bash` to ensure that no tests are failing and your code complies with this project's styling standard.
