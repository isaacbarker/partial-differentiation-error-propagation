# Error Propagation Calculator

## About

This calculator uses the partial differentiation method to propagate errors, assuming the variables are _independent_ of one another. The error in a value T, where T = f(p<sub>i</sub>) can be found with the following formula:

$$
\Delta T^2 = \sum_{i}^{} \lvert \frac{\partial f(p_i)}{\partial x_i} \rvert ^2  \Delta x_i^2,
$$

where p<sub>i</sub> represents the parameters of f, and x<sub>i</sub> represents the specific parameter.

## Libraries
The code makes use of [sympy](https://www.sympy.org/en/index.html) for symbolic algebra and partial differentiation and is made with [streamlit](https://streamlit.io/) to enable access through the web. 