import typing


def convert(value: typing.Any, to: str, on_error: str):
    try:
        if to == "int":
            value = int(value)
        elif to == "float":
            value = float(value)
        elif to == "str":
            value = str(value)
        return value
    except Exception as e:
        if on_error == "return_value":
            return value
        elif on_error == "raise_exception":
            raise Exception(e)


