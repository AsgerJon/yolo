"""The timeStamp function appends a time to a given string such as a file
name. By default, the '<when>' will be replaced with the time of
invocation. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from datetime import datetime

from utilities import maybe, typeGuard


def timeStamp(msg: str, *args, **kwargs) -> str:
  """The timeStamp function appends a time to a given string such as a file
  name. By default, the '<when>' will be replaced with the time of
  invocation. """

  strArgs = [arg for arg in args if isinstance(arg, str)]
  placeholderKwarg = kwargs.get('placeholder', None)
  placeholderArg = [*strArgs, None][0]
  placeholderDefault = '<when>'
  placeholder = maybe(placeholderKwarg, placeholderArg, placeholderDefault)
  fmtSpecKwarg = kwargs.get('format', None)
  fmtSpecArg = [*strArgs, None, None][1]
  fmtSpecDefault = '%Y%m%d_%H%M%S'
  fmtSpec = str(maybe(fmtSpecKwarg, fmtSpecArg, fmtSpecDefault))
  if not isinstance(fmtSpec, str):
    e = typeGuard('fmtSpec', fmtSpec, str)
    raise TypeError(e)
  if isinstance(placeholder, str):
    when = datetime.now().strftime(fmtSpec)
    return msg.replace(placeholder, when)
  e = typeGuard('placeholder', placeholder, str)
  raise TypeError(e)
