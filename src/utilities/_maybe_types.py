"""The maybeType function takes a type or tuple of types followed by any
number of positional arguments and returns a list, possibly empty, of any
positional arguments belonging to the type or types indicated."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Union, Tuple, Type, Any, List

Types = Union[Type, Tuple[Type, ...]]


def maybeTypes(types: Types, *args) -> List[Any]:
  """The maybeType function takes a type or tuple of types followed by any
  number of positional arguments and returns a list, possibly empty, of any
  positional arguments belonging to the type or types indicated."""
  if isinstance(types, type):
    return maybeTypes((types,), *args)
  typeArgs = []
  for arg in args:
    if isinstance(arg, types):
      typeArgs.append(arg)
  return typeArgs
