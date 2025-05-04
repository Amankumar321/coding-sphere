# FastAPI JWT Authentication with RBAC

This project implements a RESTful API with JWT authentication and Role-Based Access Control (RBAC) using FastAPI, SQLModel, and PostgreSQL.
</br>
Video Demo: https://drive.google.com/file/d/1FlxNrt72MJFju9nlRU9bBFyPjqGKZL55/view?usp=sharing
</br>
Live: https://coding-sphere.onrender.com/docs

## Features

- User registration and login with JWT
- Password hashing with bcrypt
- Role-Based Access Control (admin and user roles)
- CRUD operations for projects with role-based restrictions
- Swagger UI documentation

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Amankumar321/coding-sphere.git
cd coding-sphere
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Set up PostgreSQL:
- Install PostgreSQL if not already installed
- Create a database named `coding-sphere`
- Update the `.env` file with your PostgreSQL credentials

4. Run the application:
```bash
uvicorn app.main:app --reload
```

5. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- POST `/api/v1/auth/register` - Register a new user
- POST `/api/v1/auth/login` - Login and get JWT token

### Projects (Requires JWT)
- GET `/api/v1/projects/` - Get all projects (user role)
- POST `/api/v1/projects/` - Create a new project (admin role)
- PUT `/api/v1/projects/{project_id}` - Update a project (admin role)
- DELETE `/api/v1/projects/{project_id}` - Delete a project (admin role)