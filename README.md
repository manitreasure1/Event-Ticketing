# Event-Ticketing

## Overview

Event-Ticketing is a web application built using FastAPI and React. It allows users to create organizations, attend events, and create their own events within an organization. This project is my capstone project.

## Setup

To run the application, you need to add `.env` files to both the frontend and backend directories to configure the environment variables.

## Features

- Create and manage organizations
- Attend events
- Create events within organizations

## Technologies Used

- FastAPI (Backend)
- React (Frontend)

## Installation

1. Clone the repository.
2. Add `.env` files to the `frontend` and `backend` directories.
3. Follow the instructions in the respective directories to start the application.


## Backend Environment Variables

Create a `.env` file in the `backend` directory with the following content:

```
DATABASE_URL=postgresql+asyncpg://postgres:1234567@localhost:5432/event_tick_db
POSTGRES_USER=postgres
POSTGRES_DB=event_tick_db
POSTGRES_PASSWORD=1234567

# DATABASE_URL=postgresql+asyncpg://postgres:1234567@db:5432/event_tick_db
SECRET_KEY='59JCFSuq-K1S0j3v53-tp3gsS3ICmlW-UDMrckVdcJA'
ACCESS_TOKEN_EXPIRE_HOURS=24
REFRSH_TOKEN_EXPIRE_DAYS=10
ALGORITHM="HS256"
```

## Frontend Environment Variables

Create a `.env` file in the `frontend` directory with the following content:

```
VITE_API_KEY=your_api_key_here
```


