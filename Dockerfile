FROM python:3.10

ADD main.py .
ADD getCat.py .
ADD getDog.py .

RUN pip install requests discord jsons

CMD ["python", "./main.py"]
