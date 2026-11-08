import threading
import time


# ------------------------------------------------------------
# 1. Recursive Fibonacci Function
# ------------------------------------------------------------

def fibonacci(n):

    # Base cases
    if n <= 1:
        return n

    # Recursive calculation
    return fibonacci(n - 1) + fibonacci(n - 2)


# ------------------------------------------------------------
# 2. Thread Worker Function
# ------------------------------------------------------------

def calculate_fibonacci(n, results):

    result = fibonacci(n)

    # Store the result using n as the dictionary key
    results[n] = result


# ------------------------------------------------------------
# 3. Multithreading Experiment
# ------------------------------------------------------------

def multithreading_experiment():

    numbers = [35, 38, 40]

    total_times = []

    print("\n==============================================")
    print(" FIBONACCI COMPUTATION (WITH MULTITHREADING)")
    print("==============================================")

    for round_number in range(1, 11):

        results = {}
        threads = []

        # Create three separate threads
        for n in numbers:

            thread = threading.Thread(
                target=calculate_fibonacci,
                args=(n, results)
            )

            threads.append(thread)

        # Start measuring before the first thread starts
        start_time = time.perf_counter_ns()

        # Start all three threads
        for thread in threads:
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        # End time after the last thread finishes
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time

        total_times.append(elapsed_time)

        print("\nRound", round_number)

        print("Fib(35):", results[35])
        print("Fib(38):", results[38])
        print("Fib(40):", results[40])

        print("Total Time:", elapsed_time, "ns")

    # Calculate average execution time
    average_time = sum(total_times) / len(total_times)

    print("\n==============================================")
    print("MULTITHREADING RESULTS")
    print("==============================================")

    print("Average Time:",
          format(average_time, ".2f"), "ns")

    return average_time


# ------------------------------------------------------------
# 4. Sequential Experiment
# ------------------------------------------------------------

def sequential_experiment():

    numbers = [35, 38, 40]

    total_times = []

    print("\n==============================================")
    print(" FIBONACCI COMPUTATION (WITHOUT MULTITHREADING)")
    print("==============================================")

    for round_number in range(1, 11):

        results = {}

        # Start measuring execution time
        start_time = time.perf_counter_ns()

        # Calculate Fibonacci numbers one by one
        for n in numbers:

            results[n] = fibonacci(n)

        # End measuring execution time
        end_time = time.perf_counter_ns()

        elapsed_time = end_time - start_time

        total_times.append(elapsed_time)

        print("\nRound", round_number)

        print("Fib(35):", results[35])
        print("Fib(38):", results[38])
        print("Fib(40):", results[40])

        print("Total Time:", elapsed_time, "ns")

    # Calculate average execution time
    average_time = sum(total_times) / len(total_times)

    print("\n==============================================")
    print("SEQUENTIAL RESULTS")
    print("==============================================")

    print("Average Time:",
          format(average_time, ".2f"), "ns")

    return average_time


# ------------------------------------------------------------
# 5. Compare Both Experiments
# ------------------------------------------------------------

def compare_results(threaded_time, sequential_time):

    print("\n==============================================")
    print("FINAL PERFORMANCE COMPARISON")
    print("==============================================")

    print("Multithreading Average:",
          format(threaded_time, ".2f"), "ns")

    print("Sequential Average:",
          format(sequential_time, ".2f"), "ns")

    if threaded_time < sequential_time:

        improvement = (
            (sequential_time - threaded_time)
            / sequential_time
        ) * 100

        print("\nObservation:")
        print("Multithreading was faster in this experiment.")

        print("Time reduction:",
              format(improvement, ".2f"), "%")

    elif threaded_time > sequential_time:

        difference = (
            (threaded_time - sequential_time)
            / sequential_time
        ) * 100

        print("\nObservation:")
        print("Sequential processing was faster in this experiment.")

        print("Multithreading took",
              format(difference, ".2f"),
              "% more time.")

    else:

        print("\nObservation:")
        print("Both experiments took approximately the same time.")


# ------------------------------------------------------------
# 6. Main Program
# ------------------------------------------------------------

def main():

    print("==============================================")
    print(" ADVANCED ALGORITHMS - QUESTION 3")
    print(" FIBONACCI PERFORMANCE EXPERIMENT")
    print("==============================================")

    # Run multithreading experiment
    threaded_average = multithreading_experiment()

    # Run sequential experiment
    sequential_average = sequential_experiment()

    # Compare both experiments
    compare_results(threaded_average, sequential_average)


if __name__ == "__main__":
    main()
