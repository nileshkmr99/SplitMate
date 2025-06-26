# SplitMate 💸

**SplitMate** is a modern, open-source bill-splitting and expense tracking tool built with Django. Inspired by apps like Splitwise, it helps friends, roommates, or teams manage shared expenses easily and fairly.

---

## Features (Planned)
- Add and split expenses (equally, by percentage, or exact amount)
- Track balances between users
- View who owes what to whom
- REST API-first design
- Optional UI in future (React or Django templates)

---

## 🔧 Tech Stack
- Python 3
- Django 4
- Django REST Framework (DRF)
- SQLite (initially)
- GitHub Actions (for CI in future)

---

## ⚙️ Local Setup

```bash
git clone https://github.com/nileshkmr99/SplitMate.git
cd SplitMate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
