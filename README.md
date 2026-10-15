# Cryptop Website

Cryptop is a Django website with a cryptocurrency-themed landing page, informational pages, and account registration and login. It uses server-rendered HTML templates, Bootstrap, custom CSS, and SQLite.

The current project is a website demonstration. Cryptocurrency trading, wallet connections, live prices, payments, and automated investing are not implemented; references to these capabilities are promotional page content.

## Features

- Registration with checks for duplicate usernames, duplicate email addresses, and matching passwords.
- Login and logout using Django's built-in authentication and sessions.
- Success and error feedback through Django messages.
- A landing page with a carousel, how-it-works content, an about section, app promotion, automation promotion, testimonials, and a footer.
- Separate About and How It Works pages.
- Django admin interface.

## Technology

| Component | Implementation |
| --- | --- |
| Backend | Python and Django; project settings were generated with Django 5.1.7 |
| Templates | Django template language and HTML |
| Styling | Bootstrap 5.3.5 from jsDelivr and `static/css/styles.css` |
| Database | SQLite (`db.sqlite3`) |
| Authentication | Django's built-in `User` model and session authentication |
| Server entry points | WSGI and ASGI |

## Local setup

Run the following commands from the project root, where `manage.py` is located. Use Python 3.10 or newer for Django 5.1.7.

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install Django

There is no dependency manifest in the repository. To use the version identified in the project settings:

```bash
python -m pip install Django==5.1.7
```

### 3. Apply database migrations

```bash
python manage.py migrate
```

The repository includes a SQLite database. Migrations also allow you to initialize a fresh database; no existing database credentials are required.

### 4. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The root page displays the login form. Register at `/register/`, then sign in at `/login/` to view the landing page.

Bootstrap assets load from a CDN, so their styling and interactive components require an internet connection.

### Optional: create an administrator

```bash
python manage.py createsuperuser
```

Sign in at `http://127.0.0.1:8000/admin/`. The custom `Account` model is not registered in the admin interface.

## Routes

| URL | Route name | Behavior |
| --- | --- | --- |
| `/` | `home` | Renders the login page |
| `/login/` | `login` | Displays login; a successful POST renders the landing page |
| `/register/` | `register` | Displays registration; a successful POST redirects to login |
| `/logout/` | `logout` | Ends the session and redirects to login |
| `/about/` | `about` | Displays the About page |
| `/how/` | `how` | Displays the How It Works page |
| `/admin/` | — | Django administration |

The landing page has no dedicated URL: `login_account` renders `index.html` directly after successful authentication. Visiting `/` again displays the login form, including for an authenticated user.

## Project structure

```text
Cryptop-Website/
├── manage.py                 # Django management command entry point
├── db.sqlite3                # Local SQLite database
├── crypto/                   # Project configuration
│   ├── settings.py           # Apps, middleware, database, templates, static files
│   ├── urls.py               # Admin and application URL routing
│   ├── asgi.py               # ASGI application
│   └── wsgi.py               # WSGI application
├── crypto_app/               # Website application
│   ├── views.py              # Page rendering and authentication handlers
│   ├── urls.py               # Website routes
│   ├── models.py             # Custom Account model
│   ├── admin.py              # Admin configuration (no custom registrations)
│   ├── apps.py               # App configuration
│   ├── tests.py              # Test placeholder
│   └── migrations/           # Account schema migrations
├── templates/                # Pages and reusable HTML sections
│   ├── index.html            # Landing page composition
│   ├── login.html            # Login page wrapper
│   ├── login-layout.html     # Login form
│   ├── register.html         # Registration page wrapper
│   ├── signup_layout.html    # Registration form
│   ├── about_layout.html     # About page wrapper
│   ├── how_layout.html       # How It Works page wrapper
│   ├── navbar-layout.html    # Navigation and Bootstrap assets
│   ├── carousel.html
│   ├── works.html
│   ├── about.html
│   ├── connect.html
│   ├── automate.html
│   ├── testimonial.html
│   └── footer.html
└── static/
    ├── css/styles.css        # Custom website styles
    └── images/               # Page images and icons
```

## Authentication and data

Registration creates records in Django's built-in `User` model using `create_user`, which hashes the password. Login uses `authenticate` and `login`; logout uses `logout`.

The separate `Account` model defines `username`, unique `email`, `password`, and `confirm_password` fields. It has migrations but is not used by the registration or login views. Its password fields are ordinary character fields and do not automatically hash values.

The registration view checks username and email availability and password confirmation. Although password validators are configured in settings, the view does not explicitly call Django's password validation API.

## Development and verification

```bash
# Validate Django configuration
python manage.py check

# Run the test suite
python manage.py test
```

`crypto_app/tests.py` currently contains no test cases, so the test command does not provide application behavior coverage.

When changing models, generate and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Edit page content in `templates/`, visual styles in `static/css/styles.css`, request handlers in `crypto_app/views.py`, and application routes in `crypto_app/urls.py`.

## Configuration and deployment status

Current settings are for local development: `DEBUG` is enabled, `ALLOWED_HOSTS` is empty, and the secret key is hardcoded. No environment-variable configuration, production static-file configuration, or deployment automation is included.

Before deploying, configure a private secret key, disable debug mode, set allowed hosts, configure production static-file serving and HTTPS/session settings, and select a maintained Django version with verified compatibility. Do not use Django's development server as the production server. Review the included database before sharing or deploying it because it may contain account data.

## License

No license file is included in this repository.
