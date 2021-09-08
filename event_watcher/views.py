import asyncio
import json
from pprint import pformat

import jsonschema
from asgiref.sync import sync_to_async
from django.db import IntegrityError
from django.http import HttpResponse
from .models import Schema, Event
import logging
from django.views.decorators.csrf import csrf_exempt
import logging.config
import json
from .logging_config import logging_config
from jsonschema import ValidationError

logging.config.dictConfig(config=logging_config)

create_schema_logger = logging.getLogger("eye.event_watcher.views.create_schema")
create_event_logger = logging.getLogger("eye.event_watcher.views.create_event")

@csrf_exempt
def create_schema(request):
    if request.method == "POST":
        schema = Schema(**json.loads(request.body))
        try:
            jsonschema.Draft7Validator.check_schema(schema.schema)
            schema.save()
            return HttpResponse(status=201, content="Schema created!")
        except jsonschema.exceptions.SchemaError as e:
            create_schema_logger.error(f"Rejected schema:\n{pformat(schema.__dict__, indent=4)}\nError: {e}")
            return HttpResponse(status=422, content=e)
        except IntegrityError as e:
            create_schema_logger.error(f"Rejected schema:\n{pformat(schema.__dict__, indent=4)}\nError: {e}")
            return HttpResponse(status=422, content=e)

@csrf_exempt
async def create_events(request):
    # if request.method == "POST":
    #     await asyncio.gather(map(create_event, **json.loads(request.body)))
    return HttpResponse(status=200)


def create_event(event):
    schemas = Schema.objects.filter(categoty=event.get("category"), name=event.get("name"))
    if not schemas:
        create_event_logger.error(f"No schema found for event {event.get('category')}:{event.get('name')}")
        return False
    else:
        schema = schemas[0]
        event = Event(**event, schema=schema)
        try:
            jsonschema.Draft7Validator(schema=schema.schema).validate(event.get("data"))
            event.save()
        except ValidationError as e:
            create_schema_logger.error(f"Rejected event:\n{pformat(event.__dict__, indent=4)}\nError: {e}")
        except IntegrityError as e:
            create_schema_logger.error(f"Rejected event:\n{pformat(event.__dict__, indent=4)}\nError: {e}")







