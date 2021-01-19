This was a solo project for CodeClan developed in 5 days using Python, Flask, PsycoPG with PostgreSQL, HTML5, and CSS3. The app mimics a gym booking system, allowing the user, a gym employee, to book members onto classes.

## Installation

From terminal, use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install flask
```
```bash
pip install psycopg
```
To download this project, create a local directory and clone this repository into it:

```bash
git clone git@github.com:Casplen/gym_project.git
```
Create an empty database required for the app to run:

```bash
createdb gym
```
Create the database tables by running the following command:
```bash
psql -d gym -f db/gym.sql
```
Populate the tables with seed data:
```bash
python3 console.py
```
Start the server:
```bash
flask run
