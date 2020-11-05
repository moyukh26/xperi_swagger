import os
import json
import datetime
import getpass
from app.main.service.minio_operation_service import MinioOperation
from app.main.util.DynamicUtil import DynamicUtil


class CreateCollection():
    def __init__(
            self,
            name: str = None,
            description: str = None,
            asset_list: str = None,
    ):
        if self.asset_list is None:
            self.name = name
            self.description = description
        else:
            self.name = name
            self.description = description
            self.asset_list = asset_list

    def create_collection(self):
        try:
            collection = {}

            collection["collection_id"] = "C1"
            collection["name"] = self.name
            collection["status"] = "Active"
            collection["asset_attributes_array"] = []
            collection["collection_tags_array"] = []
            collection["owner_id"] = "007"
            collection["version_id"] = "2"
            collection["created_at"] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            collection["is_encrypted"] = False
            collection["content-type"] = "application/json"
            collection["content_length"] = "2048"
            collection["last_modified"] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            collection["content-MD5"] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            collection["URL"] = ""
            collection["is_deleted"] = False
            collection["description"] = "This is a Collection"
            collection["review_status"] = "Reviewed"
            collection["is_locked"] = False
            collection["last_review_date"] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            collection["created_by_user_id"] = getpass.getuser()

            json_object = json.dumps(collection, indent=4)
            filepath = "asset/" + self.name + ".json"
            filepath = os.path.join(os.getcwd(), filepath)

            with open(filepath, "w") as outfile:
                outfile.write(json_object)

            return json_object
        except Exception as e:
            print("Error in CreateAssetsService.createAssetMetadata(): ", e)

