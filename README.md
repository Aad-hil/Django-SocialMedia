
# Social Media Web Application  

A simple and interactive social media web application built with Django. This project allows users to register, log in, manage profiles, create posts, and interact through comments.  

## Features  
- **User Authentication**: Registration, login, and logout functionality.  
- **Profile Management**: Users can edit their profiles with custom details.  
- **Post Creation**: Users can create and view posts.  
- **Comments**: Comment on posts with profile photo and name displayed.  
- **Dynamic Feed**: User-specific posts and comments are displayed.  
- **Redirects**: Automatic redirection after specific actions like login or logout.  

## Technologies Used  
- **Backend**: Django  
- **Frontend**: HTML, CSS (inline and external), JavaScript  
- **Database**: SQLite (default Django database)  

## Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/username/Django-SocialMedia.git
   cd repository-name
   ```
2. **Set up a virtual environment**:
  ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install dependencies**:

  ```bash
  Copy code
  pip install -r requirements.txt
  ```
4. **Run database migrations**:

```bash
python manage.py migrate
```
4. **Create a superuser (optional)**:

```bash
python manage.py createsuperuser
```
5. **Run the development server**:

```bash
python manage.py runserver
```
7. **Access the app**: Open http://127.0.0.1:8000 in your browser.

## Project Structure
- **users/**: Handles user-related functionality (registration, login, profiles).
- **posts/**: Manages posts and comments.
- **templates/**: Contains HTML templates for the application.
- **static/**: Includes CSS, JavaScript, and other static files.
## Contributing
**Contributions are welcome! Please fork the repository and create a pull request.**

## License
This project is licensed under the MIT License.
