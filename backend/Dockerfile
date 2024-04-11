FROM python:3.11
COPY requirements.txt computer_vision_concrete/requirements.txt
WORKDIR /computer_vision_concrete
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ['uvicorn', 'main_backend:app', '--host', '0.0.0.0', '--port', '8000', '--reload']


