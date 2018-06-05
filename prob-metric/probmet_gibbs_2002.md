# On Choosing and Bounding Probability Metrics
* Gibbs

## problem
* How does one choose among all these metrics? Issues that can affect
a metric’s desirability include whether it has an interpretation applicable to
the problem at hand, important theoretical properties, or useful bounding
techniques.

## idea
* Knowledge of other metrics can provide a means of deriving bounds for another one
in an applied problem.
* Considering other metrics can also provide alternate insights.

## result
* rates of convergence can strongly depend on the metric chosen.

## background
* prob measure is another term for prob distrib
* The total variation distance is one of the most com-
monly used probability metrics, because it admits natural interpretations as
well as useful bounding techniques.
For instance, in (1), if A is any event,
then total variation can be interpreted as an upper bound on the difference
of probabilities that the event occurs under two measures. In Bayesian sta-
tistics, the error in an expected loss function due to the approximation of
one measure by another is given (for bounded loss functions) by the total
variation distance through its representation in equation (2)
* a sequence of probability measures converges if
for any error tolerance $\epsilon > 0$ we require there be $N$ sufficiently large for $n \ge N$ to
ensure the 'difference' between the predicted measure and the actual/true measure is smaller than $\epsilon$.

## comment
* nicely, the authors give description about:
which metric is more suitable in certain cases, so
no single metric is suitable for all.
