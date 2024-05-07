# Python Async Comprehension

### Task 0: Async Generator

**Description:**
Write a coroutine called `async_generator` that loops 10 times, each time asynchronously waiting for 1 second, then yielding a random number between 0 and 10.

**File:** `0-async_generator.py`

```python
#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Task 1: Async Comprehensions

**Description:**
Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`.

**File:** `1-async_comprehension.py`

```python
#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform
from itertools import repeat

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

async def async_comprehension() -> List[float]:
    return [number async for number in async_generator()]
```

### Task 2: Runtime for Four Parallel Comprehensions

**Description:**
Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather()`. It measures the total runtime and returns it.

**File:** `2-measure_runtime.py`

```python
#!/usr/bin/env python3

import asyncio
from typing import List
from time import time

async def measure_runtime() -> float:
    start_time = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time()
    return end_time - start_time
```

### Execution Example:

```python
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
```

**Output:**
```
10.013471995996952
```

### Repository Details:

- **GitHub Repository:** alx-backend-python
- **Directory:** 0x02-python_async_comprehension