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
$x^* = (1.1, 0.01, 1.2, 1.5, 2.0, 1.5)$ which yields $f (x^*) = 0.34 \ne 0$
* there must be discrepancies as $f(x^*) \ne 0$
* How, then, can we verify that $x^*$ is indeed a minimizer of $f$?
  * To answer this question, we need to define the term “solution”

## 2.1 what is a solution?
* minimizer
  * global minimizer
  * local minimizer
    * weak local minimizer
    * strict local minimizer
    * isolated local minimizer
* convex functions
  * for which every local minimizer is also a global minimizer

### recognizing a local minimum
When the function $f$ is smooth and $f$ is twice continuously differentiable,
* we may be able to tell that x is a local minimizer (and possibly a strict local minimizer) by
  examining just the gradient $\nabla f(x^*)$ and the Hessian $\nabla^2 f(x^*)$

### nonsmoth problem
* If, however, the function consists of a few smooth pieces, with discontinuities between the pieces,
  * it may be possible to find the minimizer by minimizing each smooth piece individually.
* If the function is continuous everywhere but nondifferentiable at certain points, as in Figure 2.3,
  * we can identify a solution by examing the subgradient or generalized gradient
* minimization of certain special nondifferentiable function
  * can be reformulated as smooth constrained optimization problems;
