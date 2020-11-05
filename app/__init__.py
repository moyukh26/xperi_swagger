# app/__init__.py
from flask_restplus import Api
from flask import Blueprint

from .main.controller.metadata_controller import api as metadata_ns
# from .main.controller.minio_bucket_controller import api as bucket_ns
from .main.controller.crud_operations import api as crud_create_ns
from .main.controller.crud_operations import read_api as crud_read_ns
from .main.controller.crud_operations import update_api as crud_update_ns
from .main.controller.crud_operations import delete_api as crud_delete_ns



blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Xperi Backend',
          version='1.0',
          description='Powered by Xperi'
          )

api.add_namespace(metadata_ns, path='/v1')
api.add_namespace(crud_create_ns, path='/v1')
api.add_namespace(crud_read_ns, path='/v1')
api.add_namespace(crud_update_ns, path='/v1')
api.add_namespace(crud_delete_ns, path='/v1')
