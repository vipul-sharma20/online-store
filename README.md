online-store
============

REST API built in Django/Python for managing products of an online store
live demo at: [https://pure-caverns-3351.herokuapp.com/](https://pure-caverns-3351.herokuapp.com/)
Make requests on this link, scroll to bottom for more details on the live demo.

How to run?
------------
* `git clone git@github.com:vipul-sharma20/online-store.git`
* `cd online-store`
* `sudo pip install virtualenv`
     * Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already.
     * If you don't have pip installed, visit here to see steps to install virtualenv: [https://virtualenv.readthedocs.org/en/latest/installation.html](https://virtualenv.readthedocs.org/en/latest/installation.html)
* `virtualenv store`
* `source store/bin/activate`
* `pip install -r requirements.txt` (wait till the requirements are installed)
* `python manage.py syncdb`
     * It will prompt to create a new user type "yes" and add give a username, email and password. This will be one of the user which we can use to try our API.
* (Optional but recommended) Load database with some initial data as fixtures (these are files inside app/fixtures:
     * `python manage.py loaddata users` 
        * will load 2 dummy users with usernames: _bruce_, _alfred_ and password: _testpass_
     * `python manage.py loaddata products` (will load a product list)
* `python manage.py runserver` This will run the application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Test
----
* Test the code by `python manage.py test`
* Tests are written in `app/tests.py`
* You can also change the verbosity of the test output using `-v`
    * `python manage.py test -v3` will give the most verbose output of the tests _(other options: v0, v1, v2)_


API Requests
------------
We can make GET, POST, PUT, DELETE requests using httpie which would be already installed if the requirements installation process was successful.

Example: a simple request using httpie `http http://127.0.0.1:8000/`

### Authentication ###
This API supports basic(username:password) authentication and a token based authentication.

* Basic authentication using httpie: `http -a bruce:testpass http://127.0.0.1:8000/`

* Token based authentication using httpie: `http http://127.0.0.1:8000/ 'Authorization: Token <token>'`

Take a look at the authtoken_token table in the DB with `select * from authtoken_token;`, you should see all the entries of the users with their auth token. You can use this for token based authentication.

In this project GET, POST, PUT, DELETE requests require authentication.

### GET (Show All) ###
Making a request using any of these two methods will give a complete list of products

* `http -a bruce:testpass GET http://127.0.0.1:8000/products/`

suppose the token for user _bruce_ is `c13a415a575338f7384d248934ad5e31ab957ab3` _(check your authtoken_token table)_

* `http GET http://127.0.0.1:8000/products/ 'Authorization: Token c13a415a575338f7384d248934ad5e31ab957ab3'`

Example:

    [
        {
            "category": "Home Decor",
            "description": "Scaled building",
            "id": 3,
            "image": "",
            "name": "Wayne Manor",
            "owner": "alfred",
            "price": 100
        },
        {
            "category": "Automobile",
            "description": "Black airplane, can easily manoeuvre",
            "id": 2,
            "image": "",
            "name": "Bat",
            "owner": "bruce",
            "price": 100
        },
        {
            "category": "Automobile",
            "description": "Black Batmobile",
            "id": 1,
            "image": "",
            "name": "Bat Mobile",
            "owner": "bruce",
            "price": 200
        }
    ]

### POST (Create) ###
Adding a new item:
* `http -a alfred:testpass POST http://127.0.0.1:8000/products/ name="product1" price=200`

OR
* `http POST http://127.0.0.1:8000/products/ name="product1" price=200 'Authorization: Token c13a415a575338f7384d248934ad5e31ab957ab3'`

### PUT (Update) ###
Update an existing item:
* `http -a bruce:testpass PUT http://127.0.0.1:8000/products/2/ name="UpdatedProduct" price=200`

OR
* `http PUT http://127.0.0.1:8000/products/2/ name="UpdatedProduct" price=200 'Authorization: Token c13a415a575338f7384d248934ad5e31ab957ab3'`

if the user is authenticated and is the owner of the product entry, then it will successfully update the item details otherwise not.

### DELETE (Remove) ###
Remove an item:
* `http -a alfred:testpass DELETE http://127.0.0.1:8000/products/1/`

OR
* `http DELETE http://127.0.0.1:8000/products/1/ 'Authorization: Token c13a415a575338f7384d248934ad5e31ab957ab3'`

if the user is authenticated and is the owner of the product entry, then it will successfully remove the item otherwise not.

### GET (Search) ###
Search an item using query parameter `q`
* `http -a alfred:testpass GET http://127.0.0.1:8000/products/?q="bat"`

OR

* `http GET 127.0.0.1:8000/products/?q="bat" 'Authorization: Token c13a415a575338f7384d248934ad5e31ab957ab3'`

This will match the query string with the name of the products and return appropriate result
Example:

    [
        {
            "category": "Automobile",
            "description": "Black airplane, can easily manoeuvre",
            "id": 2,
            "image": "",
            "name": "Bat",
            "owner": "bruce",
            "price": 100
        },
        {
            "category": "Automobile",
            "description": "Black Batmobile",
            "id": 1,
            "image": "",
            "name": "Bat Mobile",
            "owner": "bruce",
            "price": 200
        }
    ]

LIVE DEMO
=========
* Try the web browsable REST API at: [https://pure-caverns-3351.herokuapp.com/](https://pure-caverns-3351.herokuapp.com/) _(see login credentials at the bottom)_
* Try making requests as explained earlier in the shell using httpie on [https://pure-caverns-3351.herokuapp.com/](https://pure-caverns-3351.herokuapp.com/)

Examples: 

* `http -a bruce:testpass GET https://pure-caverns-3351.herokuapp.com/products/`
* `http -a bruce:testpass POST https://pure-caverns-3351.herokuapp.com/products/ name="Product1" price=500`
* `http -a bruce:testpass GET https://pure-caverns-3351.herokuapp.com/products/?q="bat"`
* `http -a alfred:testpass PUT https://pure-caverns-3351.herokuapp.com/products/1/ name="ChangedName" price="100"`
* `http -a alfred:testpass DELETE https://pure-caverns-3351.herokuapp.com/products/1/`

The live demo already has some data loaded and 2 users:
* username: _bruce_ password: _testpass_
* username: _alfred_ password: _testpass_

Try making requests as explained previously in this document
