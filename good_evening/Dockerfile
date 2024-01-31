FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY good_evening /app/

EXPOSE 5000

CMD ["python", "views.py"]
