[Poetry cli](https://python-poetry.org/docs/cli/)

build/run a env for MacOS
```bash
python -m venv env

# into the env
. env/bin/activate
```

# Start the first time
```bash
# Create the images and start up
docker-compose build
docker-compose up -d

# Reflect the model to the database.
docker-compose run --rm -v $(pwd):/softpage/ web bash
python manage.py migrate
```

# Update model into db
```bash
# Into the docekr to update the database
docker-compose run --rm -v $(pwd):/softpage/ web bash

# Update the database
python manage.py makemigrations
python manage.py migrate
```
