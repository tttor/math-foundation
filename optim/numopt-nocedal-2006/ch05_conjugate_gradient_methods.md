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
TODO
