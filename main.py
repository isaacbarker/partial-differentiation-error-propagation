import streamlit as st
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import pandas as pd
import math

st.set_page_config(
    page_title="Error Propagation",
    page_icon="🔢",
)

st.title("Error Propagation")

# Calculator
st.markdown("### Calculator")

expression = st.text_input("Function to propagate", placeholder="e.g. 1/2 * g * t**2")

# get symbols in expression and request uncertainty data for each
if expression:
    f = parse_expr(expression)

    symbols = f.free_symbols
    symbol_vals = []
    symbol_uncertainties = []

    for s in symbols:
        val_input = st.number_input(f"{s}", format="%.5f")
        symbol_vals.append(val_input)

        uncertainty_input = st.number_input(f"Δ{s} (Leave as 0 for a constant)", format="%.5f")
        symbol_uncertainties.append(uncertainty_input)

    calculate = st.button("Calculate")

    if calculate:
        # calculate uncertainty
        uncertainty_squared = 0
        subs = dict(zip(symbols, symbol_vals))

        for i, s in enumerate(symbols):
            f_diff_s = sp.diff(f, s)
            uncertainty_squared += math.pow(abs(f_diff_s.subs(subs).evalf()), 2) * math.pow(symbol_uncertainties[i], 2)

        value = f.subs(subs)
        error = math.sqrt(uncertainty_squared)

        def round_sig(x, sig=3):
            if x == 0:
                return 0
            return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

        st.markdown(f"Propagated value: **{round_sig(value, 3)} ± {round_sig(error, 1)}**")

# How to
common_functions = {
    "Function": [
        "$x^2$",
        "$xy$",
        r"$\sqrt{x}$",
        "$ln(x)$"
    ],
    "Formatted": [
        "x**2",
        "x * y",
        "sqrt(x)",
        "ln(x)"
    ]
}

df = pd.DataFrame(common_functions)

st.markdown("""
    ### Usage
    Write the function which you want to propagate errors through. The code will then detect the symbols you have used and prompt for values and their respective uncertainties.
    A few common operations and their syntax is avaliable below, though it follows python mathematical notation in general.
""")

st.markdown(df.to_markdown(index=False))

# Theory and about section
st.markdown("""
    ### Theory
    This calculator uses the partial differentiation method to propagate errors, assuming the variables are _independent_ of one another.
    The error in a value T, where T = f(p<sub>i</sub>) can be found with the following formula:
""", unsafe_allow_html=True)
st.latex(r"""
    \Delta T^2 = \sum_{i}^{} \lvert \frac{\partial f(p_i)}{\partial x_i} \rvert ^2  \Delta x_i^2,
""")

st.markdown("""
    where p<sub>i</sub> represents the parameters of f, and x<sub>i</sub> represents the specific parameter.
""", unsafe_allow_html=True)

st.text("Code written by Isaac Barker. ")

