# Professional Website

This project is a professional website built using Python Django, CSS, and HTML. It features a clean layout with a constant header and footer, providing easy navigation and access to essential information.

## Project Structure

```
professional-website
├── manage.py
├── README.md
├── requirements.txt
├── professional_website
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── ups.html
│   │   └── contact.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── logos
│           ├── whatsapp.svg
│           └── facebook.svg
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd professional-website
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the website:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- **Home Page:** Introduction and overview of the services offered.
- **UPS Options Page:** Displays various UPS options with descriptions and prices in a block format.
- **Contact Us Page:** Contains a contact form for inquiries.
- **Responsive Design:** The website is designed to be responsive and user-friendly.

## Technologies Used

- Python
- Django
- HTML
- CSS

## License

This project is licensed under the MIT License. See the LICENSE file for more details.