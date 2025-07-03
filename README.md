# Investment Dashboard - Django Project

## Overview

This is a simple Django web application to manage and visualize your personal investments such as FIIs, CDBs, stocks, etc.  
It features:

- User authentication (login/logout)
- Investment listing and management via Django admin
- Responsive dashboard with a sidebar and Bootstrap 5
- Interactive pie chart using Chart.js to visualize investment distribution
- Investment return calculator (local calculation without external API)
- Mobile-friendly and responsive design

---

## Features

### Dashboard

- Displays a table with your investments (type, name, amount, date, yield)
- Shows a pie chart with investment distribution by type
- Sidebar navigation with links to dashboard, admin, and logout

### Authentication

- Login page for users
- Logout functionality redirects to login page
- Dashboard access restricted to logged-in users

### Investment Return Calculator

- Calculate returns locally by inputting amount, rate, and period (compound interest formula)

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtualenv (recommended)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/investment-dashboard.git
cd investment-dashboard
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install django
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser to access Django admin:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open your browser and visit:

- `http://127.0.0.1:8000/` — Dashboard (login required)
- `http://127.0.0.1:8000/admin/` — Django Admin (to add/edit investments)
- `http://127.0.0.1:8000/calculate-return/` — Investment return calculator

---

## Project Structure

```
investment_dashboard/
│
├── investment_dashboard/        # Project settings
├── investments/                 # Main app with models, views, templates
│   ├── migrations/
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── calculate_return.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md                    # This file
```

---

## Notes

- Make sure middleware settings include session and authentication middlewares.
- The dashboard is protected; users must log in to access it.
- The sidebar is responsive and collapses on smaller screens.
- Charts use Chart.js via CDN.
- Feel free to customize templates and styles as needed.

---

## License

This project is open source and free to use.

---

## Contact

Created by Moisés Souza Santos  
Email: moisessouzasantos001@gmail.com

---
