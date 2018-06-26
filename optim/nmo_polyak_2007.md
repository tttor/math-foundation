# Newton’s method and its use in optimization
* B.T. Polyak
* European Journal of Operational Research 181 (2007) 1086–1096

## intro
* the polynomial time interior point algorithms in convex optimization
  are based on Newton’s method.

## 2. Idea and history of the method
* basic idea of Newton’s method (in 1669)
  * linearization
  * suppose $F: \mathbb{R} \mapsto \mathbb{R}$
  * we are finding the root of $F$, i.e.
    solving $F(x) = 0$
  * eg $F(x) = x^3 - 2x - 5 = 0$
  * The starting approximation for the root was $x = 2$
  * $F(2 + h) = h^3 + 6h^2 + 10h - 1$
  * neglecting higher order terms, Newton got the linear equation
    $10h - 1 = 0$
  * Thus the next approximation is $x = 2 + 0.1 = 2.1$ and
  * the process can be repeated for this point
* J. Raphson, who proposed in 1690 the general form of
  method (2) (i.e., F(x) was not assumed to be a poly-
  nomial only and the notion of a derivative was
  * solving for $F(x) = 0$
  * Starting from an initial point $x_0$,
     we can construct the linear approximation of $F(x)$ in
    the neighborhood of $x_0: F(x_0 + h)  \approx F(x_0) + F'(x_0)h$
  * and solve the arising linear equation $F(x_0) + F'(x_0)h = 0$
  * Thus, we arrive at recurrent method
    * $x_{k+1} = x_k - {F'(x_k)}^{-1} F(x_k)$
    * $k = 0, 1, \ldots$
