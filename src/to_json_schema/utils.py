def get_json_schema_type(value):
    value_type = type(value)

    if value_type == dict:
        return "object"

    elif value_type == list:
        return "array"

    elif value_type == str:
        return "string"

    elif value_type == bool:
        return "boolean"

    elif value_type == int:
        return "integer"

    elif value_type == float:
        return "number"
    else:
        return "null"
