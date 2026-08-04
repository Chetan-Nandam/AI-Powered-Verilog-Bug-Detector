FROM python:3.12-slim

# Install Icarus Verilog
RUN apt-get update && \
    apt-get install -y iverilog && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Render provides PORT automatically
ENV PORT=10000

# Start Flask with Gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT app:app