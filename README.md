# JHU Handshake Data Tools
This package consists of a series of tools useful for handling and cleaning data from JHU's Handshake environment.
### Majors
The `clean_major` function will clean a Handshake major to remove extraneous details such as concatenated degree information.

```python
from jhu_handshake_data_tools import clean_major

cleaned_major = clean_major('B.S. Comp Sci: English')  # 'English'
```