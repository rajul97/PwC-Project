from src.pipeline import spark

def test_spark_session():
    assert spark is not None
