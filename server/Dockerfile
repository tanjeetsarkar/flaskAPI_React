FROM python:3.10.4-alpine3.15

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]