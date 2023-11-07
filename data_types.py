from typing import *

Time = NewType("Time", str)

Date = NewType("Date", str)

Text = NewType("Text", str)

DBOperationResult = NewType("DBOperationResult", Union[bool, str])