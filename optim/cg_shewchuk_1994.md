# An Introduction to the Conjugate Gradient Method Without the Agonizing Pain
* Jonathan Richard Shewchuk

# 1. Introduction
* CG is effective for solving large systems of linear equations, in the form of
  * $Ax = b$, where
     * $x$ is an unknown vector,
     * $b$ is a known vector, and
     * $A$ is a known, square, symmetric, positive-definite (or positive-indefinite) matrix.
* Iterative methods like CG are suited for use with sparse matrices

# 2. Notation
* capital letters to denote matrices,
* lower case letters to denote vectors,
* Greek letters to denote scalars

# 3. The Quadratic Form
* The gradient is a vector field that, for a given point $x$, points in the direction of greatest increase of $f(x)$.
* Because the solution is a saddle point, Steepest Descent and CG will not work

# 4. The Method of Steepest Descent
* the residual as
  * the direction of steepest descent
  * how far we are from the correct value of $b$
* the zigzag path, which appears because each
  gradient is orthogonal to the previous gradient.

# 5. Thinking with Eigenvectors and Eigenvalues
* the eigenvalues of the identity matrix $I$ are all one, and every nonzero vector is an eigenvector of $I$ .
* the eigenvalues of a positive-definite matrix are all positive

# 6. Convergence Analysis of Steepest Descent
TODO

# 7. The Method of Conjugate Directions
* to make the search directions A-orthogonal instead of orthogonal
* conjugate Gram-Schmidt process: to generate a set of A-orthogonal directions
  * difficulty: all the old search vectors must be kept in memory to construct each new one
    * CG, which is a method of Conjugate Directions, cured these disadvantages.

# 8. The Method of Conjugate Gradients
* CG is simply the method of Conjugate Direction,
  where the search directions are constructed by conjugation of the residuals
  * First, the residuals worked for Steepest Descent, so why not
    for Conjugate Directions?
  * Second, the residual has the nice property that it’s orthogonal to the previous
    search directions (Equation 39), so it’s guaranteed always to produce a new, linearly independent search
    direction unless the residual is zero, in which case the problem is already solved
* Kyrlov subspace
* $\beta$: the Gram-Schmidt constants
* The name “Conjugate Gradients” is a bit of a misnomer,
  * because the gradients are not conjugate, and the conjugate directions are not all gradients.
  * “Conjugated Gradients” would be more accurate

# 9. Convergence Analysis of Conjugate Gradients
TODO

# 10. Complexity
TODO

# 11. Starting and Stopping
* If you have a rough estimate of the value of $x$, use it as the starting value
* If not, set $x=0$; either Steepest Descent or CG will eventually converge when used to solve **linear** systems.
* When Steepest Descent or CG reaches the minimum point, the residual becomes zero,
* stop immediately when the residual is zero
* accumulated roundoff error in the
  recursive formulation of the residual (Equation 47) may yield a false zero residual; this problem could be
  resolved by restarting with Equation 45
* it is small customary fraction to of stop the norm of the residual falls below specific value


# 12. Preconditioning
* Preconditioning is a technique for improving the condition  number of a matrix.
* Transformed Preconditioned Conjugate Gradient Method
* UNtransformed Preconditioned Conjugate Gradient Method
* The effectiveness of a preconditioner
  * not necessary to compute $M^{-1}$, but only necessary to compute $M^{-1}v$
* it is generally accepted that for large-scale applications,
  CG should nearly always be used with a preconditioner

# 13. Conjugate Gradients on the Normal Equations
TODO

# 14. The Nonlinear Conjugate Gradient Method
TODO
