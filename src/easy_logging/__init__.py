"""EasyFormatter is a simple, customizable logging formatter for Python."""
from .styling import Ansi, Theme
from .config import FormatterConfig

__all__ = ["Ansi", "Theme", "FormatterConfig"]
