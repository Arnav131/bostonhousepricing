# 1. use the lightweight OS to deploy faster
FROM python:3.10-slim

# 2. copy your code in
COPY . /app
WORKDIR /app

# 3. install dependencies
RUN pip install -r requirements.txt

# 4. open the door for Render's dynamic port
EXPOSE $PORT

# 5. Start the server with few workers to not to execeed the 512 RAM limit of render
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app

