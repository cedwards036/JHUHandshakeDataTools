import re
from typing import Set, List, Callable

from jhu_handshake_data_tools.src.major_prefixes import IN_PREFIXES, SPACE_PREFIXES


def make_major_cleaning_function(in_prefixes: Set[str], space_prefixes: List[str]) -> Callable[[str], str]:
    def clean_major(major: str) -> str:
        return clean_major_with_space_prefix(
            clean_major_with_in_prefix(
                clean_major_with_colon_prefix(major),
                in_prefixes),
            space_prefixes)

    return clean_major


def clean_major_with_colon_prefix(major: str) -> str:
    if ':' in major:
        return major.split(':', 1)[1].strip()
    else:
        return major


def clean_major_with_in_prefix(major: str, lookup: Set[str]) -> str:
    major_components = major.split(' in ', 1)
    if major_components[0] in lookup:
        return major_components[1]
    else:
        return major


def clean_major_with_space_prefix(major: str, lookup: List[str]) -> str:
    for prefix in lookup:
        match = re.match(rf'^{prefix}\s+(.+)$', major)
        if match:
            return match.groups()[0]
    return major


clean_major = make_major_cleaning_function(IN_PREFIXES, SPACE_PREFIXES)
