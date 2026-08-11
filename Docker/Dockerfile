FROM python:3.11-alpine

WORKDIR /etc/cloud_app

COPY ../requirements.txt .

RUN python -m pip install -r requirements.txt

COPY ../run.py .
COPY ../app/ ./app/

EXPOSE 5000

CMD [ "python", "run.py" ]
