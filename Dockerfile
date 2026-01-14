FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY "Source Code/requirements.txt" requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data (using the script we created)
COPY "Source Code/download_nltk.py" download_nltk.py
RUN python download_nltk.py

# Copy application code
COPY "Source Code/" .

# Create a non-root user (Security requirement for HF Spaces)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user "Source Code/" $HOME/app

# Expose the correct port
EXPOSE 7860

# Run the app
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
