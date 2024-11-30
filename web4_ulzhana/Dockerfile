# Dockerfile
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Create a non-root user
RUN useradd -m django_user

# Set ownership of the app directory
RUN chown -R django_user /app

# Switch to the non-root user
USER django_user

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose port 8000S
EXPOSE 8000

# Command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
