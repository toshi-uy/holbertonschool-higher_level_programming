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
    return numpy.dot(m_a, m_b)
