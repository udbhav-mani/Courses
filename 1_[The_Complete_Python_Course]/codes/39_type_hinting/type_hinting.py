from typing import List, Dict, Union

name: str = "Raj"
# Now this can be used anywhere as a data type
dict1 = List[Dict[str, Union[str, int]]]


def type_hint(name) -> str:
    return name


print(type_hint("home"))
