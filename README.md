# Benchmark Utilities

[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://raw.githubusercontent.com/drkostas/bench-utils/master/LICENSE)

## About <a name = "about"></a>

A collection of benchmarking
tools. [PYPI Package](https://pypi.org/manage/project/bench-utils/releases/)

## Table of Contents

+ [Using the library](#using)
    + [Installing and using the library](#install_use)
+ [Manually install the library](#manual_install)
    + [Prerequisites](#configuration)
    + [Install the requirements](#installing_req)
+ [License](#license)

## Using the library <a name = "using"></a>

### Installing and using the library <a name = "install_use"></a>

First, you need to install the library either using pip:

```shell
$ pip install bench_utils
```

Then, import it and use it like so:

```python
from bench_utils import timeit, profileit

# --- Timeit --- #
# Context Manager
with timeit():
    # A code block
    pass


@timeit()
def my_func():
    # Function code
    pass


# --- Profileit --- #
# Context Manager
with profileit():
    # A code block
    pass


@profileit()
def my_func():
    # Function code
    pass
```

For more advanced examples
check [example_timeit.py](https://raw.githubusercontent.com/drkostas/bench-utils/master/example_timeit.py)
and [example_profileit.py](https://raw.githubusercontent.com/drkostas/bench-utils/master/example_profileit.py)
.

## Manually install the library <a name = "manual_install"></a>

These instructions will get you a copy of the project up and running on your local machine for
development and testing purposes. See deployment for notes on how to deploy the project on a live
system.

### Prerequisites <a name = "prerequisites"></a>

You need to have a machine with
[anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed and
any Bash based shell (e.g. zsh) installed.

```ShellSession

$ conda -V
conda 4.10.1

$ echo $SHELL
/usr/bin/zsh

```

### Install the requirements <a name = "installing_req"></a>

All the installation steps are being handled by
the [Makefile](https://raw.githubusercontent.com/drkostas/bench-utils/master/Makefile). First, create a
file called `~/.pypirc` with your pypi login details, as follows:

```
[pypi]
username = your_pypi_username
password = your_pypi_password
```

Then, modify the python version and everything else you need in
the [settings.ini](https://raw.githubusercontent.com/drkostas/bench-utils/master/settings.ini).

Finally, execute the following commands:

```ShellSession
$ make create_env
$ conda activate bench_utils
$ make release
```

## License <a name = "license"></a>

This project is licensed under the MIT License - see
the [LICENSE](https://raw.githubusercontent.com/drkostas/bench-utils/master/LICENSE) file for details.

<a href="https://www.buymeacoffee.com/drkostas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
