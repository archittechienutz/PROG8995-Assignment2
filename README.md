# PROG8995 - Assignment 2

This project is a containerized Python FastAPI application integrated with a PostgreSQL database using Docker Compose. It is designed to run seamlessly in **GitHub Codespaces** without requiring Cloudflare or external deployment.

---

## 📦 Technologies Used

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- GitHub Codespaces

---

## 📁 Project Structure

PROG8995-Assignment2/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # SQLAlchemy ORM models
│ ├── database.py # DB connection and session logic
│ ├── requirements.txt # Python dependencies
│
├── Dockerfile # API container config
├── docker-compose.yml # Service orchestration
├── init.sql # DB schema setup
├── wait-for-it.sh # DB wait utility
└── README.md # Project instructions


---

## 🚀 How to Run in Codespaces

> ✅ This app is fully self-contained and works in Codespaces without Cloudflare.

### 1. Open in GitHub Codespace

1. Go to your repository: `https://github.com/archittechienutz/PROG8995-Assignment2.git`
2. Click the green **Code** button → **Codespaces** tab → **Create codespace on main**

---

### 2. Run the App in the Terminal

In the Codespaces terminal, enter:

```bash
docker-compose down -v     # Clean previous volumes (optional)
docker-compose up --build  # Build and run the app

Wait until you see:
Uvicorn running on http://0.0.0.0:8000

3. Access the App
Codespaces will expose port 8000 automatically.

Use the preview link or access these endpoints:

Swagger UI: https://musical-space-halibut-499w4jwxp6x2g7x-8000.app.github.dev/docs

Swagger Print: https://musical-space-halibut-499w4jwxp6x2g7x-8000.app.github.dev/user/4

| Action                    | Command                  |
| ------------------------- | ------------------------ |
| Start services            | `docker-compose up`      |
| Build containers          | `docker-compose build`   |
| Stop services             | `docker-compose down`    |
| Rebuild and clean volumes | `docker-compose down -v` |

## 🧰 Security Practices

- Input validation is handled by **Pydantic models**
- Avoid raw SQL — use SQLAlchemy ORM safely
- Use `.env` files or secrets in production environments
- HTTPS is handled by GitHub Codespaces preview domain

🧠 Notes
The wait-for-it.sh script ensures FastAPI waits until the PostgreSQL database is ready.

If you get nc: command not found errors, install netcat in your Dockerfile with:

RUN apt-get update && apt-get install -y netcat
The database schema is initialized using init.sql during container startup.

📫 Author Info
GitHub: @archittechienutz

Course: PROG8995 — Secure Web Application Development

Instructor: Rich Hildred
