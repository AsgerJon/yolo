"""The typeGuard function creates an appropriate error message for a named
argument expected to be of a given type, including the actual type."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def typeGuard(name: str, obj: object, *expType: type, ) -> str:
  """The typeGuard function creates an appropriate error message for a named
  argument expected to be of a given type, including the actual type."""
  typeArgs = [arg for arg in expType if isinstance(arg, type)]
  if not typeArgs:
    raise TypeError('Received no types!')
  if isinstance(obj, (*typeArgs,)):
    return 'No type related error indicated'
  actTypeMsg = type(obj).__qualname__
  objMsg = str(obj)
  expTypeMsg = None
  if len(typeArgs) == 1:
    typeName = typeArgs[0].__qualname__
    expTypeMsg = """'of type: '%s'""" % typeName
  if len(typeArgs) == 2:
    typeNames = [type_.__qualname__ for type_ in typeArgs]
    tN = typeNames
    expTypeMsg = """'of type: '%s or %s'""" % (tN[0], tN[1])
  if len(typeArgs) > 2:
    typeNames = [type_.__qualname__ for type_ in typeArgs]
    ending = '%s or %s' % (typeNames[-2], typeNames[-1])
    types = ', '.join([*typeNames[:-2], ending])
    expTypeMsg = 'to be one of: %s' % types
  e = """Expected '%s' %s, but received '%s' of type '%s'!"""
  return e % (name, expTypeMsg, objMsg, actTypeMsg)
