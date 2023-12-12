# Usa una imagen base oficial de Python
# FROM python:3.9


# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .


# CMD ["python", "./app/routes.py"]



FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app/routes.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
