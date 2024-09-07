import time

import rust_python_example


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # Zavolání Rust funkce fibonacci z Pythonu
    repeated = 50
    print("Calling Rust fibonacci function from Python")
    start = time.time()
    for i in range(repeated):
        result = rust_python_example.fibonacci(30)
    end = time.time()
    rust_time = end - start
    print(f"Rust time: {rust_time}")

    # Zavolání Python funkce fibonacci z Pythonu
    print("Calling Python fibonacci function from Python")
    start = time.time()
    for i in range(repeated):
        result = fibonacci(30)
    end = time.time()
    python_time = end - start
    print(f"Python time: {python_time}")

    print(f"Rust is faster than Python about {python_time//rust_time} times.")
