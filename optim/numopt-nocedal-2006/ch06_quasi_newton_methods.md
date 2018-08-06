# ch06_quasi_newton_methods.md

* Quasi-Newton methods
  * like steepest descent,
    require **only the gradient** of the objective function to be supplied at each iterate.
  * By measuring the changes in gradients, they
    construct a model of the objective function that is good enough to
    produce superlinear convergence.

# 6.1 the bfgs method
* $B_k$ is an $n \times n$ symmetric positive definite matrix
  * that will be revised or updated at every iteration.
* the key difference with Newton method is that
  * the approximate Hessian Bk is used in place of the true Hessian.
* Davidon proposed
  * Instead of computing B k afresh at every iteration,
    * to update it in a
      simple manner to account for the curvature measured during the most recent step
  * One reasonable requirement is that
    * the gradient of $m_{k+1}$ should match the
      gradient of the objective function $f$ at the latest TWO iterates $x_k$ and $x_{k+1}$
* secant equation: equ (6.6), see also equ (2.12)
* the condition (6.7)
  * is guaranteed to hold if we impose the Wolfe (3.6) or strong
    Wolfe conditions (3.7) on the line search
  * When f is strongly convex, the inequality (6.7)
    will be satisfied for any two points xk and xk+1
  * will not always hold for nonconvex functions,
    * need to enforce (6.7) explicitly, by imposing restrictions on
      the line search procedure that chooses the step length
* When the curvature condition is satisfied,
  * the secant equation (6.6) always has a solution
  * it admits an infinite number of solutions,
* To determine Bk+1 uniquely,
  * impose the additional condition that among all symmetric matrices
    satisfying the secant equation, Bk+1 is,
    in some sense, closest to the current matrix Bk .
  * equ 6.9a, 6.9b
  * Different matrix norms can be used in (6.9a), and
    each norm gives rise to a different quasi-Newton method,
    eg Frobenius norm
* DFP updating formula
  * DFP: Davidon, Fletcher and Powell
  * using Frobenius norm and some weighting matrix, equ (6.11)
* Using the Sherman–Morrison–Woodbury formula (A.28),
  we can derive the following expression for the update of the inverse
  Hessian approximation Hk that corresponds to the DFP update of Bk in (6.13):
* fundamental idea of quasi-Newton updating:
  * Instead of recomputing the approximate Hessians (or inverse Hessians) from scratch at every iteration,
    apply a simple
    modification that combines the most recently observed information about the objective
    function with the existing knowledge embedded in our current Hessian approximation.
* BFGS formula
  * is presently considered to be the most effective of all quasi-Newton updating formulae.
    * supersedes The DFP updating formula
  * Instead of imposing conditions on the Hessian approximations Bk , we
    impose similar conditions on their inverses Hk .
  * unique solution Hk+1 to (6.16) is in (6.17)
* How should we choose the initial approximation H0 ?
  * use specific information about the problem, for instance
    by setting it to the inverse of an approximate Hessian calculated by finite differences at x0
  * simply set it to be the identity matrix, or a multiple of the identity matrix,
    where the multiple is chosen to reflect the scaling of the variables.
* Algorithm 6.1 (BFGS Method).
  * its rate of convergence is superlinear, which is fast enough for most practical purposes
    * cf Newton’s method: converges quadratically
* Sherman–Morrison–Woodbury formula:
  * to derive a version of the BFGS algorithm that works with the Hessian approximation Bk rather than Hk

## properties of the bfgs method
* BFGS: the superlinear rate of convergence

## implementation
* The line search, which should satisfy either the Wolfe conditions (3.6) or the strong Wolfe conditions (3.7),
  * should always try the step length $\alpha_k = 1$ first,
    * because this step length will eventually always be accepted (under certain conditions),
    * thereby producing superlinear convergence of the overall algorithm.
