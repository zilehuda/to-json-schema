from to_json_schema.combine import combine_schemas
from to_json_schema.utils import get_json_schema_type


class SchemaBuilder:
    def __init__(self, *args, **kwargs):
        pass

    def to_json_schema(self, data) -> None:
        if data is None:
            raise TypeError("data type does not supported")

        return self.get_schema(data)

    def get_schema(self, value):
        value_type = get_json_schema_type(value)

        if value_type == "object":
            return self.get_object_schema(value)

        elif value_type == "array":
            return self.get_array_schema(value)

        else:
            return {"type": value_type}

    def get_object_schema(self, value: dict, *args, **kwargs):
        schema = {"type": "object"}
        properties = {}
        for key, _value in value.items():
            properties[key] = self.get_schema(_value)

        if properties:
            properties = {"properties": properties}

        return {
            "type": "object",
            **properties,
        }

    def get_array_schema(self, values: list, *args, **kwargs):
        schema_type = "array"

        schemas = []
        for value in values:
            schemas.append(self.get_schema(value))

        items = {"items": combine_schemas(schemas)} if schemas else {}

        return {
            "type": schema_type,
            **items,
        }
