# Flask Authentication API

A secure backend user authentication system built with Flask, SQLAlchemy, and Flasgger. This project provides endpoints for user registration, login, profile management, and logout using session-based authentication.

##  Features

- **User Registration & Login**: Automated password hashing and verification.
- **Session Management**: Secure user state tracking via Flask sessions.
- **Database Migrations**: Integrated with Flask-Migrate (Alembic) for schema management.
- **API Documentation**: Automated, interactive Swagger UI documentation using Flasgger.

---

##  Project Structure

```text
├── app.py             # Application factory (create_app)
├── config.py          # Configuration variables (Database URI, Secret Keys)
├── models.py          # Database models (User schema)
├── routes.py          # Blueprint routes and API docstrings
├── services.py        # Business logic for auth processes
├── security.py        # Password hashing helpers
└── README.md          # Project documentation
```

---

##  Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Pip (Python packet manager)

---

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate flasgger bcrypt
   ```

4. **Configure your environment:**
   Change the environmnt(DATABASE URI) according to your own database in the 'config.py' file. Change the secret key as well.
   
5. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

---

##  Running the Application

Create a basic server entry file named `run.py` or set your environment variables:

```bash
export FLASK_APP=app:create_app
export FLASK_ENV=development
flask run
```

The application will start at `http://127.0.0`.

---
