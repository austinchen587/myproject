from oss2 import Auth, Bucket
from django.core.files.storage import Storage
from django.conf import settings
from urllib.parse import urljoin


class AliyunOSSStorageBase(Storage):
    """
    基础阿里云 OSS 存储类，支持文件上传、URL 生成等功能。
    """

    def __init__(self, bucket_name=None, base_url=None):
        """
        初始化 OSS 存储基类
        :param bucket_name: OSS Bucket 名称
        :param base_url: Bucket 的基础 URL
        """
        self.bucket_name = bucket_name
        self.base_url = base_url

        if not self.bucket_name or not self.base_url:
            raise ValueError("bucket_name 和 base_url 必须提供")

        # 初始化 OSS 的认证和 Bucket 实例
        self.auth = Auth(settings.OSS_ACCESS_KEY_ID, settings.OSS_ACCESS_KEY_SECRET)
        self.bucket = Bucket(self.auth, settings.OSS_ENDPOINT, self.bucket_name)

    def _save(self, name, content):
        try:
            self.bucket.put_object(name, content.read())
            return name
        except Exception as e:
            raise IOError(f"Failed to upload file {name} to OSS: {str(e)}")

    def url(self, name):
        return urljoin(self.base_url, name)

    def exists(self, name):
        try:
            return self.bucket.object_exists(name)
        except Exception as e:
            raise IOError(f"Failed to check if file {name} exists in OSS: {str(e)}")

    def delete(self, name):
        try:
            self.bucket.delete_object(name)
            return True
        except Exception as e:
            raise IOError(f"Failed to delete file {name} from OSS: {str(e)}")


class AliyunOSSEmployeeStorage(AliyunOSSStorageBase):
    """
    专用于存储 Employee 文件的存储类
    """
    def __init__(self):
        super().__init__(
            bucket_name=settings.OSS_EMPLOYEE_BUCKET_NAME,
            base_url=settings.OSS_EMPLOYEE_BASE_URL
        )