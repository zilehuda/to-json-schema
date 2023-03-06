import pytest

from to_json_schema.to_json_schema import SchemaBuilder


def test_to_json_schema():
    schema_builder = SchemaBuilder()
    assert schema_builder.to_json_schema({}) == {"type": "object"}
    assert schema_builder.to_json_schema([]) == {"type": "array"}
    assert schema_builder.to_json_schema({"ping": "poing"}) == {
        "type": "object",
        "properties": {"ping": {"type": "string"}},
    }
    assert schema_builder.to_json_schema({"array": []}) == {
        "type": "object",
        "properties": {"array": {"type": "array"}},
    }

def test_to_json_schema_invalid_input():
    schema_builder = SchemaBuilder()
    with pytest.raises(TypeError):
        assert schema_builder.to_json_schema(None)




