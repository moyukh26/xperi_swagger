# from flask import request, jsonify
# from flask_restplus import Resource
# from flask_cors import cross_origin
#
# from ..service.minio_operation_service import MinioOperation
# from ..util.dto import BucketDto
#
# api = BucketDto.api
# _bucket = BucketDto.bucket
#
#
# @api.route('/minio-bucket/<string:bucket_name>', endpoint='/minio-bucket')
# class MinioBucket(Resource):
#     @api.doc('get minio bucket information')
#     def get(self, bucket_name):
#         """Get Bucket Information"""
#         try:
#             minio_object = MinioOperation()
#             response_minio_object = minio_object.read_data_from_minio(bucket_name)
#             print(response_minio_object)
#             response = {"message": "All metadata related informations", "id": bucket_name}
#             return jsonify(response)
#         except Exception as ex:
#             response = {}
#             response["status"] = True
#             response["error"] = ex
#             return jsonify(response)
#
#
#
#     @api.response(201, 'Metadata successfully created.')
#     @api.doc('update a metadata')
#     def put(self, id):
#         """Update a Metadata"""
#         data = request.json
#         response = {"message": "Metadata successfully updated", "id": id}
#         return jsonify(response)
#
#     # @api.response(201, 'Metadata successfully created.')
#     # @api.doc('create a new metadata')
#     # @api.expect(_metadata, validate=True)
#     # def post(self):
#     #     """Create a new Metadata"""
#     #     data = request.json
#     #     response = {"message": "Metadata successfully created"}
#     #     return jsonify(response)
