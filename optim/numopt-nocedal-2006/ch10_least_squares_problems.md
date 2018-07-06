# ch10: Least-Squares Problems

## 10.3: algorithms for nonlinear least-squares problems

### the gauss–newton method
* advantage of Gauss–Newton
  * our use of the approximation (10.24) saves us the trouble of computing the individual residual Hessians
  * there are many interesting situations in which the first term J J in (10.5) dominates
    the second term (at least close to the solution x ), so
    that J k T Jk is a close approximation to ∇ 2 f k and the convergence rate of Gauss–Newton is
    similar to that of Newton’s method.
  * whenever Jk has full rank and the gradient
    ∇ f k is nonzero, the direction p GN k is a descent direction for f , and therefore a suitable
    direction for a line search.
  * we can find the search direction by applying linear least-squares algorithms to the subproblem (10.26)
* If the number of residuals m is large
  while the number of variables n is relatively small,
  * it may be unwise to store the Jacobian J explicitly.
  * A preferable strategy may be to calculate the matrix $J^T J$ and gradient vector $J^T r$ by
    evaluating r j and ∇r j successively for $j = 1, 2, . . . , m$
  * The Gauss–Newton steps can then be computed by
    solving the system (10.23) of normal equations directly.
* Implementations of the Gauss–Newton method usually perform a line search in
  the direction $p_k^{GN}$ ,
  * requiring the step length αk to satisfy conditions like those discussed in
    Chapter 3, such as the Armijo and Wolfe conditions; see (3.4) and (3.6).

### convergence of the gauss–newton method
TODO

### methods for large-residual problems
* On large-residual problems, the asymptotic convergence rate of Gauss–Newton and
  Levenberg–Marquardt algorithms is only linear—slower than the superlinear convergence
  rate attained by algorithms for general unconstrained problems, such as Newton or quasi-Newton.
