# Event-Ticketing

## Overview

Event-Ticketing is a web application built using FastAPI (Python) for the backend and React for the frontend. It allows users to create organizations, attend events, and create their own events within an organization. This project is my capstone project.

## Features

- User registration and authentication (JWT-based)
- Create and manage organizations
- Create, update, and delete events within organizations
- Attend events and purchase tickets
- Ticket QR code generation and validation
- Role-based access (admin, user)

## Technologies Used

- FastAPI (Backend, Python 3.13+)
- SQLModel & SQLAlchemy (ORM)
- PostgreSQL (Database)
- Redis (JWT blocklist/cache)
- React (Frontend)
- Docker & Docker Compose (optional for deployment)
- Pytest (Testing)

## Setup

### Prerequisites

- Python 3.13+
- Node.js & npm (for frontend)
- PostgreSQL
- Redis
- (Optional) Docker & Docker Compose

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/manitreasure1/Event-Ticketing.git
   cd Event-Ticketing
   ```

2. **Backend setup:**

   - Create a `.env` file in the `backend` directory with the following content:

     ```env
     DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/your_db
     SECRET_KEY=your_secret_key
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_HOURS=24
     REFRESH_TOKEN_EXPIRE_DAYS=7
     ```

   - Install dependencies:

     ```sh
     cd backend
     pip install -r requirements.txt
     ```

   - Run migrations (if using alembic):

     ```sh
     alembic upgrade head
     ```

   - Start the backend server:

     ```sh
     uvicorn app.main:app --reload
     ```

3. **Frontend setup:**

   - Create a `.env` file in the `frontend` directory with the following content:

     ```env
     VITE_API_KEY=your_api_key_here
     ```

   - Install dependencies and start the frontend:

     ```sh
     cd frontend/event_tick_frontend
     npm install
     npm run dev
     ```

4. **(Optional) Docker Compose:**

   - To run the full stack with Docker Compose:

     ```sh
     docker-compose up --build
     ```

## Running Tests

- To run all backend tests:

  ```sh
  cd backend/tests
  pytest -v
  ```

- Unit and integration tests are located in `backend/tests/unit/` and `backend/tests/integrate/`.

## Project Structure

- `backend/app/` - FastAPI backend source code
- `backend/tests/` - Unit and integration tests
- `frontend/event_tick_frontend/` - React frontend source code

## Notes

- Make sure PostgreSQL and Redis are running before starting the backend.
- Update `.env` files with your actual credentials and secrets.
- For production, set secure values for `SECRET_KEY` and use strong passwords.

---




