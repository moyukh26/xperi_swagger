from flask import request, jsonify
from flask_restplus import Resource
from flask_cors import cross_origin

from ..util.dto import MetadataDto

api = MetadataDto.api
_metadata = MetadataDto.metadata


@api.route('/metadata/<string:id>', endpoint = '/metadata')
# @cross_origin()
class UserList(Resource):
    @api.doc('get metadata')
    # @api.marshal_list_with(_metadata, envelope='data')
    # @api.param('id', 'The Metadata identifier')
    def get(self, id):
        """List all metadata"""
        response = {"message": "All metadata related informations", "id" : id}
        return jsonify(response)

    @api.response(201, 'Metadata successfully created.')
    @api.doc('update a metadata')
    def put(self, id):
        """Update a Metadata"""
        data = request.json
        response = {"message": "Metadata successfully updated", "id" : id}
        return jsonify(response)

    # @api.response(201, 'Metadata successfully created.')
    # @api.doc('create a new metadata')
    # @api.expect(_metadata, validate=True)
    # def post(self):
    #     """Create a new Metadata"""
    #     data = request.json
    #     response = {"message": "Metadata successfully created"}
    #     return jsonify(response)