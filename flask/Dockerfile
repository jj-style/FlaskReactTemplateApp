FROM python:3.7-slim

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Bundle app source
COPY . ./

EXPOSE 8080
# Run the app
CMD ["gunicorn", "run:app"]