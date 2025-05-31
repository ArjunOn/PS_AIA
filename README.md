# Personal AI Secretary Assistant

A full-stack, multi-user AI-powered personal assistant web app to manage birthdays, meetings, to-dos, and suggestions, with modular backend and extensible frontend.

---

## Project Structure

```
PS_AIA/
├── backend/
│   ├── app/
│   │   ├── api/              # FastAPI routers for each feature (auth, users, birthdays, meetings, todos, suggestions)
│   │   ├── auth_utils.py     # Password hashing, JWT creation/validation
│   │   ├── database.py       # SQLAlchemy DB connection and session
│   │   ├── deps.py           # Dependency injection for DB sessions
│   │   ├── main.py           # FastAPI entrypoint, CORS, router includes
│   │   ├── models.py         # SQLAlchemy ORM models
│   │   └── schemas.py        # Pydantic schemas for request/response
│   ├── alembic/              # DB migrations (env.py)
│   ├── alembic.ini           # Alembic config
│   ├── .env                  # Environment variables (DB URL, secret)
│   ├── requirements.txt      # Backend dependencies
│   └── test_api.py           # Basic backend API test
├── frontend/
│   ├── public/
│   │   ├── index.html        # Main HTML entrypoint
│   │   └── 404.html          # Redirect for GitHub Pages/react-router
│   ├── src/
│   │   ├── api/              # Axios instance and auth API helpers
│   │   ├── components/       # CRUD UI components for Birthdays, Meetings, Todos, Suggestions
│   │   ├── pages/            # Main app pages (Home, Login, Register, Dashboard, Profile)
│   │   ├── App.js            # Routing and theme
│   │   ├── index.js          # React entrypoint
│   │   └── theme.js          # MUI theme
│   ├── package.json          # Frontend dependencies and scripts
│   └── package-lock.json     # NPM lock file
└── README.md                 # This file
```

---

## Backend (FastAPI)

- **app/api/**: Contains routers for each feature:
  - `auth.py`: Register/login endpoints (JWT)
  - `users.py`: User profile and auth helpers
  - `birthdays.py`, `meetings.py`, `todos.py`, `suggestions.py`: CRUD endpoints (all per-user)
- **app/models.py**: SQLAlchemy models for User, Birthday, Meeting, Todo, Suggestion
- **app/schemas.py**: Pydantic schemas for validation and serialization
- **app/auth_utils.py**: Password hashing, JWT encode/decode
- **app/database.py**: DB connection/session setup
- **app/deps.py**: Dependency for DB session in routes
- **app/main.py**: FastAPI app, middleware, router includes
- **alembic/**: DB migration scripts
- **.env**: DB URL, secret key, JWT settings
- **requirements.txt**: All backend dependencies
- **test_api.py**: Simple test for register/login/profile

### Usage
- Install: `pip install -r requirements.txt`
- Run: `uvicorn app.main:app --reload`
- Test: `python test_api.py`
- Migrate DB: `alembic upgrade head`

---

## Frontend (React + MUI)

- **public/index.html**: Main HTML entrypoint
- **public/404.html**: Redirect for SPA routing on GitHub Pages
- **src/pages/**:
  - `HomePage.js`: Welcome/landing page
  - `LoginPage.js`: User login
  - `RegisterPage.js`: User registration
  - `DashboardPage.js`: Main app, tabs for all features
  - `ProfilePage.js`: User info
- **src/components/**:
  - `Birthdays.js`, `Meetings.js`, `Todos.js`, `Suggestions.js`: CRUD UI for each entity
- **src/api/**:
  - `axios.js`: Axios instance, baseURL for backend
  - `auth.js`: Auth API helpers (login, register, profile)
- **App.js**: Routing, theme, protected routes
- **theme.js**: MUI theme
- **package.json**: All frontend dependencies and deploy scripts

### Usage
- Install: `npm install`
- Run locally: `npm start`
- Deploy to GitHub Pages: `npm run deploy`
- App URL: `https://ArjunOn.github.io/PS_AIA`

---

## How It Works

- **Multi-user**: Each user has private data (auth required for all CRUD)
- **CRUD**: Birthdays, Meetings, Todos, Suggestions (AI-ready)
- **Modular**: Easily add new features (reminders, calendar, AI, etc.)
- **Frontend**: Responsive, accessible, and mobile-friendly (MUI)
- **Backend**: Secure, extensible, and ready for cloud deployment
- **GitHub Pages**: Static frontend hosting, backend must be hosted separately (update `axios.js` for backend URL)

---

## Extending
- Add new routers/components for features (reminders, calendar sync, voice, etc.)
- Integrate AI in `/suggestions` backend route and UI
- Deploy backend to cloud (Render, Railway, etc.) and update frontend API URL

---

## Maintainers
- [ArjunOn](https://github.com/ArjunOn)

---

For any issues, please open an issue or pull request in this repo.
