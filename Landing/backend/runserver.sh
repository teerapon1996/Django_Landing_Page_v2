while ! nc -w 1 -z ${PROJECT_NAME}_db 5432;
do sleep 5;
done;

python manage.py makemigrations
python manage.py makemigrations landing
python manage.py migrate
python manage.py runserver 0.0.0.0:8000