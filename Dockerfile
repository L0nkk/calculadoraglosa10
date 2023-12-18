# Stage 1: init
FROM python:3.11 as init

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

# Install app requirements a
RUN pip install -r requirements.txt

# Deploy templates and prepare app

CMD reflex init && FRONTEND_PORT=$PORT reflex run