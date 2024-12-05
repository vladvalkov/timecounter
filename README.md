# timecounter
A simple time-based counter for Python.
## Installation
I recommend `uv` as a tool for package management.
### uv
```bash
uv add git+https://github.com/vladvalkov/timecounter
```

### pip
```bash
pip install git+https://github.com/vladvalkov/timecounter
```

## Quick start
```python
import time
from timecounter import TimeCounter

tc = TimeCounter(retention=120, bucket=1) # Retain 120 seconds of data, bucketed by 1 second
tc.add(10) # Add 10 to the counter
time.sleep(1) # Simulate some work or delay
tc.add(20) # Add 20 to the counter

tc.last(2) # 30
```