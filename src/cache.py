"""Compressed KV cache utilities."""

from dataclasses import dataclass, field


@dataclass
class QuartzCache:
    rank: int = 32
    keys: list = field(default_factory=list)
    values: list = field(default_factory=list)

    def append(self, key, value):
        self.keys.append(key)
        self.values.append(value)
