import oss2
from django.core.files.storage import Storage
from django.conf import settings
from urllib.parse import urljoin


class AliyunOSSStorage(Storage):
    """
    Custom storage for Aliyun OSS.
    """
    def __init__(self, access_key=None, secret_key=None, endpoint=None, bucket_name=None):
        self.access_key = access_key or settings.OSS_ACCESS_KEY_ID
        self.secret_key = secret_key or settings.OSS_ACCESS_KEY_SECRET
        self.endpoint = endpoint or settings.OSS_ENDPOINT
        self.bucket_name = bucket_name or settings.OSS_BUCKET_NAME

        # Initialize the OSS Bucket
        self.auth = oss2.Auth(self.access_key, self.secret_key)
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)

    def _save(self, name, content):
        # Save the file to OSS
        self.bucket.put_object(name, content.read())
        return name

    def url(self, name):
        # Generate the public URL for the file
        return urljoin(f"https://{self.bucket_name}.{self.endpoint}", name)

    def exists(self, name):
        # Check if a file exists in OSS
        return self.bucket.object_exists(name)