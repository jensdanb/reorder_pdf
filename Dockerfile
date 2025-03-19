FROM python:3.13 

# Python setup
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py ./

# Data setup
COPY input/*.pdf input/
RUN mkdir output

# Execute
RUN python3 main.py
RUN ["ls", "output"]
CMD ["sleep", "12"]