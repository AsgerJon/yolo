"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
import os
from yolo import Yolo


@Yolo
def tester00() -> None:
  """Hello world!"""
  stuff = [os, sys, 'Hello world']
  for item in stuff:
    print(item)


with tester00 as yolo:
  yolo.echo()
