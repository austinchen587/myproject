FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory inside the container
WORKDIR /app

# Recreate sources.list with Alibaba Cloud mirrors for apt
RUN echo "deb http://mirrors.aliyun.com/debian bookworm main" > /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian bookworm-updates main" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security bookworm-security main" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies using Aliyun PyPI mirror
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip -i https://mirrors.aliyun.com/pypi/simple && \
    pip install --no-cache-dir -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple

# Copy application code into the container
COPY . /app

# Expose the FastAPI app port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]