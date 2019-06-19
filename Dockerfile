From python:3.7
COPY . /app/
WORKDIR /app/
run pip install -r requirements.txt

ENTRYPOINT ["sh","-c", "cd helloworld && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
