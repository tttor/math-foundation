# ch07: Large-Scale Unconstrained Optimization
*  objective functions in large problems often possess a structural property known as partial separability,
  which means they can be decomposed into a sum of simpler functions, each of which depends on only a small subspace of IR n
* dealing with the hessian
  * factorization
  * approximations to the Newton step using iterative linear algebra techniques


## 7.1
* familiy of inexact Newton methods
  * obtaining approximations to pk N that are inexpensive to calculate but are good search directions or steps
* Hessian-free manner,
  * the Hessian ∇ 2 f k need not be calculated or stored explicitly at all.

### line search newton–cg method (aka truncated Newton method)
* When the Hessian ∇ 2 f k is nearly singular, the line search Newton–CG direction can be long and of poor quality,
  requiring many function evaluations in the line search and giving only a small reduction in
  the function
* Hessian-free Newton methods.
  *  does not require explicit knowledge of the Hessian Bk  ∇ 2 fk .
  * Rather, it requires only that we can supply Hessian–vector products of the form ∇ 2 fk d for any given vector d.
* The price we pay for
  bypassing the computation of the Hessian is one new gradient evaluation per CG iteration.
