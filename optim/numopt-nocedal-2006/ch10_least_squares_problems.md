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
