# Basic

# Book
* G. H. Golub and C. F. Van Loan, Matrix Computations, Baltimore, MD, Johns Hopkins University Press
* Lectures on Probability Theory and Mathematical Statistics, Marco Taboga
* Jan R. Magnus, Heinz Neudecker-Matrix Differential Calculus with Applications in Statistics and Econometrics, 3rd Edition-Wiley (2007)
* http://matrixcookbook.com

# Course
* https://www.khanacademy.org/math/multivariable-calculus
* https://github.com/fastai/numerical-linear-algebra
* https://www.statlect.com/
* https://stattrek.com/

# Tool
* https://www.desmos.com
* https://www.derivative-calculator.net/

# Misc
* Taylor series, theorem
* eigen value, eigen vector
* http://mathworld.wolfram.com/MatrixEquation.html
* Big-O Notation, $O(\cdot)$
* https://stats.stackexchange.com/questions/29713/what-is-covariance-in-plain-language
* https://math.stackexchange.com/questions/337090/if-f-is-strictly-convex-in-a-convex-set-show-it-has-no-more-than-1-minimum
* https://math.stackexchange.com/questions/395944/proof-on-showing-function-f-in-c1-on-an-open-convex-set-u-subset-mathbb
  * $ f \in C^k$ means all partial derivatives up to (and including) order $k$ exist and continuous.

## positive definite matrix
* https://math.stackexchange.com/questions/2523985/question-about-for-all-symmetric-matrix-and-positive-definite
* https://math.stackexchange.com/questions/1059566/explain-proof-that-any-positive-definite-matrix-is-invertible
* https://math.stackexchange.com/questions/1404534/why-does-positive-definite-matrix-have-strictly-positive-eigenvalue
* https://yutsumura.com/positive-definite-real-symmetric-matrix-and-its-eigenvalues/

### vs positive semi-definite matrix
* https://onlinelibrary.wiley.com/doi/pdf/10.1002/9780470173862.app3
* https://math.stackexchange.com/questions/1733726/positive-semi-definite-vs-positive-definite
* https://www.quora.com/Is-there-a-difference-between-positive-semi-definite-and-positive-definite-matrix

## derivative, gradient, jacobian, hessian
* https://www.math.ucdavis.edu/~kouba/CalcOneDIRECTORY/chainruledirectory/ChainRule.html
* https://mathinsight.org/chain_rule_refresher
* https://en.wikipedia.org/wiki/Differentiation_rules

Let $\phi: \mathbb{R} \mapsto \mathbb{R}$ be a univariate fn: a real value fn of a real variable.

Then the first derivative is defined as:</br>
$\frac{d \phi}{d \alpha} = \phi'(\alpha) = \lim_{\epsilon \mapsto 0} \frac{\phi(\alpha + \epsilon) - \phi(\alpha)}{\epsilon}$

And the second derivative is: </br>
$\frac{d^2 \phi}{d \alpha^2} = \phi''(\alpha) = \lim_{\epsilon \mapsto 0} \frac{\phi'(\alpha + \epsilon) - \phi'(\alpha)}{\epsilon}$


