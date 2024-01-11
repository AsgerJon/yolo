"""AbstractField provides an abstract baseclass for descriptor classes.
Subclasses should implement:
  _explicitGetter
  _explicitSetter
  _explicitDeleter
as is needed. None of the above are strictly required, but the default
implementation raises an AttributeError if an instance of a subclass
invokes an accessor method not implemented by the subclass."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
