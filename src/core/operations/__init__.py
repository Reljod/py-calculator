
from dataclasses import dataclass

from src.core.operations.basic import BasicOperatorPlugins


@dataclass
class OperatorPlugins:
    basic: BasicOperatorPlugins


class Operator:
    def __init__(self, plugins: OperatorPlugins | None = None):
        self.plugins = plugins
