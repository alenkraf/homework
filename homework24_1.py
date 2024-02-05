import concurrent.futures
import math

NUMBERS = [

]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_prime_concurrent_executor(numbers, executor):
    with executor() as pool:
        results = list(pool.map(is_prime, numbers))
    return results

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as thread_pool:
        thread_results = check_prime_concurrent_executor(NUMBERS, concurrent.futures.ThreadPoolExecutor)

    with concurrent.futures.ProcessPoolExecutor() as process_pool:
        process_results = check_prime_concurrent_executor(NUMBERS, concurrent.futures.ProcessPoolExecutor)

    print("Thread Results:", thread_results)
    print("Process Results:", process_results)
