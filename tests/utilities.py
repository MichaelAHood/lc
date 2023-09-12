from dataclasses import dataclass
from typing import Any


@dataclass
class TestCase:
    __test__ = False
    input: Any
    want: Any
