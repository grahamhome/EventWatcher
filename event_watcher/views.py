from pprint import pformat

import jsonschema
from django.http import HttpResponse
from django.shortcuts import render
from .models import Schema
import logging

create_schema_logger = logging.getLogger("eye.event_watcher.views.create_schema")

def validate_schema(self):
    try:
        jsonschema.Draft7Validator.check_schema(self.schema)
        return True
    except jsonschema.exceptions.SchemaError as e:
        # schema_logger.error(f"Rejected schema:\n{pformat(self.schema, indent=4)}\nError: {e.message}")
        return False

def index(request):
    return HttpResponse(status=200, content="Go away or I shall taunt you a second time")

def create_schema(request):
    if request.is_ajax() and request.method == "POST":
        data = request.body
        schema = Schema(**data)
        try:
            jsonschema.Draft7Validator.check_schema(schema.schema)
            return HttpResponse(status=201, content="Schema created!")
        except jsonschema.exceptions.SchemaError as e:
            create_schema_logger.error(f"Rejected schema:\n{pformat(schema.schema, indent=4)}\nError: {e.message}")
            return HttpResponse(status=422, content=e.message)


