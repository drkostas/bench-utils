# pip install bench-utils
from bench_utils import profileit
import time


# --- Timeit as a decorator --- #

# Set custom print and use the function name and arguments as you want
@profileit(custom_print='Running {func_name} function with arguments {args} ({0} and {1})')
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
with profileit(custom_print='Code Block Time: {duration:2.5f} sec(s)', skip=False):
    for _ in range(2):
        time.sleep(0.1)

# The `internal_only` argument is for not printing the timeit but storing the duration variable
# which can be accessed and saved
timeit_without_print = profileit(internal_only=True)
with timeit_without_print:
    for _ in range(3):
        time.sleep(0.1)
profiler_obj = timeit_without_print.profiler
# print(timeit_total)

# The `file` argument is for saving the output in a file (e.g. when using a logger)
# `k_words` is used to include only pstats that contain these words
# `sort_by` is to select the sorting argument (pstat column)
file = open('tmp.log', 'w+')
profiler_output = 'profiler_output.log'
keep_only_these = ['bench_utils']
sort_by = 'tottime'
custom_print = f'Profiling Code block - skipping: '
with profileit(file=file, profiler_output=profiler_output,
               keep_only_these=keep_only_these,
               custom_print=custom_print, sort_by=sort_by, internal_only=True):
    run_something_2(1)
    run_something_2(4)
# See tmp.log
