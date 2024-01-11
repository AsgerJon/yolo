"""The createDir function attempts to create a directory given by the
positional arguments that are first joined."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from utilities import maybeTypes, typeGuard, monoSpace


def createDir(*args, ) -> None:
  """The createDir function attempts to create a directory given by the
  positional arguments that are first joined."""
  strArgs = maybeTypes(str, *args)
  if len(strArgs) > 1:
    return createDir(os.path.join(*strArgs))
  if not strArgs:
    e = typeGuard('strArgs', strArgs, str)
    raise TypeError(e)
  dirName = strArgs[0]
  error = None
  try:
    os.makedirs(dirName, exist_ok=True)
  except PermissionError as permissionError:
    error = permissionError
  except OSError as osError:
    error = osError
  if error is not None:
    e = """The following error occurred when attempting to create 
    directory named '%s': %s""" % (dirName, error.__class__.__qualname__)
    raise error.__class__(monoSpace(e)) from error
