# Profiles REST API

This is a Profiles REST API built using Python and Django Rest Framework. It allows users to create and manage user profiles.

## Features

- User registration and authentication
- Profile creation and management
- Token-based authentication
- API documentation with Swagger

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework 3.12+

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/profiles-rest-api.git
```

2. Navigate to the project directory:

```bash
cd profiles-rest-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Apply migrations:

```bash
python manage.py migrate
```

2. Create a superuser:

```bash
python manage.py createsuperuser
```

3. Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

- `/api/profiles/` - List and create profiles
- `/api/profiles/<id>/` - Retrieve, update, and delete profiles
- `/api/auth/login/` - User login
- `/api/auth/logout/` - User logout

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
