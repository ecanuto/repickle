from .cloudpickle import load, loads, register_pickle_by_value  # noqa
from .cloudpickle_fast import dumps, dump  # noqa


def register_module(module):
    register_pickle_by_value(module)


def dump_to_file(object, filename):
    with open(filename, "wb") as file:
        dump(object, file, -1)


def load_from_file(filename):
    with open(filename, "rb") as file:
        return load(file)
