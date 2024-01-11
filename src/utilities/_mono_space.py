"""The monoSpace function returns a given string with all consecutive
characters considered whitespace replaced by a single space."""
#  MIT Licence
#  Copyright (c) 2023-2024 Asger Jon Vistisen
from __future__ import annotations


def monoSpace(text: str, *args, **kwargs) -> str:
  """The monoSpace function takes a string as argument and returns it with
  all whitespace replaced with a single space. Include '<br>' to force a
  line break which is then placed after the whitespace replacement."""

  whiteSpace = ['\n', '\r', '\f', '\v']

  for symbol in whiteSpace:
    text = text.replace(symbol, ' ')

  _c = len(text)
  while '  ' in text and _c:
    text = text.replace('  ', ' ')
    _c -= 1
  if not _c:
    raise RuntimeError('While loop stuck!')

  newLineKwarg = kwargs.get('newLine', None)
  newLineArg = None
  for arg in args:
    if isinstance(arg, str) and newLineArg is None:
      newLineArg = arg
  newLineDefault = '<br>'
  newLine = None
  for arg in [newLineKwarg, newLineArg, newLineDefault]:
    if arg is not None and newLine is None:
      if isinstance(arg, str):
        newLine = newLineKwarg
      else:
        e = """Expected new-line character to be of type %s,<br> 
        but received: %s!"""
        raise TypeError(monoSpace(e % (str, type(newLine))))
  return text.replace('<br>', '\n')
