# Optimization
See also:
* https://github.com/tttor/dl-foundation/tree/master/method/optim
* https://github.com/tttor/rl-foundation/tree/master/method/policy-based/optim

# Book
* Convex Optimization; Boyd and Vandenberghe
  * https://web.stanford.edu/~boyd/cvxbook/
* First-Order Methods in Optimization, Amir Beck, 2017
  * https://epubs.siam.org/doi/book/10.1137/1.9781611974997
* Iterative Methods for Optimization, C.T. Kelley
  * https://archive.siam.org/books/kelley/fr18/
* Linear and Nonlinear Optimization, Igor Griva, Stephen G. Nash, Ariela Sofer
  * http://math.gmu.edu/~igriva/book/book-index.html
* Numerical Methods for Least Squares Problems, Åke Björck
  * https://epubs.siam.org/doi/book/10.1137/1.9781611971484
* Numerical Optimization; Jorge Nocedal, Stephen J. Wright
  * http://users.iems.northwestern.edu/~nocedal/book/index.html
* Optimization Algorithms on Matrix Manifolds
  * https://www.jstor.org/stable/j.ctt7smmk, P.-A. Absil et al
* Practical Methods of Optimization, R. Fletcher
  * https://ebookcentral-proquest-com.ezproxy.library.uq.edu.au/lib/uql/detail.action?docID=1212544
  * https://onlinelibrary-wiley-com.ezproxy.library.uq.edu.au/doi/pdf/10.1002/9781118723203
* Trust region methods, Andrew R. Conn , Nicholas I. M. Gould and Philippe L. Toint
  * https://epubs.siam.org/doi/book/10.1137/1.9780898719857
* Introductory Lectures on Convex Optimization: A Basic Course, Yurii Nesterov

# Course, workshop, tutorial
* http://people.seas.harvard.edu/~yaron/AM221-S16/index.html
* https://web.stanford.edu/class/ee364a/
* https://ipvs.informatik.uni-stuttgart.de/mlr/marc/teaching/13-Optimization/
* https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
* https://www.scipy-lectures.org/advanced/mathematical_optimization/
> Mathematical optimization is very... mathematical. If you want performance, it really pays to read the books.
* https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/quadratic-approximations/a/quadratic-approximation
* https://github.com/llSourcell/Second_Order_Optimization_Newtons_Method
* http://videolectures.net/deeplearning2015_schmidt_smooth_finite/
* Sebastien Bubeck: Five Miracles of Mirror Descent
  * https://www.youtube.com/watch?v=5DIZCxcfeWU

# Tool
## autograd, autodiff
* http://www.autodiff.org/
* https://github.com/HIPS/autograd

## optim package, software
* http://www.optimojoe.com/products/optizelle/
* http://www.cvxpy.org/
* https://docs.scipy.org/doc/scipy/reference/optimize.html
* https://github.com/adefazio/phessianfree
* https://github.com/BRML/climin
* https://www.cs.ubc.ca/~schmidtm/Software/minFunc.html
* https://cs.nyu.edu/faculty/overton/software/nlcg/index.html
* https://web.stanford.edu/group/SOL/software.html

# Misc
* http://math.gmu.edu/~igriva/book/Appendix%20D.pdf # Least squares
* https://www.benfrederickson.com/numerical-optimization/
* https://stats.stackexchange.com/questions/55247/how-to-choose-the-right-optimization-algorithm
* https://math.stackexchange.com/questions/189644/intuition-behind-gradient-vs-curvature
* https://math.stackexchange.com/questions/2201384/what-is-the-definition-of-a-first-order-method
* https://math.stackexchange.com/questions/189644/intuition-behind-gradient-vs-curvature
* https://www.quora.com/What-are-some-good-resources-to-learn-about-optimization
* https://math.stackexchange.com/questions/905327/definition-of-global-convergence
  * https://math.stackexchange.com/questions/1554269/global-convergence-versus-convergence-to-a-global
* https://en.wikipedia.org/wiki/Condition_number
  * https://en.wikipedia.org/wiki/Well-posed_problem
  * https://blogs.mathworks.com/cleve/2017/07/17/what-is-the-condition-number-of-a-matrix/
  * ill-conditioned: that a small error in the initial data can result in much larger errors in the answers.
  * An ill-conditioned problem is indicated by a large condition number.
* https://en.wikipedia.org/wiki/Rate_of_convergence
  * https://math.stackexchange.com/questions/2615576/sublinear-rate-of-convergence-in-mathematical-optimization
* convex vs non-convex opt, http://dx.doi.org/10.1561/2200000058
  * An optimization problem is said to be convex if the objective is a convex function,
    **as well as** the constraint set is a convex set.
  * An optimization problem that violates **either one** of these conditions, i.e.,
    one that has a non-convex objective, or a non-convex constraint set, or both, is called a non-convex optimization problem.
* https://stats.stackexchange.com/questions/228874/why-use-m-k-to-approximate-f-k-in-trust-region-method-for-optimization

## non-smooth optimization
* https://www.cs.ubc.ca/labs/lci/mlrg/slides/2015_DLSS_NonSmoothNonFiniteNonConvex.pdf
* http://www.iro.umontreal.ca/~memisevr/dlss2015/2015_DLSS_NonSmoothNonFiniteNonConvex.pdf
* http://videolectures.net/deeplearning2015_schmidt_nonsmooth_nonfinite/

## test function
* https://en.wikipedia.org/wiki/Test_functions_for_optimization
* https://www.sfu.ca/~ssurjano/optimization.html
* http://infinity77.net/global_optimization/test_functions.html#test-functions-index
* http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO.htm
* https://arxiv.org/abs/1308.4008
* http://www.cuter.rl.ac.uk/Problems/mastsif.shtml
  * https://github.com/optimizers/cutest-mirror
  * https://link.springer.com/article/10.1007/s10589-014-9687-3
  * https://github.com/kenjydem/CUTEST.py
  * https://jfowkes.github.io/pycutest/_build/html/index.html

## benchmark
* http://www.timmitchell.com/software/betaRMP/

## conjugate gradient (CG)
* https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf
* http://ikuz.eu/2015/04/15/the-concept-of-conjugate-gradient-descent-in-python/
* https://en.wikipedia.org/wiki/Conjugate_gradient_method
* https://cs.nyu.edu/faculty/overton/software/nlcg/index.html
* http://learning.eng.cam.ac.uk/carl/code/minimize/
* http://andrew.gibiansky.com/blog/machine-learning/conjugate-gradient
* http://people.cs.vt.edu/~asandu/Public/Qual2011/Optim/Hager_2006_CG-survey.pdf

## steepest descent
* https://people.seas.harvard.edu/~yaron/AM221-S16/lecture_notes/AM221_lecture10.pdf

