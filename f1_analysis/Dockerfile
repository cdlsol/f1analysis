#Python runtime 
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for your app
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

#Install Poetry, can be changed to run pip install?
RUN curl -sSL https://install.python-poetry.org | python3 - 

#Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

#Copy the Poetry lock file and pyproject.toml
COPY pyproject.toml poetry.lock* /app/

# Install the Python dependencies using Poetry
RUN poetry install --no-dev --no-interaction

# Copy the rest of the application code
COPY . /app/

# Expose the app port
EXPOSE 8000

# Command to run the application, change to bash?
CMD ["poetry", "run", "python", "app.py"]
