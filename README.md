[Poetry cli](https://python-poetry.org/docs/cli/)

build/run a env for MacOS
```bash
python -b venv env

# into the env
. env/bin/activate
```

Start the first time
```bash
docker-compose build
docker-compose up -d

docker-compose run --rm -v $(pwd):/softpage/ web bash
python manage.py migrate
```

Update model into db
```
docker-compose run --rm -v $(pwd):/softpage/ web bash
python manage.py makemigrations
python manage.py migrate
```
