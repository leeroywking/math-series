# Series 

## Task
    - All futher tasks should be driven by TDD
    - Create a function that will return the nth fibonacci number
    - Create a function that will return the nth lucas number
    - Create a function that will return the nth sum number 

## Bonus 
    - write each function iteratively and recursively
    - 100% code coverage

```bash

(math-series-M3lhcFER-py3.8) lee@lee-XPS-13-9300:~/math-series$ pytest --cov=mmath_series tests/
=========================================== test session starts ============================================
platform linux -- Python 3.8.2, pytest-5.4.3, py-1.8.1, pluggy-0.13.1
rootdir: /home/lee/math-series
plugins: cov-2.9.0
collected 15 items                                                                                         

tests/test_series.py ...............                                                                 [100%]Coverage.py warning: Module mmath_series was never imported. (module-not-imported)
Coverage.py warning: No data was collected. (no-data-collected)
WARNING: Failed to generate report: No data to report.

/home/lee/.cache/pypoetry/virtualenvs/math-series-M3lhcFER-py3.8/lib/python3.8/site-packages/pytest_cov/plugin.py:264: PytestWarning: Failed to generate report: No data to report.

  self.cov_controller.finish()


----------- coverage: platform linux, python 3.8.2-final-0 -----------


============================================ 15 passed in 0.63s ============================================

```
