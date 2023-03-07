===================
to-json-schema
===================

A simple package that convert dictionary or a list into json-schema using the OpenAPI standards.

Installation
------------

to-json-schema can be installed via ``pip``:

.. code-block:: sh

   $ pip install to-json-schema

Quickstart
----------

You can now convert your python dict into json-schema:

.. code-block:: python

   from to_json_schema.to_json_schema import SchemaBuilder

    data = {
        "country": "Pakistan",
        "city": "Karachi",
        "population": 16051521,
        "is_capital": False,
        "key_qualities": ["food", "multi-cultural"],
    }

    schema_builder = SchemaBuilder()
    json_schema = schema_builder.to_json_schema(data)

    >>> {'type': 'object', 'properties': {'country': {'type': 'string'}, 'city': {'type': 'string'}, 'population': {'type': 'integer'}, 'is_capital': {'type': 'boolean'}, 'key_qualities': {'type': 'array', 'items': {'type': 'string'}}}}

You can also convert list of dict, string, integer into-json schema

.. code-block:: python
    
    from to_json_schema.to_json_schema import SchemaBuilder

    data = [{"foo": 12, "bar": 14}, {"moo": 52, "car": 641}, {"doo": 6, "tar": 84}]

    schema_builder = SchemaBuilder()
    json_schema = schema_builder.to_json_schema(data)
    
    >>> {'type': 'array', 'items': {'type': 'object', 'properties': {'foo': {'type': 'integer'}, 'bar': {'type': 'integer'}, 'moo': {'type': 'integer'}, 'car': {'type': 'integer'}, 'doo': {'type': 'integer'}, 'tar': {'type': 'integer'}}}}

