# Use Python 3.12 official image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy your application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3", "/src/gemini.py"]# Use Python 3.12 official image
