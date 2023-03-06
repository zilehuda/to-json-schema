from itertools import groupby

from to_json_schema.constants import SCALAR_TYPES


def combine_schemas(schemas):
    res = None
    schemas.sort(key=lambda x: x["type"])
    schemas = [
        {"type": k, "schemas": list(v)}
        for k, v in groupby(schemas, key=lambda x: x["type"])
    ]
    if len(schemas) == 1:
        res = combine_everything(schemas[0]["schemas"])
    elif all([schema["type"] in SCALAR_TYPES for schema in schemas]):
        res = combine_types(schemas)
    else:
        res = {
            "anyOf": [combine_everything(grouped_schema["schemas"]) for grouped_schema in schemas]
        }

    return res


def combine_everything(schemas):
    combined_types = combine_types(schemas)
    combined_properties = combine_properties(schemas)
    combined_items = combine_items(schemas)

    return {
        **combined_types,
        **combined_properties,
        **combined_items,
    }


def combine_types(schemas):
    types = list(set(map(lambda schema: schema["type"], schemas)))
    return {
        "type": types[0] if len(types) == 1 else types,
    }


def combine_properties(schemas):
    properties = {}
    schema_props = {}
    for schema in schemas:
        props: dict = schema.get("properties", {})
        for k, v in props.items():
            if k in schema_props:
                schema_props[k].append(v)
            else:
                schema_props[k]: list = [v]

    if len(schema_props) == 0:
        return {}

    for k, v in schema_props.items():
        properties[k] = combine_schemas(v)
    return {"properties": properties}


def combine_items(schemas):
    items = []
    for schema in schemas:
        _items = schema.get("items")
        if _items:
            items.append(_items)
    
    if len(items) == 0:
        return {}

    return {
        "items": items[0] if len(items) == 1 else items,
    }
