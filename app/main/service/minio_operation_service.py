import os
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
from app.main.util.DynamicUtil import DynamicUtil


class MinioOperation:
    def __init__(self):
        dyutil = DynamicUtil('config.ini')
        self.host = dyutil.config.get('minio', 'host')
        self.access_key = dyutil.config.get('minio', 'access_key')
        self.secret_key = dyutil.config.get('minio', 'secret_key')


        self.minioClient = Minio(self.host,
                                 access_key=self.access_key,
                                 secret_key=self.secret_key,
                                 secure=True)

    def create(self, bucket_name):
        try:
            self.minioClient.make_bucket(bucket_name=bucket_name)
            self.minioClient.enable_bucket_versioning(bucket_name)
            return {
                "bucket_name": bucket_name,
                "status_code": 200
            }
        except BucketAlreadyOwnedByYou as err:
            pass
        except BucketAlreadyExists as err:
            pass
        except ResponseError as err:
            raise


    def read(self, bucket_name):
        objects = self.minioClient.list_objects(bucket_name, recursive=True)
        print(objects)
        file_list = []
        for obj in objects:
            try:
                file_name = obj.object_name.encode('utf-8')
                print(file_name)
                file_list.append(file_name)
                # file_name = file_name.decode('utf-8')
                # data = self.minioClient.get_object(bucket_name, file_name)
                # file_path, file = os.path.split(os.path.abspath(file_name))

                # isdir = os.path.isdir(file_path)
                # if not isdir:
                #     os.makedirs(file_path)
                #
                # with open(file_name, 'wb') as file_data:
                #     for d in data.stream(32 * 1024):
                #         file_data.write(d)

                return {
                    "bucket_name": bucket_name,
                    "files": file_list,
                    "status_code": 200
                }
            except ResponseError as err:
                print("Error in MinioOperationService.read(): ", err)
                return {
                    "error_message": err,
                    "status_code": 500
                }


    def upload(self, bucket_name, object_name, filepath):
        try:
            self.minioClient.fput_object(str(bucket_name), str(object_name), filepath)
        except ResponseError as err:
            print("Error in MinioOperationService.upload(): ", err)


    def list_bucket_objects(self, bucket_name):
        try:
            objects = self.minioClient.list_objects(bucket_name, recursive=True)
            for obj in objects:
                print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
                      obj.etag, obj.size, obj.content_type)
        except ResponseError as err:
            print("Error in MinioOperationService.listBucketObjects(): ", err)


    def delete(self, bucket_name):
        objects = self.minioClient.list_objects(bucket_name, recursive=True)
        print(objects)
        for obj in objects:
            try:
                print("OBJECT : ", objects)
                self.minioClient.remove_object(bucket_name, obj)
                return {
                    "bucket_name": bucket_name,
                    "status_code": 200
                }
            except ResponseError as err:
                print("Error in MinioOperationService.delete(): ", err)


    def get_stats(self, bucket_name, object_name):
        try:
            stat = self.minioClient.stat_object(bucket_name, object_name)
            return stat
        except ResponseError as err:
            print("Error in MinioOperationService.get_stats(): ", err)

