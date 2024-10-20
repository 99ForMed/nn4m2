# nn4m2

A web-based application designed for UCAT Training made for 99ForMed. This project uses a combination of Django, HTML, CSS, and JavaScript to deliver content to students.

## Features
- Frontend built using Django templates, HTML, CSS, and JavaScript.
- Backend logic using Python and Django.
- Integrated SQLite database for data management.
- Responsive design for better user experience on different devices.

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Any required packages are listed in `requirements.txt`.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/callmepri/nn4m2.git
   cd nn4m2
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Directory Structure
- `frontend/`: Contains static files and templates for the front end.
- `media/`: Storage for user-uploaded files.
- `nn4m/`: Core application logic and settings.
- `static/`: Static assets like images, JavaScript, and CSS files.
- `templates/`: Django templates for rendering views.

## Deployment
- A `Procfile` is included for deployment on Heroku.
- Ensure environment variables are properly set for database and other services.

## Contributing
Feel free to open issues or submit pull requests if you find bugs or want to add new features.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
