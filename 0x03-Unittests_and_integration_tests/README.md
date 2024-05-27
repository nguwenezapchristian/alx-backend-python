# Unittests and Integration Tests

This project contains unit tests and integration tests for a Python project. The tests are implemented using the `unittest` framework and parameterized with `parameterized` library. Mocking of HTTP calls is done using `unittest.mock.patch`.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nguwenezapchristian/alx-backend-python.git
```

2. Navigate to the project directory:

```bash
cd alx-backend-python/0x03-Unittests_and_integration_tests
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Tests

To run all the tests, execute the following command:

```bash
python -m unittest
```

You can also run specific test files individually. For example, to run the tests in `test_utils.py`, use:

```bash
python -m unittest test_utils.py
```

## Test Files

- `test_utils.py`: Contains unit tests for utility functions.
- `test_client.py`: Contains unit tests for the GithubOrgClient class.
