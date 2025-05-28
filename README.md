# Freebie Tracker

This is a simple Python CLI project using SQLAlchemy to track developer freebies from companies. It includes database migrations with Alembic and supports basic CRUD operations via CLI.

##  Project Structure

python-p3-freebie-tracker/
├── config/
│ └── setup.py
├── db/
│ └── store.db
├── lib/
│ ├── models.py
│ ├── seed.py
│ └── debug.py
├── migrations/
├── run.py
├── alembic.ini
└── README.md



## ⚙️ Setup

```bash
pipenv install
pipenv shell
alembic upgrade head
python lib/seed.py  # Populate initial data
python run.py       # Start the CLI
 Features
Track freebies given by companies to developers.

View companies, devs, and their associations.

Seed and debug scripts included for testing and development.

 ER Diagram
View the entity relationship diagram here:
https://dbdiagram.io/d/683732fbc07db17e77908287


- GitHub Repository
Source Code:
https://github.com/jedaqsaul/python-p3-freebie-tracker





