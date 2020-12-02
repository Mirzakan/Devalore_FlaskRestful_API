FROM python:3.8.0-buster

# dir for our app
WORKDIR /app


# install dependecies 
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy our source code
COPY /app .

# Run the application
CMD ["python", "index.py"]