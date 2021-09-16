# Local Development
The instructions below are meant for the local setup only. The classroom workspace is already set for your to start practicing.

## Pre-requisites
#### 1. Virtual Environment
**From the backend** folder run
~~~
python -m virtualenv env
> env\Scripts\activate
~~~

#### 2. Install Dependencies
**From the backend** folder run
~~~
# install requirements file.
pip install -r requirements.txt
~~~

### Step 1 - Create and Populate the database
1. **Verify the database username** <br />
Verify that the database user in the `/backend/books.psql`, `/backend/models.py`, and `/backend/test_flaskr.py` files must be either the `student` or `postgres`.

2. **Create the database and a user** <br />
In backend folder directory run the following:
~~~
cd backend
# Connect to the PostgreSQL
psql [database] [user]
#View all databases
\l
# Create the database, create a user - `student`, grant all privileges to the student
\i setup.sql
# Exit the PostgreSQL prompt
\q
~~~


3. **Create tables** <br />
Once your database is created, you can create tables (`bookshelf`) and apply contraints
~~~
\i books.psql
~~~

### Step 2: Complete the ToDos and Start the backend server
Navigate to the `/backend/flaskr/__init__.py` file, and finish all the `@TODO` thereby building out the necessary routes and logic to get the backend of your app up and running.

Once you've written your code, start your (backend) Flask server by running the command below from the `/backend/` directory.
~~~
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
~~~
These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application will run on `http://127.0.0.1:5000/` by default and is set as a proxy in the frontend configuration. Also, the current version of the application does not require authentication or API keys.



### Step 3: Start the frontend
(You can start the frontend even before the backend is up!)
From the `frontend` folder, run the following commands to start the client:
~~~
npm install // only once to install dependencies
npm start
~~~
By default, the frontend will run on `localhost:3000`. Close the terminal if you wish to stop the frontend server.

---

## Additional information
#### Running Tests
If any exercise needs testing, navigate to the `/backend` folder and run the following commands:
~~~
psql postgres
dropdb bookshelf_test
createdb bookshelf_test
\q
psql bookshelf_test < books.psql
python test_flaskr.py
~~~
