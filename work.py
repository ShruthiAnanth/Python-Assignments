import time

# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    total_lines = lines_before_coffee
    while lines_before_coffee > 0:
        lines_before_coffee = lines_before_coffee // prod_loss
        total_lines += lines_before_coffee
    return total_lines, 1

# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee and
#         the number of calls to sum_series as a tuple
def linear_search(total_lines, prod_loss):
    initial_lines = 1
    total_for_initial_lines, calls_to_sum_series = sum_series(initial_lines, prod_loss)

    while total_for_initial_lines < total_lines:
        initial_lines += 1
        total_for_initial_lines, calls = sum_series(initial_lines, prod_loss)
        calls_to_sum_series += calls

    return initial_lines, calls_to_sum_series

# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee and
#         the number of calls to sum_series as a tuple
def binary_search(total_lines, prod_loss):
    low = 1
    high = total_lines
    best_option = (0, 0, 0)
    total_calls = 0  # To store the total calls to sum_series

    while low <= high:
        mid = (low + high) // 2
        lines_written, calls = sum_series(mid, prod_loss)
        total_calls += calls  # Accumulate total calls

        if lines_written >= total_lines:
            best_option = (mid, lines_written, total_calls)
            high = mid - 1
        else:
            low = mid + 1

    return best_option


def main():
    # TODO: read number of cases, and store it in num_cases
    num_cases = int(input())

    # TODO: Iterate for the number of test cases
    for i in range(num_cases):
        # read one line for one case
        # TODO: Replace this line with reading next line from stdin (input redirection or terminal)
        line = input()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, _, binary_calls = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", binary_calls, "times")
        finish = time.time()
        binary_time = finish - start
        print(f"Elapsed Time: {binary_time:0.8f} seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        linear_calls, linear_lines = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", linear_lines)
        print("sum_series called", linear_calls, "times")
        finish = time.time()
        linear_time = finish - start
        print(f"Elapsed Time: {linear_time:0.8f} seconds")
        print()

        # Comparison
        comparison = linear_time / binary_time if binary_time else 1
        print(f"Binary Search was {comparison:0.1f}",
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
