from django.db import models
import logging
from pprint import pformat
import jsonschema


schema_logger = logging.getLogger("event_watcher.models.Schema")


class Schema(models.Model):
    """
    An event schema.
    """
    category = models.CharField(max_length=255, default=None)
    name = models.CharField(max_length=255, default=None)
    schema = models.JSONField(default=None)

    class Meta:

        constraints = [
            models.UniqueConstraint(name="OneSchemaPerCategoryName", fields=["category", "name"])
        ]

    def __str__(self):
        return f"Schema for {self.category}:{self.name}"


class Event(models.Model):
    """
    An event.
    """
    session_id = models.UUIDField()
    timestamp = models.DateTimeField()
    schema = models.ForeignKey(Schema, on_delete=models.SET_NULL, null=True)
    data = models.JSONField()



    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             name="SchemaExists",
    #             check=(
    #                 Schema.objects.filter(
    #                     models.Q(
    #                         category=models.F("category"),
    #                         name=models.F("name")
    #                     )
    #                 ).exists()
    #             ))
    #     ]
