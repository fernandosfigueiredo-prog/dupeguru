# Copyright 2016 Virgil Dupras
#
# This software is licensed under the "GPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/gpl-3.0.html

try:
    from core.pe._cache import bytes_to_colors  # noqa
except ImportError:
    def bytes_to_colors(data):
        """Transform the bytes 'data' into a list of 3-sized tuples."""
        if not data:
            return []
        result = []
        end = (len(data) // 3) * 3
        for i in range(0, end, 3):
            result.append((data[i], data[i + 1], data[i + 2]))
        return result


def colors_to_bytes(colors):
    """Transform the 3 sized tuples 'colors' into a bytes string.

    [(0,100,255)] --> b'\x00d\xff'
    [(1,2,3),(4,5,6)] --> b'\x01\x02\x03\x04\x05\x06'
    """
    return b"".join(map(bytes, colors))
