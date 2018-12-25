** Item Catalog
                              ******** Hossam sabry ********

*** 

This is the second project for the Udacity Full Stack Nanodegree.
Project Description:-
A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication.
Authenticated users have the ability to post, edit, and delete their own items.

***
This project has one main Python module application.py which runs the Flask application. 
A SQL database is created using the database_setup.py module and you can populate the database 
with test data using fakeitems.py. 
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end 
of the application.


***Dependencies
1.Vagrant
2.Udacity Vagrantfile
3.VirtualBox


*** Usage

1.Install Vagrant & VirtualBox.
2.Clone the Udacity Vagrantfile
3.Go to Vagrant directory and either clone this repo or download and place zip here
Once Vagrant is installed, cd to vagrant/ and run vagrant up && vagrant ssh. 
In the virtual machine, cd to /vagrant/catalog


4.Setup application database python 
`database_setup.py`
5.Insert fake data 
`python fakeitems.py`

6.Then run the application:


`python application.py`


7.After the last command you are able to browse the application at this URL:


`http://localhost:5000/`


