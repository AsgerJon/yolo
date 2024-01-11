"""The maybe function returns the first positional argument different from
'None'."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def maybe(*args) -> object:
  """Returns the first positional argument encountered that is different
  from 'None'."""
  for arg in args:
    if arg is not None:
      return arg
