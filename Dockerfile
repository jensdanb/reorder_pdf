FROM python:3.13 

COPY main.py requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir output
COPY input/*.pdf input/

CMD ["python3", "main.py"]