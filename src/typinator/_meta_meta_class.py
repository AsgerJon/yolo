"""The MetaTypinator class provides a shared meta-metaclass exposing a few
metaclass level methods otherwise inaccessible.

There are no dragons here."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


class _MetaTypinator(type):
  """The MetaTypinator class provides a shared meta-metaclass exposing a few
  metaclass level methods otherwise inaccessible.

  There are no dragons here."""

  def __str__(cls, ) -> str:
    """String representation"""
    return cls.__qualname__

  def __repr__(cls, ) -> str:
    """Code representation"""
    namespace = dict.__str__(getattr(cls, '__dict__'))
    return 'MetaTypinator(%s, (), %s)' % (cls.__name__, namespace)


class MetaTypinator(_MetaTypinator, metaclass=_MetaTypinator):
  """In between class exposing the meta-metaclass"""
  pass
