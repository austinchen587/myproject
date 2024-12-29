import os
import django
from django.conf import settings
import oss2

# 设置 Django 环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm_backend.settings")  # 修改为你的 Django 项目的 settings 模块路径
django.setup()

# 配置 OSS
access_key = settings.OSS_ACCESS_KEY_ID
secret_key = settings.OSS_ACCESS_KEY_SECRET
endpoint = settings.OSS_ENDPOINT
bucket_name = "crm-customer-audio"

# 初始化 OSS 客户端
auth = oss2.Auth(access_key, secret_key)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

# 本地文件路径
local_dir = "/home/myproject/crm_backend/media/customer_audio"

def upload_to_oss(local_file_path, oss_path):
    """上传文件到 OSS"""
    with open(local_file_path, "rb") as file_obj:
        bucket.put_object(oss_path, file_obj)
        print(f"Uploaded {local_file_path} to {oss_path}")

def migrate_audio_files():
    """迁移所有音频文件到 OSS"""
    for root, dirs, files in os.walk(local_dir):
        for file_name in files:
            local_file_path = os.path.join(root, file_name)

            # 生成 OSS 上的路径
            relative_path = os.path.relpath(local_file_path, local_dir)
            oss_path = f"customer_audio/{relative_path}"

            # 上传文件到 OSS
            upload_to_oss(local_file_path, oss_path)

if __name__ == "__main__":
    migrate_audio_files()