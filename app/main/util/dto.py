from flask_restplus import Namespace, fields


class MetadataDto:
    api = Namespace('Metadata', description='metadata related operations')
    metadata = api.model('Metadata', {
        'id': fields.String(required=True, description='metadata id'),
        'name': fields.String(required=False, description='metadata name')
    })


# class BucketDto:
#     api = Namespace('Bucket', description='MinIO bucket related operations')
#     bucket = api.model('Bucket', {
#         'bucket_name': fields.String(required=True, description='MinIO bucket name'),
#         'object_name': fields.String(required=False, description='MinIO Object name in a bucket'),
#         'filepath': fields.String(required=False, description='Filepath'),
#         'location': fields.String(required=False, description='location'),
#         'content_type': fields.String(required=False, description='content_type'),
#     })

class CreateDto:
    api = Namespace('Create_Asset', description='CRUD Operation - CREATE')
    create_model = api.model('CREATE', {
        'name': fields.String(required=True, description='Asset name'),
        'source': fields.String(required=True, description='Source File Path'),
        'destination': fields.String(required=True, description='Collection Name')
    })


class ReadDto:
    api = Namespace('READ', description='CRUD Operation - READ')
    read_model = api.model('READ', {
        'type': fields.String(required=True, description='Resource Type'),
        'identifier': fields.String(required=True, description='Resource name'),
        'applicationType': fields.String(required=True, description='Application name')
    })


class UpdateDto:
    api = Namespace('UPDATE', description='CRUD Operation - UPDATE')
    update_model = api.model('UPDATE', {
        'type': fields.String(required=True, description='Resource Type'),
        'identifier': fields.String(required=True, description='Resource name'),
        'object': fields.String(required=True, description='Resource Type'),
        'filepath': fields.String(required=True, description='Resource name'),
        'applicationType': fields.String(required=True, description='Application name')
    })

class DeleteDto:
    api = Namespace('DELETE', description='CRUD Operation - DELETE')
    delete_model = api.model('DELETE', {
        'type': fields.String(required=True, description='Resource Type'),
        'identifier': fields.String(required=True, description='Resource name'),
        'applicationType': fields.String(required=True, description='Application name')
    })

