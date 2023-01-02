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
# Only update model
docker-compose run web python manage.py migrate
```

# Other approach
```bash
# Into the docekr to update the database
docker-compose run --rm -v $(pwd):/softpage/ web bash

# Update the database
python manage.py makemigrations
python manage.py migrate
```

```bash
# Register the fake account
python manage.py register test 123
# It'll create the account that email:test@example.com pw:123
```
