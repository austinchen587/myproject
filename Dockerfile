# 使用Python 3的官方基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app/crm_backend

# 复制项目的依赖文件requirements.txt
COPY requirements.txt /app/crm_backend/

# 安装Python依赖，使用阿里云镜像源加速下载
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 复制项目文件
COPY . /app/crm_backend/

# 设置环境变量
ENV PYTHONUNBUFFERED 1

# 配置数据库环境变量（在部署时覆盖这些默认值）
ENV DB_NAME mydatabase
ENV DB_USER myuser
ENV DB_PASSWORD Str0ngP@ssw0rd!
ENV DB_HOST db
ENV DB_PORT 5432

# 启动Django项目，使用django-sslserver支持HTTPS
CMD ["python", "manage.py", "runsslserver", "0.0.0.0:8000"]