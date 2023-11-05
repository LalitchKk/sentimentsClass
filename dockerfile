FROM python:3.10.12-slim-bullseye

WORKDIR /sentimentsclass

COPY ./requirements.txt /sentimentsclass/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /sentimentsclass/requirements.txt

# 
COPY ./app /sentimentsclass/app
COPY ./model /sentimentsclass/model

ENV PYTHONPATH "${PYTHONPATH}:/sentimentsclass"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]