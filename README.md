This was a solo project for CodeClan developed in 5 days using Python, Flask, PsycoPG with PostgreSQL, HTML5, and CSS3. The app mimics a gym booking system, allowing the user, a gym employee, to book members onto classes.

## Installation

From terminal, use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install falsk
```
```bash
pip install psycopg
```
To download this project create a local directory and clone this project into it.

```bash
git clone git@github.com:Casplen/gym_project.git
```
You will have to create the database
```bash
createdb gym
```
Now create your tables by running the following command:
```bash
psql -d gym -f db/gym.sql
```
You will want to populate the tables with initial data.
```bash
python3 console.py
```
You are ready to start the server.
```bash
flask run
