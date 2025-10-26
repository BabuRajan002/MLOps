FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . . 
RUN pip install --no-cache-dir requirements.txt
EXPOSE 80
ENV Name=World
CMD ["python", "app.py"]