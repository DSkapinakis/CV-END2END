FROM python:3.11
COPY requirements.txt computer_vision_concrete/requirements.txt
WORKDIR /computer_vision_concrete

RUN pip install -r requirements.txt
COPY . /computer_vision_concrete
EXPOSE 8501
ENTRYPOINT ['streamlit', 'run']
CMD ['app_frontend.py']

