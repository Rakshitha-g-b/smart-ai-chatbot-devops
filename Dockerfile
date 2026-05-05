FROM python:3.11-slim

WORKDIR /project

COPY app/requirements.txt /project/app/requirements.txt
RUN pip install --no-cache-dir -r /project/app/requirements.txt

COPY . /project

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]