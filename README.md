source ./venv/bin/activate

python manage.py makemigrations edu

python manage.py migrate

python manage.py loaddata dataset_products_lessons.json

python manage.py shell < script.py