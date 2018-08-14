# ch04: Trust-Region Methods
* use the quadratic model  of the objective function in different ways
  * Line search methods use it
    * to generate a search direction, and
    * then focus their efforts on finding a suitable step length α along this direction.
  * Trust-region methods
    * define a region around the current iterate within which they trust the model to
      be an adequate representation of the objective function, and
    * then choose the step to be the approximate minimizer of the model in this region.
    * thus:
      * choose the direction and length of the step simultaneously.
      * If a step is not acceptable, they reduce the size of the region and find a new minimizer
      * generally,  the direction of the step changes whenever the size of the trust region is altered.
* choose the size of the region according to the performance of the algorithm during previous iterations
* assume that the model function m k that is used at each iterate xk is quadratic
* the trust-region approach requires us
  * to solve a sequence of subproblems (4.3)
    in which the objective function and constraint are both quadratic.

## outline of the trust-region approach
TODO
