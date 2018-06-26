# ch02: Fundamentals of Unconstrained Optimization

Nonlinear least-squares problem: a special case of unconstrained optimization
* given measurements $y_1, y_2, \ldots, y_m$ of a signal taken at times $t_1, t_2, \ldots, t_m$
* choose to model it by the function $\phi(t;x)$,
  where $x_i \in \mathbb{R}$, $i = 1, 2, \ldots, 6$ are the parameter of the model
* goal: to make the model values $\phi(t_j;x)$ fit the observed data $y_j$ as closely as possible.
* as an optimization problem,
  * group the parameters $x_i$ into a vector of unknowns $x = (x_1, x_2, \ldots, x_6)^T$
  * define residuals: $r_j(x) = y_j - \phi(t_j;x)$, where $j = 1, 2, \ldots, m$
    * which measure the discrepancy between the model and the observed data
  * solving the opt problem below for an estimate of $x$
    * $min_{x \in \mathbb{R}^6} f(x) = r_1^2 + r_2^2 + \ldots + r_m^2$ ...(2.3)

Suppose that for the data given, the optimal solution of (2.3) is approximately
$x^{\ast} = (1.1, 0.01, 1.2, 1.5, 2.0, 1.5)$ which yields $f (x^{\ast}) = 0.34 \ne 0$
* there must be discrepancies as $f(x^{\ast}) \ne 0$
* How, then, can we verify that $x^{\ast}$ is indeed a minimizer of $f$?
  * To answer this question, we need to define the term “solution”

## 2.1 What is a solution?
* minimizer
  * global minimizer
  * local minimizer
    * weak local minimizer
    * strict local minimizer
    * isolated local minimizer
* convex functions
  * for which every local minimizer is also a global minimizer

### recognizing a local minimum
Taylor’s theorem.
  * The mathematical tool used to study minimizers of smooth functions is

When the function $f$ is smooth and $f$ is twice continuously differentiable,
* we may be able to tell that x is a local minimizer (and possibly a strict local minimizer) by
  examining just the gradient $\nabla f(x^{\ast})$ and the Hessian $\nabla^2 f(x^{\ast})$

* Necessary conditions for optimality
  * Theorem 2.2 (First-Order Necessary Conditions).
  * Theorem 2.3 (Second-Order Necessary Conditions).

* sufficient conditions,
  which are conditions on the derivatives of $f$ at the point $z^{\ast}$  that
  guarantee that $x^{\ast}$ is a local minimizer.
  * Theorem 2.4 (Second-Order Sufficient Conditions).


### nonsmoth problem
* If, however, the function consists of a few smooth pieces, with discontinuities between the pieces,
  * it may be possible to find the minimizer by minimizing each smooth piece individually.
* If the function is continuous everywhere but nondifferentiable at certain points, as in Figure 2.3,
  * we can identify a solution by examing the subgradient or generalized gradient
* minimization of certain special nondifferentiable function
  * can be reformulated as smooth constrained optimization problems;

## 2.2 Overview of algorithms
* All algorithms for unconstrained minimization require
  the user to supply a starting point, which we usually denote by $x_0$
* steps
  * Beginning at $x_0$, optimization algorithms generate a sequence of iterates `${x_k}_{k=0}^{\infty}$`
  * that terminate when either
    * no more progress can be made or
    * when it seems that a solution point has been approximated with sufficient accuracy.
  * In deciding how to move from one iterate $x_k$ to the next,
    the algorithms use information about the function $f$ at $x_k$ , and
    possibly also information from earlier iterates $x_0, x_1, \ldots, x_{k-1}.
    *  use this information to find a new iterate $x_{k+1}$ with a lower function value than $x_k$

TWO fundamental strategies for moving from the current point to a new iterate:
line search and trust region.
BOTH differ in the order in which they choose the direction and distance of the move to the next iterate.

### line search
* steps
  * starts by fixing the direction $p_k$ and
  * then identifying an appropriate distance, namely the step length $\alpha_k$
* solving
  * $min_{\alpha >0} f(x_k + \alpha p_k)$
* issue: choice of the search direction $p_k$
  * in general, any descent direction is guaranteed to produce a decrease in f
    provided that the step length is sufficiently small
  * steepest descent direction $ - \nabla f_k $
    * as in: steepest descent method
    * this direction is orthogonal to the contours of the function.
  * the Newton direction.
    * have a fast rate of local convergence, typically quadratic.
    * need the Hessian
  * Quasi-Newton search directions
    * not require computation of the Hessian and
    * yet still attain a superlinear rate of convergence.
    * Two of the most popular formulae for updating the Hessian approximation $B_k$
      * symmetric-rank-one (SR1) formula
      * BFGS formula
  * nonlinear conjugate gradient methods
    * not attain the fast convergence rates of Newton or quasi-Newton methods,
    * but they have the advantage of not requiring storage of matrices.

### trust region
* steps
  * choose a maximum distance, ie the trust-region radius $\delta_k$
  * then seek a direction and step that attain the best improvement possible subject to
    this distance constraint.
  * If this step proves to be unsatisfactory, we reduce the distance measure $\delta_k$ and try again
    *  it usually points in a different direction from the previous candidate.
* solving
  * $min_p m_k(x_k + p)$
  * where $x_k + p$ lies inside the trust region.
* Usually, the trust region is a ball defined by the Euclidean norm `$||p||_2 \le \delta$`,
   where the scalar $\delta > 0$ is called the trust-region radius
* issue: choice of the Hessian $B_k$, models for trust-region methods
* variant
  * trust-region Newton method
  * trust-region quasi-Newton method.

### scaling
*  One important issue in problem formulation is scaling
* In unconstrained optimization,a problem is said to be poorly scaled
  if changes to x in a certain direction produce much larger variations in the value of f than
  do changes to x in another direction.
* Some optimization algorithms, such as steepest descent, are sensitive to poor scaling,
  * while others, such as Newton’s method, are unaffected by it.
* in designing complete algorithms, we try to incorporate
  * scale invariance into all aspects of the algorithm, including the line search or trust-region strategies
  * and convergence tests.
* Generally speaking, it is easier to preserve scale invariance for line search algorithms than
  for trust-region algorithms

## question
* so in line search, the step size $\alpha$ should **never** be fixed/constant?
  but many, except those with adaptive learning rate, treat that as a constant
* trust region is alwasy better than line search?
