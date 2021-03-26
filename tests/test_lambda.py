import pytest
import etl.lambda_function as lf
import os


def test_response():
    assert lf.get_data()