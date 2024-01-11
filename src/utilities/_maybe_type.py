"""The maybeType function takes a type or tuple of types followed by any
number of positional arguments and returns the first such that is of the
type or types indicated. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Union, Tuple, Type, Any

Types = Union[Type, Tuple[Type, ...]]


def maybeType(types: Types, *args) -> Any:
  """The maybeType function takes a type or tuple of types followed by any
  number of positional arguments and returns the first such that is of the
  type or types indicated. """

  if isinstance(types, type):
    return maybeType((types,), *args)
  for arg in args:
    if isinstance(arg, types):
      return arg
