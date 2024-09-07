# Rust-Python Integration Template

This project serves as a **template** for using Rust within Python to achieve performance improvements in
computationally expensive tasks. By leveraging the power of Rust for speed, and the flexibility of Python for ease of
use, this project demonstrates how to efficiently combine the two languages.

In this template, we showcase a simple example where the Fibonacci sequence is computed both in Python and in Rust, and
we measure the speed of both implementations. This provides a clear example of the **performance benefits** Rust can
offer when integrated with Python.

## Requirements

- Python 3.x
- Rust (with `cargo`)
- [maturin](https://github.com/PyO3/maturin) for compiling Rust into a Python module

You can install `maturin` using pip:

```bash
pip install maturin
```

## Project Setup

1. **Clone the repository** and navigate to the project directory:

```bash
git clone <repo_url>
cd rust_python_project
```

2. **Set up a virtual environment (optional but recommended):**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. **Build and install the Rust module** using `maturin`:

```bash
maturin develop
```

This will compile the Rust code and install the module `rust_python_example` into your Python environment.

## Rust-Python Fibonacci Performance Comparison

In this project, we use both a Python implementation and a Rust implementation of the **Fibonacci sequence** to
demonstrate the performance gains of using Rust.

The Python code looks like this:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

In Rust, the Fibonacci function is implemented in a similar way but benefits from Rust's performance optimizations:

```rust
#[pyfunction]
fn fibonacci(n: u64) -> u64 {
    if n <= 1 {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}
```

### Usage Example

The following script compares the speed of the Fibonacci function implemented in Python versus Rust:

```python
import time
import rust_python_example


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    repeated = 50

    # Timing Rust's Fibonacci function
    print("Calling Rust fibonacci function from Python")
    start = time.time()
    for _ in range(repeated):
        result = rust_python_example.fibonacci(30)
    end = time.time()
    rust_time = end - start
    print(f"Rust time: {rust_time}")

    # Timing Python's Fibonacci function
    print("Calling Python fibonacci function from Python")
    start = time.time()
    for _ in range(repeated):
        result = fibonacci(30)
    end = time.time()
    python_time = end - start
    print(f"Python time: {python_time}")

    print(f"Rust is faster than Python by a factor of {python_time // rust_time} times.")
```

### Explanation of the Performance Test

The test compares the performance of calculating the 30th Fibonacci number:

1. **Rust Fibonacci**:
    - The `rust_python_example.fibonacci(30)` function is called `50` times in a loop.
    - The time taken is measured using Python's `time` module.

2. **Python Fibonacci**:
    - The pure Python `fibonacci(30)` function is called `50` times in a loop.
    - The time taken is again measured using Python's `time` module.

3. **Performance Result**:
    - The difference in execution time between the Rust and Python implementations is displayed.
    - The speedup factor is calculated by comparing the total execution times of Rust and Python.

### Running the Test

After installing the Rust module, run the performance comparison:

```bash
python python_module/example.py
```

### Expected Output

You will see output similar to the following, showing that Rust is significantly faster than Python for this
computational task:

```
Calling Rust fibonacci function from Python
Rust time: 0.35816025733947754
Calling Python fibonacci function from Python
Python time: 6.149831533432007
Rust is faster than Python about 17.0 times.
```

## Why Use Rust in Python?

- **Speed**: Rust is a systems programming language that offers near-C level performance. For computationally expensive
  tasks like the Fibonacci sequence, Rust can significantly reduce execution time.
- **Memory Safety**: Rust’s strong memory safety guarantees ensure that there are no data races, and programs are more
  stable.
- **Simple Integration**: Using PyO3 and `maturin`, it’s easy to expose Rust functions as Python modules, giving you the
  best of both languages.

## Conclusion

This project serves as a template for integrating Rust into Python applications to accelerate performance-critical
sections. By leveraging Rust’s speed and Python’s flexibility, you can optimize your applications without sacrificing
development ease.

---

This README provides a detailed explanation of the project structure, setup, and a real-world performance comparison
between Python and Rust implementations of the Fibonacci sequence. You can use this as a starting point for integrating
Rust into your Python projects for performance improvements.