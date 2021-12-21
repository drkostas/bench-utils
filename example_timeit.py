# pip install bench-utils
from bench_utils import timeit
import time


# --- Timeit as a decorator --- #

# Set custom print and use the function name and arguments as you want
@timeit(custom_print='Running {func_name} function with arguments {args} ({0} and {1})')
def run_something(a=1, b=2):
    for i in range(b):
        run_something_2(a)
        a += 1
    return "ok"


def run_something_2(c=3):
    return c ** 2


run_something(3, 5)

# --- Timeit as a Context Manager --- #

# Set custom print and use the duration argument as you want
# the `skip` argument is for skipping the timeit when desired
with timeit(custom_print='Code Block Time: {duration:2.5f} sec(s)', skip=False):
    for _ in range(2):
        time.sleep(0.1)

# The `internal_only` argument is for not printing the timeit but storing the duration variable
# which can be accessed and saved
timeit_without_print = timeit(internal_only=True)
with timeit_without_print:
    for _ in range(3):
        time.sleep(0.1)
timeit_total = timeit_without_print.total
# print(timeit_total)

# The `file` argument is for saving the output in a file (e.g. when using a logger)
file = open('tmp.log', 'w+')
with timeit(custom_print='Printing in file - Code Block Time: {duration:2.5f} sec(s)', file=file):
    for _ in range(2):
        time.sleep(0.1)
# See tmp.log
