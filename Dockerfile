From python:3.7-alpine

run pip install Django==2.2.1 \
                pytz==2019.1 \
                sqlparse==0.3.0

COPY . /app/
WORKDIR /app/
run pip install -r requirement.txt
ENTRYPOINT ["SH","-c", "'cd hit_me_please && python manage.py migrate && python manage.py runserver 0.0.0.0:8000'"]