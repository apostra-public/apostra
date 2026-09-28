from typing import TypeAlias, Union

JsonValue: TypeAlias = Union[str, int, float, bool, None, list["JsonValue"], dict[str, "JsonValue"]]
