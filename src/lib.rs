use pyo3::prelude::*;

// Exponenciálně složitá funkce pro výpočet n-tého Fibonacciho čísla
#[pyfunction]
fn fibonacci(n: u64) -> u64 {
    if n <= 1 {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}

// Modul, který bude volat Python
#[pymodule]
fn rust_python_example(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
