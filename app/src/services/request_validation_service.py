from cerberus import Validator
from flask import abort

from ..utils import convert


class RequestValidationService:
    """
    Request validation related methods
    """

    def __init__(self, request):
        self.request = request
        self.schema = {}
        self.update_schema()

    def update_schema(self):
        self.schema.update({
            "controller.recommend": {
                "query_params": {
                    "recommendations_count": {
                        "type": "integer",
                        "coerce": "to_int",
                        "min": "1",
                        "required": False,
                        "empty": False
                    },
                    "rating_filter": {
                        "type": "float",
                        "coerce": "to_float",
                        "min": 0,
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
                    },
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
                    }
                },
            },
            "controller.search": {
                "query_params": {
                    "count": {
                        "type": "integer",
                        "coerce": "to_int",
                        "min": 1,
                        "required": False,
                        "empty": False
                    },
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
                },
            }
        })

    @staticmethod
    def __validator(data, schema):
        validator = RequestValidator(schema)
        is_validated = validator.validate(data)

        if not is_validated:
            abort(400, validator.errors)
        else:
            return validator.document

    def __body_validator(self, schema):
        data = self.request.form.to_dict(flat=True)
        return self.__validator(data=data, schema=schema)

    def __query_params_validator(self, schema):
        data = self.request.args.to_dict(flat=True)
        return self.__validator(data=data, schema=schema)

    def validate_data(self):
        """
        This method is used to validate the data against the schema
        :return: validated data
        """
        schema = self.schema.get(self.request.endpoint)
        validated_document = {}
        validated_document.update(self.__query_params_validator(schema=schema.get("query_params")))
        return validated_document


class RequestValidator(Validator):

    def _normalize_coerce_to_int(self, value):
        return convert(value=value, to="int", on_error="return_value")

    def _normalize_coerce_to_float(self, value):
        return convert(value=value, to="float", on_error="return_value")

    def _normalize_coerce_to_percentage(self, value):
        value = convert(value=value, to="float", on_error="return_value")
        return value / 100
