# ch05_conjugate_gradient_methods.md

* interest in conjugate gradient methods is twofold.
  * they are among the most useful techniques for solving large linear systems of equations.
  * they can be adapted to solve nonlinear optimization problems.

## 5.1 the linear conjugate gradient method
* **linear** conjugate gradient method
  * is an iterative method for solving a **linear** system of equations $Ax = b$
    * $A$ is an $n \times n$ symmetric positive definite matrix
  * either as an algorithm
    * for solving linear systems or
    * as a technique for minimizing convex quadratic functions $\phi$
  * can be stated equivalently as the following minimization problem equ 5.2
    * the gradient of $\phi$ equals the residual of the linear system, equ 5.3

### conjugate direction methods
* a set of nonzero vectors { p0, p1 , . . . , pl } is said to be conjugate with respect to the symmetric
  positive definite matrix A if ...
  * any set of vectors satisfying this property is also linearly independent.
* The importance of conjugacy lies in the fact that
  * we can minimize $\phi$ in $n$ steps
    by successively minimizing it along the individual directions in a conjugate set.
  * Theorem 5.1.
* There are many ways to choose the set of conjugate directions.
  * eg: the eigen-vectors v1 , v2 , . . . , vn of A are mutually orthogonal
    as well as conjugate with respect to A

### basic properties of the conjugate gradient method
* conjugate gradient method is a conjugate direction method with a very special property:
  * In generating its set of conjugate vectors, it can compute a new vector $p_k$ by
    using ONLY the previous vector $p_{k-1} .
    * does not need to know all the previous elements p0 , p1 , . . . , pk−2 of the conjugate set;
      pk is automatically conjugate to these vectors. This
* each direction pk is chosen to be a linear combination of the negative residual $-r_k$
  (which, by (5.3), is the steepest descent direction for $\phi$ and the previous direction $p_{k-1}$
* the update
  * $p_k = -r_k + \beta p_{k-1}$
  * $\beta$ is to be determined by the requirement that $p_{k-1}$ and $p_k$ must
    be conjugate with respect to A
* other important properties.
  * the residuals ri are mutually orthogonal.
  * each search direction pk and residual rk is contained in the Krylov subspace of degree k for r0 ,
* the term “conjugate gradient method” is actually a misnomer
  * Since the gradients rk are mutually orthogonal
  * It is the search directions, not the gradients, that are conjugate with respect to A

### a practical form of the conjugate gradient method
* never need to know the vectors x, r , and p for more than the last two iterations.
* major computational tasks
  * computation of the matrix–vector product Apk
  * calculation of the inner products ... and ...
  * calculation of three vector sums
* The CG method is recommended only for large problems;
  * otherwise, Gaussian elimination or other factorization algorithms such as
    the singular value decomposition are to be preferred,
    since they are less sensitive to rounding errors.
* For large problems, the CG method has the advantage that
  * it does not alter the coefficient matrix and
  * (in contrast to factorization techniques) does not produce fill in the arrays holding the matrix.
  * CG method sometimes approaches the solution quickly,

### rate of convergence
TODO

### preconditioning
* preconditioning
  * is a change of variables from x to x̂ via a nonsingular matrix C
  * to accelerate the conjugate gradient method by transforming the linear system
    to improve the eigenvalue distribution of A.
* preconditioned CG methods
  * need to solve systems of the form $My = r$ (step (5.39d)).

### practical preconditioners
* knowledge about the structure and
  origin of a problem (in this case, knowledge that the system Ax  b is a finite-dimensional
  representation of a PDE) is the key to devising effective techniques for solving the problem
* General-purpose preconditioners
  * most important strategies of this type include sym-
    metric successive overrelaxation (SSOR), incomplete Cholesky, and banded preconditioners.

## 5.2 nonlinear conjugate gradient methods
* to ask whether we can adapt the linear CG approach
  to minimize general convex functions, or even general nonlinear functions f
  * recall: linear CG can be viewed as a minimization
    algorithm for the convex quadratic function φ defined by (5.2)
    * f to be a strongly convex quadratic and αk to be the exact minimizer,

### the fletcher–reeves method
* extend the conjugate gradient method to nonlinear functions by making two simple changes
  * in place of the formula (5.24a) for the step length αk (which minimizes φ along the search direction
    pk ), we need to perform a line search that identifies an approximate minimum of the
    nonlinear function f along pk .
  * the residual r , which is simply the gradient of φ in
    Algorithm 5.2 (see (5.3)), must be replaced by the gradient of the nonlinear objective f .
* requiring the step length αk to satisfy the strong Wolfe conditions

### the polak–ribière method and variants
* many variants of the Fletcher–Reeves method that
  * differ from each other mainly in the choice of the parameter $\beta_k$.
* Numerical experience indicates that Algorithm PR tends to be the more robust and efficient
  thatn FR
* A surprising fact about Algorithm PR is
  * that the strong Wolfe conditions (5.43) do NOT guarantee that pk is always a descent direction
* other variants
  * PR+
  * Hestenes-Stiefel formula
  * FR-PR.

### quadratic termination and restarts
TODO

### global convergence
TODO

### numerical performance
The Polak–Ribière algorithm, or its variation PR+, are not always more efficient
than Algorithm FR, and it has the slight disadvantage of requiring one more vector of
storage. Nevertheless, we recommend that users choose Algorithm PR, PR+ or FR-PR, or
the methods based on (5.49) and (5.50).

### notes and references
Since this angle can be arbitrarily close to 90◦ , the Fletcher–Reeves method can be slower than
the steepest descent method. The Polak–Ribière method behaves quite differently in these
circumstances: If a very small step is generated, the next search direction tends to the steepest
descent direction, as argued above. This feature prevents a sequence of tiny steps.
