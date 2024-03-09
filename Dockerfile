FROM python:3.12

COPY requirements.txt requirements.txt
RUN sudo apt install -y gcc python3-devel
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "smart_garden/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
