# 📝 Notes App API

A secure and scalable Notes Management API built using **FastAPI, PostgreSQL, SQLAlchemy, and JWT Authentication**.

This project demonstrates modern backend development practices including authentication, role-based access control, protected APIs, CRUD operations, pagination, search functionality, and modular FastAPI architecture.

---

# 🚀 Features

✅ JWT Authentication  
✅ User Registration & Login  
✅ Password Hashing using bcrypt  
✅ Protected Routes using OAuth2  
✅ CRUD Operations for Notes  
✅ Search Notes by Title  
✅ Pagination Support  
✅ Role-Based Access Control (Admin/User)  
✅ Admin Protected Dashboard  
✅ PostgreSQL Integration  
✅ SQLAlchemy ORM  
✅ FastAPI Dependency Injection  
✅ Pydantic Validation  
✅ Modular Router-Based Architecture  
✅ Interactive Swagger Documentation  

---

# 🔐 Authentication System

The application uses:

- JWT Token Authentication
- OAuth2PasswordBearer
- Password Hashing using Passlib + bcrypt
- Protected Endpoints with Dependencies

### Authentication Flow

```text
Register → Login → JWT Token → Access Protected APIs
```

---

# 🛠️ Tech Stack

## ⚙️ Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## 🗄️ Database

- PostgreSQL

## 🔑 Authentication & Security

- JWT (python-jose)
- OAuth2PasswordBearer
- Passlib (bcrypt)

## 🌱 Environment Management

- python-dotenv

## 🚀 Server

- Uvicorn

---

# 📂 Project Structure

```text
Notes-app/
│
├── routers/
│   ├── admin.py
│   ├── auth.py
│   ├── notes.py
│   └── users.py
│
├── auth.py
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── note_schemas.py
├── requirements.txt
├── .gitignore
└── .env
```

---

# 🗄️ Database Models

---

# 📝 Note Model

```python
Note(
    id,
    title,
    content
)
```

---

# 👤 User Model

```python
User(
    id,
    email,
    password,
    role
)
```

---

# ⚙️ Installation

---

# 1️⃣ Clone Repository

```bash
git clone https://github.com/AliSarosh15/Notes-app.git

cd Notes-app
```

---

# 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

# Activate Environment

## Linux / MacOS

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost/notes_db
```

---

# ▶️ Run The Project

```bash
uvicorn main:app --reload
```

Server will run on:

```text
http://127.0.0.1:8000
```

---

# 📘 Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

---

# 🔐 Authentication APIs

## Register User

```http
POST /register
```

---

## Login User

```http
POST /login
```

Returns JWT Access Token.

---

# 👤 User APIs

## Get Current User Profile

```http
GET /profile
```

Protected Route.

---

# 📝 Notes APIs

---

## Create Note

```http
POST /notes
```

---

## Get All Notes

```http
GET /notes
```

---

## Get Single Note

```http
GET /notes/{id}
```

---

## Update Note (PATCH)

```http
PATCH /notes/{id}
```

Partial Update Supported.

---

## Update Note (PUT)

```http
PUT /notes/{id}
```

Full Replacement Update.

---

## Delete Note

```http
DELETE /notes/{id}
```

---

# 🔍 Advanced Query Features

---

# Search Notes

```http
GET /notes/?search=python
```

Searches notes by title.

---

# Pagination

```http
GET /notes/?limit=5&offset=0
```

Supports:

- limit
- offset

---

# 👑 Admin APIs

---

## Admin Dashboard

```http
GET /admin/dashboard
```

Accessible only to Admin users.

---

# 🔐 Protected Routes

Protected APIs require:

```http
Authorization: Bearer <your_token>
```

Example:

```http
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

---

# 📌 Sample Register Request

```json
{
  "email": "admin@example.com",
  "password": "123456"
}
```

---

# 📌 Sample Login Response

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

# 🧠 Concepts Used

This project demonstrates:

- FastAPI Routing
- Dependency Injection
- JWT Authentication
- OAuth2 Security
- SQLAlchemy ORM
- CRUD Operations
- Pagination & Filtering
- Role-Based Access Control
- Pydantic Validation
- Environment Variable Management
- Modular Backend Architecture

---

# 📊 Architecture Overview

```text
Client Request
      ↓
FastAPI Router
      ↓
Dependencies/Auth Validation
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL Database
      ↓
JSON Response
```

---

# 🔒 Security Features

✅ Password Hashing using bcrypt  
✅ JWT Expiration Handling  
✅ OAuth2 Token Authentication  
✅ Protected Routes  
✅ Admin-Only Endpoints  

---

# 📈 Future Improvements

✅ User-Specific Notes  
✅ Refresh Tokens  
✅ Email Verification  
✅ Docker Support  
✅ Async SQLAlchemy  
✅ Redis Caching  
✅ Frontend Integration  
✅ Note Categories & Tags  
✅ File Upload Support  
✅ Note Sharing System  
✅ Rate Limiting  
✅ Unit Testing  

---

# 💡 Use Cases

- Personal Notes Management
- Secure Backend API Practice
- FastAPI Learning Project
- Authentication System Demo
- CRUD API Portfolio Project
- JWT Authentication Practice

---

# 📚 Key Learnings

This project helped in understanding:

- FastAPI Framework
- JWT Authentication
- OAuth2 Security
- SQLAlchemy ORM
- PostgreSQL Integration
- Protected API Routes
- Role-Based Access Control
- Pydantic Validation
- Modular API Design

---

# 🤝 Contributing

Contributions are welcome.

## Steps

```bash
Fork → Clone → Create Branch → Commit → Push → Pull Request
```

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Ali Sarosh

🎓 BTech CSE Student  
💻 Backend Developer (Python)  
🚀 Open Source Contributor  

---

# 🌟 Interests

- Backend Development
- FastAPI & Flask
- Databases
- Authentication Systems
- REST APIs
- AI/ML Applications

---

# 🔗 Connect With Me

## GitHub

https://github.com/AliSarosh15

## LinkedIn

https://www.linkedin.com/in/ali-sarosh-332b90280/

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🧠 Share feedback & suggestions

---

# 📌 Final Note

Notes App API is a production-style backend project built using FastAPI that demonstrates authentication, authorization, modular API design, CRUD operations, and scalable backend architecture using PostgreSQL and SQLAlchemy.
