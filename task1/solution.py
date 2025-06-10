from functools import wraps


def strict(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        annotations = func.__annotations__

        for name, values in zip(annotations.keys(), args):
            expected_type = annotations[name]
            if not isinstance(values, expected_type):
                raise TypeError(f"Аргумент {name} не соответствует типу {expected_type.__name__}")

        for name, values in kwargs.items():
            if name in annotations:
                expected_type = annotations[name]
                if not isinstance(values, expected_type):
                    raise TypeError(f"Аргумент {name} не соответствует типу {expected_type.__name__}")

        return func(*args, **kwargs)
    return wrapped


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))
# print(sum_two(1, 2.4))
