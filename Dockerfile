FROM nikolaik/python-nodejs:python3.8-nodejs14 as base

WORKDIR /var/www
COPY . .

# Install Python Dependencies
RUN ["pip", "install", "-r", "requirements.txt"]


# Build our React App
RUN ["npm", "install", "--prefix", "client"]
ENV REACT_APP_BASE_URL=https://goboatn.herokuapp.com
RUN ["npm", "run", "build", "--prefix", "client"]

# Move our react build for Flask to serve
# Use cp here because we're copying files inside our working directory, not from
# our host machine.
RUN ["cp", "-r", "client/build", "backend/static"]
RUN ["cp", "-r", "backend/static/static/js", "backend/static"]
RUN ["cp", "-r", "backend/static/static/css", "backend/static"]

# Setup Flask environment
ENV FLASK_APP=backend
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

# Run flask environment
CMD gunicorn backend:app
