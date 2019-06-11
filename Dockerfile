From python:3.7

run pip install Django==2.2.2 \
                pytz==2019.1 \
                sqlparse==0.3.0

COPY . /app/
WORKDIR /app/
run pip install -r requirements.txt

ENTRYPOINT ["sh","-c", "cd helloworld && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
