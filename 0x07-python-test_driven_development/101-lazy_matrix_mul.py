#!/usr/bin/python3
"""
Test Driven Doc Lazy Matrix mul

"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices by using the module NumPy
    Returns: new matrix
    """
    if type(m_a) is str or type(m_b) is str:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    for i in m_a:
        for j in i:
            if type(j) is str:
                raise TypeError("invalid data type for einsum")
    for a in m_b:
        for b in a:
            if type(b) is str:
                raise TypeError("invalid data type for einsum")
    return numpy.dot(m_a, m_b)
