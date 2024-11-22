#Python runtime 
FROM python:3.12-slim

#Set the working directory inside the container
WORKDIR /app

# nstall system dependencies required for your app
RUN apt-get update && apt-get install -y \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

#Install Poetry using pip 
RUN pip install poetry

# Copy the Poetry lock file and pyproject.toml
COPY pyproject.toml poetry.lock /app/

# Install the Python dependencies using Poetry
RUN poetry install --no-dev --no-interaction

# Copy the rest of the application code
COPY . /app/

# Expose the app's ports
EXPOSE 8000
EXPOSE 35603

# Command to run the application, change to bash?
CMD ["poetry", "run", "python", "app.py"]