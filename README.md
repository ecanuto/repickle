# Repickle

Repickle makes it possible to serialize Python constructs not supported by the
default pickle module from the Python standard library. Repickle just extends
[cloudpickle](https://github.com/cloudpipe/cloudpickle) and add support for
load and dump to files.

## Installation

The latest release of `repickle` is available from
[pypi](https://pypi.python.org/pypi/repickle):

    pip install repickle


## Examples

Pickling a lambda expression:

```python
>>> import repickle
>>> squared = lambda x: x ** 2
>>> repickle.dump_to_file(squared, "pickled_lambda.pkl")

>>> new_squared = repickle.load_from_file("pickled_lambda.pkl")
>>> new_squared(2)
4
```

Pickling a function interactively defined in a Python shell session
(in the `__main__` module):

```python
>>> CONSTANT = 42
>>> def my_function(data: int) -> int:
...     return data + CONSTANT
...
>>> import repickle
>>> repickle.dump_to_file(my_function, "pickled_lambda.pkl")
>>> depickled_function = repickle.load_from_file("pickled_lambda.pkl")
>>> depickled_function(43)
85
```
