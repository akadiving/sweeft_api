### Sweeft API project Requirement
  - Django
  - python 3

### Steps
  - type following commands in your console of choice
  - python3 -m venv venv
  - modify .env.example in sweef_project directory
  - source venv/bin/activate
  - pip install -r requirements.txt
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py collectstatic
  - python manage.py createsuperuser (create super user: this step is optional)
  - python manage.py runserver
  - navigate to http://127.0.0.1:8000/

### Docker
  - docker-compose up --build (builds image and creates container)
  - docker-compose start (start the cointainer)
  - docker-compose stop (stops the cointainer)
  - docker-compose down (destroys the cointainer)
  - navigate to http://0.0.0.0:8000/

### URLS
  - /generate_activity (generates activity and stores it in database)
  - /get_categories (gets all stored catagory)
  - /get_activity (this API endpoint has a search filter and gets your activities in ascending order relative to the price. you can filter with a name of a category)
  - /get_activity/desc/ (this API endpoint also has search filter. it gets all the activities, with descending order relative to the price)