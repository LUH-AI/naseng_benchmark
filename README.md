# Benchmark Functions


Source: Li, Yucen Lily, Tim GJ Rudner, and Andrew Gordon Wilson. "A study of bayesian neural network surrogates for bayesian optimization." arXiv preprint arXiv:2305.20028 (2023).

## Installation
Install the project:
````
pip install -e .
````
## Adding a New Test Function

### Defining the function

Our library supports any test function which extends the `BaseTestProblem` class defined in BoTorch ([documentation](https://botorch.org/api/test_functions.html#botorch.test_functions.base.BaseTestProblem)). This class requires an implementation of the `evaluate_true` method, which takes in X values and returns the value of the objective function at those values.

For example, in order to specify the objective function $y = x^2$, we can define the following class:
```
class Toy(BaseTestProblem):
    dim = 1

    def evaluate_true(self, X: Tensor) -> Tensor:
        return torch.pow(X, 2)
```

Many of the test function we use in the library are defined in the `test_functions` folder, or directly imported from BoTorch.
