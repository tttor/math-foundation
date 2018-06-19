# Numerical Optimization
* Jorge Nocedal, Stephen J. Wright
* Second Edition; 2006 Springer Science+Business Media, LLC.

## preface
* focus on
  * continuous problems
    * cf discrete optimization problem, eg. integer programming
  * local optimization
  * large scale optimization techniques, such as
    * interior-point methods, inexact Newton methods,
      limited-memory methods, and the role of partially separable functions and automatic differentiation.
  * deterministic optimization problems,

## ch01: intro
* objective
  * a quantitative measure of the performance of the system under study
  * depends on certain characteristics of the system, called variables or unknowns or parameter,
  * often the variables are restricted, or constrained, in some way.
* modeling
  * The process of identifying objective, variables, and constraints for a given problem
* optimality conditions
  * for checking that the current set of variables is indeed the solution of the problem
* sensitivity analysis, which
  * reveals the sensitivity of the solution to changes in the model and data.
* Optimization algorithms
  * are iterative.
  * begin with an initial guess of the variable $x$ and
  * generate a sequence of improved estimates (called “iterates”) until they terminate, hopefully at a solution.
  * good algorithms should possess (trade-offs among these are central issues)
    * robusness: should perform well on a wide variety of problems in their class, for all reasonable values of the starting point.
    * efficiency: should not require excessive computer time or storage.
    * accuracy:  should be able to identify a solution with precision,
      without being overly sensitive to errors in the data or
      to the arithmetic rounding errors that occur when the algorithm is implemented on a computer

### taxonomy
* a linear programming problem
  * When the objective function and all the constraints are linear functions of $x$
* Nonlinear programming problems,
  * in which at least some of the constraints or the objective are nonlinear functions,
* Stochastic optimization algorithms
  * use the quantifications of the uncertainty to produce solutions that optimize the expected performance of the model
* robust optimization,
  * in which certain constraints are required to hold for all possible values of the uncertain data.
* deterministic optimization problems,
  * in which the model is completely known
* convex programming
  * a special case of the general constrained optimization problem (1.1) in which
    * the objective function is convex,
    * the equality constraint functions ci (·), i ∈ E, are linear, and
    * the inequality constraint functions ci (·), i ∈ I, are concave.

### Mathematically:
* $x$ is the vector of variables,
* $f$, objective fn: a (scalar) function of $x$ that we want to maximize or minimize;
* $c_i$ are constraint functions,
  * which are scalar functions of x that define certain equations and
    inequalities that the unknown vector x must satisfy.
* the optimization problem can be written
  * $min_{x \in R^n} f(x)$
    * subject to $c_i(x) = 0$, $i \in E$
    * subject to $c_i(x) \ge 0$, $i \in I$
    * $I$ and $E$ are sets of indices for inequality and equality constraints, respectively.


