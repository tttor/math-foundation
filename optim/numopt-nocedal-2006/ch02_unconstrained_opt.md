# ch02: Fundamentals of Unconstrained Optimization

nonlinear least-squares problem: a special case of unconstrained optimization
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
$x^* = (1.1, 0.01, 1.2, 1.5, 2.0, 1.5) which yields $f (x^*) = 0.34 \ne 0$
* there must be discrepancies as $f(x^*) \ne 0$
* How, then, can we verify that $x^*$ is indeed a minimizer of $f$?
  * To answer this question, we need to define the term “solution”
