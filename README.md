# go

##Overview
GoTo is a custom URL shortener that encourages elimination of downtime in thinking about and typing long urls that are frequented by the user. This is done by a script that modifies /etc/hosts and gives it a new name given other than localhost. A homebrew formula moves the codebase to /usr/local/Cellar and installs all the dependencies. The script then starts the server.

##Motivation
To be able to quickly navigate to my favorite songs, go to certain github pages and documentation, message the people I actively talk to the most, go to the homepage of my current course and section, etc.


##Installation
1. brew tap biancasubion/tap
2. brew install goto
3. sudo me < name_root >

##Example
I install goto, and name the root page 'go'.

I can now open go/ in my web browser and see the GoTo interface.

The url I want to shorten contains a pdf version of The Adventures Of Sherlock Holmes. The url is 'http://people.maths.ox.ac.uk/moulton/documents/The_Adventures_of_Sherlock_Holmes.pdf'. I enter it into the form, then add an alias 'sh'.

Now I will be able to type in go/sh on my web browser and it will direct me to 'http://people.maths.ox.ac.uk/moulton/documents/The_Adventures_of_Sherlock_Holmes.pdf'.

##Built With
* [Flask](http://flask.pocoo.org) - The web framework used
* [SQLite3] (https://www.sqlite.org) - The database used
* [Homebrew] (http://brew.sh) - The package manager used to package project

![Alt Text](http://g.recordit.co/QH3crhGrKP.gif)
