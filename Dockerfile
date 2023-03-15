FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requeirements.txt requeirements.txt
RUN pip3 install -r requeirements.txt

# COPY . .
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]