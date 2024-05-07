# Python - Async

This directory contains Python scripts demonstrating asynchronous programming concepts using asyncio.

## Files:

### 0-basic_async_syntax.py
This file contains a basic asynchronous coroutine named `wait_random`. It takes an integer argument `max_delay` (default value: 10) and waits for a random delay between 0 and `max_delay` seconds (inclusive) before returning the delay value.

### 1-concurrent_coroutines.py
This file imports the `wait_random` function from `0-basic_async_syntax` and defines an asynchronous routine named `wait_n`. It takes two integer arguments, `n` and `max_delay`, and spawns `wait_random` `n` times with the specified `max_delay`. The function returns a list of all the delays (float values) in ascending order without using `sort()` due to concurrency.

### 2-measure_runtime.py
This file imports the `wait_n` function from the previous file and defines a function named `measure_time`. It takes two integer arguments, `n` and `max_delay`, measures the total execution time for `wait_n(n, max_delay)`, and returns the average time per call.

### 3-tasks.py
This file imports the `wait_random` function from `0-basic_async_syntax` and defines a function named `task_wait_random`. It takes an integer argument `max_delay` and returns an asyncio Task.

### 4-tasks.py
This file is similar to `1-concurrent_coroutines.py`, but it takes the code from `wait_n` and alters it into a new function named `task_wait_n`. The function is nearly identical to `wait_n`, except `task_wait_random` is being called.