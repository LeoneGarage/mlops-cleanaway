"""
This module defines the following routines used by the 'train' step of the regression recipe:

- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model pipeline.
"""


def estimator_fn():
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    import xgboost as xgb

    return xgb.XGBRegressor(random_state=42, base_score=0.5)
