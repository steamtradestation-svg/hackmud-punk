import re
from typing import Optional

def find_trigger(line: str, pattern: str) -> Optional[re.Match]:
    try:
        return re.search(pattern, line)
    except re.error:
        return None
