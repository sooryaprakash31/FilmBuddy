from cerberus import Validator
from flask import abort

from ..utils import convert


class RequestValidationService:

    def __init__(self, request):
        self.request = request
        self.schema = {}
        self.update_schema()

    def update_schema(self):
        self.schema.update({
            "controller.recommend": {
                "body": {
                    "title": {
                        "type": "string",
                        "required": True,
                        "empty": False
                    },
                    "year": {
                        "type": "integer",
                        "coerce": "to_int",
                        "required": True,
                        "empty": False
                    },
                    "recommendations_count": {
                        "type": "integer",
                        "coerce": "to_int",
                        "required": False,
                        "empty": False
                    },
                    "rating_filter": {
                        "type": "float",
                        "coerce": "to_float",
                        "max": 5.0,
                        "required": False,
                        "empty": False
                    },
                    "popularity_percentage": {
                        "type": "float",
                        "min": 0,
                        "max": 100,
                        "coerce": "to_percentage",
                        "required": False,
                        "empty": False
                    }
                }
            },
            "controller.search": {
                "body": {
                    "title": {
                        "type": "string",
                        "required": True,
                        "empty": False
                    },
                    "year": {
                        "type": "integer",
                        "coerce": "to_int",
                        "required": False,
                        "empty": False
                    },
                    "count": {
                        "type": "integer",
                        "coerce": "to_int",
                        "required": False,
                        "empty": False
                    }
                }
            }
        })

    def __body_validator(self):
        schema = self.schema.get(self.request.endpoint).get("body")
        data = self.request.form.to_dict(flat=True)
        validator = RequestValidator(schema)
        is_validated = validator.validate(data)

        if not is_validated:
            abort(400, validator.errors)
        else:
            return validator.document

    def validate_data(self):
        return self.__body_validator()


class RequestValidator(Validator):

    def _normalize_coerce_to_int(self, value):
        return convert(value=value, to="int", on_error="return_value")

    def _normalize_coerce_to_float(self, value):
        return convert(value=value, to="float", on_error="return_value")

    def _normalize_coerce_to_percentage(self, value):
        value = convert(value=value, to="float", on_error="return_value")
        return value / 100

