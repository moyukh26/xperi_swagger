from flask import request, jsonify
from flask_restplus import Resource
from flask_cors import cross_origin

from ..service.minio_operation_service import MinioOperation
from ..service.create_assets_service import CreateAsset
from ..util.dto import CreateDto
from ..util.dto import ReadDto
from ..util.dto import UpdateDto
from ..util.dto import DeleteDto

api = CreateDto.api
_create_model = CreateDto.create_model

read_api = ReadDto.api
_read_model = ReadDto.read_model

update_api = UpdateDto.api
_update_model = UpdateDto.update_model

delete_api = DeleteDto.api
_delete_model = DeleteDto.delete_model


@api.route('/create_asset/<name>,<source>,<destination>', endpoint='/create_asset')
class Create(Resource):
    # @api.doc('create a new Resource')
    # def get(self, bucket_name):
    #     """Get Bucket Information"""
    #     try:
    #         minio_object = MinioOperation()
    #         response_minio_object = minio_object.read_data_from_minio(bucket_name)
    #         print(response_minio_object)
    #         response = {"message": "All metadata related informations", "id": bucket_name}
    #         return jsonify(response)
    #     except Exception as ex:
    #         response = {}
    #         response["status"] = True
    #         response["error"] = ex
    #         return jsonify(response)



    # @api.response(201, 'Metadata successfully created.')
    @api.response(201, 'Created successfully.')
    @api.doc('Create a new Asset')
    def post(self, name, source, destination):
        """Create a New Asset"""
        asset_object = CreateAsset(
                            name=name,
                            source_path=source,
                            destination=destination
                        )
        asset_object.upload_assets()
        response_obj = asset_object.create_asset_metadata()
        return response_obj


@read_api.route('/read/<type>,<identifier>,<applicationType>', endpoint='/read')
class Read(Resource):
    @api.response(201, 'Read successfully.')
    @api.doc('Read from an Existing Resource')
    def post(self, type, identifier, applicationType):
        """Read from an Existing Resource"""
        response_obj = {}
        if applicationType.lower() == "minio":
            minio_object = MinioOperation()
            if type.lower() == "bucket":
                response_obj = minio_object.read(identifier)

        response = {"bucket_name": response_obj["bucket_name"], "files": str(response_obj["files"]), "status_code": 200}
        return jsonify(response)


@delete_api.route('/delete/<type>,<identifier>,<applicationType>', endpoint='/delete')
class Read(Resource):
    @api.response(201, 'Deleted successfully.')
    @api.doc('Delete from an Existing Resource')
    def post(self, type, identifier, applicationType):
        """Delete from an Existing Resource"""
        response_obj = {}
        if applicationType.lower() == "minio":
            minio_object = MinioOperation()
            if type.lower() == "bucket":
                response_obj = minio_object.delete(identifier)

        response = {"bucket_name": response_obj["bucket_name"], "message": "Deleted successfully ", "status_code": 200}
        return jsonify(response)

