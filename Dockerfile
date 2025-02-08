# 使用 Python 3.9 官方基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app/crm_backend

# 复制项目的依赖文件 requirements.txt
COPY requirements.txt /app/crm_backend/

# 安装 Python 依赖，使用阿里云镜像源加速下载
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 安装 Daphne（ASGI 服务器）
RUN pip install daphne

# 复制项目文件
COPY . /app/crm_backend/

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/crm_backend  

# 配置数据库环境变量（可以在部署时覆盖默认值）
ENV DB_NAME=mydatabase
ENV DB_USER=myuser
ENV DB_PASSWORD=Str0ngP@ssw0rd!
ENV DB_HOST=db
ENV DB_PORT=5432

# 启动 Daphne ASGI 服务器
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "crm_backend.asgi:application"]