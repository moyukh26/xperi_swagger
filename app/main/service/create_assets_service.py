import os
import json
import datetime
import getpass
from app.main.service.minio_operation_service import MinioOperation
from app.main.util.DynamicUtil import DynamicUtil


class CreateAsset():
    def __init__(
            self,
            name: str = None,
            source_path: str = None,
            destination: str = None,
    ):

        dyutil = DynamicUtil('config.ini')
        self.name = name
        self.source_path = source_path
        self.destination = destination
        self.bucket_name = dyutil.config.get('minio', 'bucket_name')
        # self.upload_assets()
        # self.create_asset_metadata()

    def upload_assets(self):
        try:
            minio_object = MinioOperation()
            minio_object.upload(self.bucket_name, self.name, self.source_path)
        except Exception as e:
            print("Error in CreateAssetsService.uploadAssets(): ", e)

    def create_asset_metadata(self):
        try:
            asset_metadata = {}
            collection_list = []
            collection_list.append(self.destination)
            minio_object = MinioOperation()
            stats = minio_object.get_stats(self.bucket_name, self.name)

            asset_metadata["version_id"] = stats.version_id
            asset_metadata["created_at"] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            asset_metadata["is_encrypted"] = False
            asset_metadata["content-type"] = stats.content_type
            asset_metadata["content_length"] = stats.size
            asset_metadata["last_modified"] = datetime.datetime(*stats.last_modified[:6]).strftime('%m/%d/%Y %H:%M:%S')
            asset_metadata["URL"] = ""
            asset_metadata["is_deleted"] = False
            asset_metadata["collection_id"] = collection_list
            asset_metadata["name"] = self.name
            asset_metadata["description"] = "This is an asset"
            asset_metadata["created_by_user_id"] = getpass.getuser()

            json_object = json.dumps(asset_metadata, indent=4)
            filepath = "asset/" + self.name + ".json"
            filepath = os.path.join(os.getcwd(), filepath)

            with open(filepath, "w") as outfile:
                outfile.write(json_object)

            return json_object
        except Exception as e:
            print("Error in CreateAssetsService.createAssetMetadata(): ", e)

