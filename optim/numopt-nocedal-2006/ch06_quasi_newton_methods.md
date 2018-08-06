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
* Broyden family of updating formulae: of which BFGS is a special case
* If at some iteration the matrix Hk becomes a poor approximation to the true inverse Hessian,
  is there any hope of correcting it?
  * Can these errors grow to the point of erasing all useful information in
    the quasi-Newton approximate Hessian?
  * the BFGS formula has very effective self-correcting properties
    * The self-correcting properties of BFGS hold only when an adequate line search is performed
      * the Wolfe line search conditions ensure that the gradients are sampled at points
        that allow the model (6.1) to capture appropriate curvature information.
    * cf: the DFP method is less effective in correcting bad Hessian approximations;
* the DFP and BFGS updating formulae are duals of each other,
  in the sense that one can be obtained from the other by the interchanges s ↔ y,B ↔ H .

## implementation
* The line search, which should satisfy either the Wolfe conditions (3.6) or the strong Wolfe conditions (3.7),
  * should always try the step length $\alpha_k = 1$ first,
    * because this step length will eventually always be accepted (under certain conditions),
    * thereby producing superlinear convergence of the overall algorithm.
* The values c1 = 10−4 and c2 = 0.9 are commonly used in (3.6)
* the initial matrix H0 often is set to some multiple β I of the
  identity, but there is no good general strategy for choosing the multiple β.
  * A heuristic that is often quite effective is to scale the starting matrix after the first
    step has been computed but before the first BFGS update is performed;
    see equ (6.20)
* The performance of the BFGS method CAN DEGRADE if the line search is NOT based on the Wolfe conditions
  * Eg: an Armijo backtracking line search (see Section 3.1):
    * The unit step length αk = 1 is tried first and is successively decreased until
      the sufficient decrease condition (3.6a) is satisfied.
    * For this strategy, there is NO GUARANTEE that the curvature condition yk T sk > 0 (6.7)
      will be satisfied by the chosen step, since a step length greater than 1 may be required to satisfy this condition.
    * not recommended,
      * simply skip the BFGS update by setting Hk+1 = Hk when yk T sk is negative or too close to zero
      * because the updates may be skipped much too often to
        allow Hk to capture important curvature information for the objective function f .
    * see a damped BFGS update
      * that is a more effective strategy for coping with the case where the curvature condition (6.7) is not satisfied
