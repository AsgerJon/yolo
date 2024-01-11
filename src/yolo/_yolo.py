"""The Yolo provides the class central to the yolo module."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
import os
from io import StringIO
from typing import Callable, Optional
from types import TracebackType
from warnings import warn

from utilities import maybeTypes, maybeType, maybe, typeGuard, monoSpace, \
  createDir, timeStamp

Error = Optional[BaseException]
TBType = Optional[TracebackType]
EType = Optional[type]


class Yolo:
  """The Yolo provides the class central to the yolo module."""

  __log_dir__ = os.getenv('YOLODIR', os.path.abspath(__file__))
  __log_base_filename__ = 'yolog_<when>'
  __log_name__ = 'main'
  __log_ext__ = 'log'

  def __init__(self, callMeMaybe: Callable, *args, **kwargs) -> None:
    self.__inner_function__ = callMeMaybe
    self.__inside_context__ = False
    self.__format_spec__ = None
    self.__explicit_name__ = None
    self.__explicit_project_name__ = None
    self.__explicit_dir__ = None
    self.__explicit_base_filename__ = None
    self.__explicit_ext__ = None
    #  Control flags
    self.__post_exit_echo__ = False
    self.__echo_log_file__ = False
    self.__captured_stdout__ = StringIO()
    self.__captured_stderr__ = StringIO()
    self.__original_stdout__ = sys.stdout
    self.__original_stderr__ = sys.stderr

  def __set_name__(self, owner: type, name: str) -> None:
    print('__set_name__')
    print(owner, name)

  def _getProjectName(self) -> str:
    """Getter-function for the current project name. """
    explicitProjectName = self.__explicit_project_name__
    funcName = getattr(self.__inner_function__, '__name__', None)
    dirName = os.path.dirname(sys.argv[0])
    projectName = maybeType(str, explicitProjectName, funcName, dirName)
    if isinstance(projectName, str):
      return projectName
    return self.__class__.__module__

  def _getBaseFileName(self) -> str:
    """Getter-function for the base file name. Please note, that this name
    should include '<when>' which will be replaced by a suitable
    timestamp. If missing '<when>' will be appended to the end of the
    name."""
    explicitName = self.__explicit_base_filename__
    fallbackName = self.__class__.__log_base_filename__
    name = maybeType(str, explicitName, fallbackName)
    if isinstance(name, str):
      return name
    e = typeGuard('name', name, str)
    raise TypeError(e)

  def _getLogExtension(self) -> str:
    """Getter-function for the log file extension. This can be set
    explicitly, but defaults to 'log'. """
    explicitExt = self.__explicit_ext__
    fallbackExt = self.__class__.__log_ext__
    ext = maybeType(str, explicitExt, fallbackExt)
    if isinstance(ext, str):
      return ext
    e = typeGuard('ext', ext, str)
    raise TypeError(e)

  def _getLogFileName(self) -> str:
    """Getter-function for log file name. This is distinct from log name,
    as it appends a timestamp and specified file extension."""
    base = self._getBaseFileName()
    ext = self._getLogExtension()
    timedName = timeStamp(base, '<when>', )
    return '%s.%s' % (timedName, ext)

  def _getLogDir(self, **kwargs) -> str:
    """Getter-function for directory intended to contain the log files"""
    explicitDir = self.__explicit_dir__
    fallbackDir = self.__class__.__log_dir__
    logDir = maybeType(str, explicitDir, fallbackDir)
    if isinstance(logDir, str):
      logDir = os.path.dirname(logDir)
      if os.path.isdir(logDir):
        return logDir
      if kwargs.get('_recursion', False):
        e = """Encountered inescapable recursion loop when attempting to 
        create the directory named: '%s' intended for log files!"""
        raise RecursionError(monoSpace(e % logDir))
      createDir(logDir)
      return self._getLogDir(_recursion=True)
    e = typeGuard('logDir', logDir, str)
    raise TypeError(e)

  def _getProjectLogDir(self, **kwargs) -> str:
    """Getter-function for the log directory for the named project.
    Generally, a directory in the general log directory is used. To
    specify a particular directory for a particular project, set an
    environment variable to the project name and a log directory will be
    placed there. """
    logDir = self._getLogDir()
    projectName = self._getProjectName()
    projectLogDir = os.path.join(logDir, projectName)
    if os.path.exists(projectLogDir):
      return projectLogDir
    if kwargs.get('_recursion', False):
      e = """Encountered inescapable recursion loop when attempting to 
      create the directory named: '%s' intended for log files generated 
      by the project named: '%s'!""" % (projectLogDir, projectName)
      raise RecursionError(e)
    createDir(projectLogDir)
    return self._getProjectLogDir(_recursion=True)

  def _getLogPath(self) -> str:
    """Getter-function for full file path at which to save log file"""
    logDir = self._getProjectLogDir()
    timedName = self._getLogFileName()
    return os.path.join(logDir, timedName)

  def __call__(self, *args, **kwargs) -> None:
    """Calling an instance runs the contained test function."""

  def _collectOutput(self, ) -> str:
    """Collects the output from the captured stdout, formats it and
    returns it."""
    return self.__captured_stdout__.getvalue()

  def _collectError(self, ) -> str:
    """Collects the out from the captured error stream, formats it and
    returns it."""
    return self.__captured_stderr__.getvalue()

  def log(self, *args, **kwargs) -> None:
    """Logs the file """
    logPath = self._getLogPath()
    if os.path.exists(logPath):
      e = """Expected filePath: '%s' to be available, but found a file 
      already present!"""
      raise FileExistsError(e)
    echoLogFile = kwargs.get('echoFilename', False)
    self.__echo_log_file__ = True if echoLogFile else False
    output = self._collectOutput()
    with open(logPath, 'w') as f:
      f.write(output)

  def echo(self, *args, **kwargs) -> None:
    """Sets the echo flag to True. Future version will allow
    customizations through arguments."""
    self.__post_exit_echo__ = True

  def getOutput(self) -> str:
    """Getter-function for captured output stream."""

  def getError(self) -> str:
    """Getter-function for captured error stream."""

  def __enter__(self) -> Yolo:
    """Replaces the standard output and error streams with those of this
    instance. """
    print("""Executing function: '%s'""" % self.__inner_function__.__name__)
    v = sys.version_info
    x, y, z = v.major, v.minor, v.micro
    print("""Running Python %s.%s.%s""" % (x, y, z)
    self.__inside_context__ = True
    self.__original_stdout__ = sys.stdout
    self.__original_stderr__ = sys.stderr
    self.__captured_stdout__ = StringIO()
    self.__captured_stderr__ = StringIO()
    sys.stdout = self.__captured_stdout__
    sys.stderr = self.__captured_stderr__
    self.__inner_function__()
    return self

  def __exit__(self, ecls: EType, err: Error, tb: TBType, ) -> None:
    """Restores original standard output and error streams. If errors were
    encountered they are then raised. """
    sys.stdout = self.__original_stdout__
    sys.stderr = self.__original_stderr__
    if ecls is None:
      if self.__post_exit_echo__:
        print(self._collectOutput())
        if self.__captured_stderr__:
          print(self._collectError())
      if self.__echo_log_file__:
        print('Log file saved to: %s' % self._getLogPath())
      self.__inside_context__ = False
      return
    raise err
