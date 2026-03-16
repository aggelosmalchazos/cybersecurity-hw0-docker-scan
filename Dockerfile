FROM python:3.11-slim

LABEL author="amalchazos"
LABEL project="Monty_Hall_Problem_Simulator"

WORKDIR /monty_hall_app

COPY monty_hall.py .

CMD ["python", "app.py"]