# ch_2_axiom_of_prob.md

# 2.1 Intro
* Goal: to compute the probability of an event

# 2.2 Sample space and events
* Sample space $S$ of the experiment: the set of all possible outcomes of an experiment
  * Example 3:
    If the experiment consists of flipping two coins, then the sample space
    consists of the following four point:
    $S = \{ (H, H), (H, T), (T, H), (T, T) \}$
* Event $E$:
  * is any subset of the sample space
  * is a set consisting of possible outcomes of the experiment
  * In example 3:
    if $E = \{ (H, H), (H, T) \}$, then $E$ is the event that a head appears on the first coin
  * If the outcome of the experiment is contained in $E$,
    then we say that $E$ has occured
* Union of the event $E$ and $F$
  * consists of all outcomes that are either in $E$ or in $F$ or in both
  * is denoted by $E \cup F$
* Intersection of the event $E$ and $F$
  * consists of all outcomes that are both in $E$ and in $F$
  * is denoted by $E \cap F$, or simply $EF$
  * If $EF = \emptyset$, then $E$ and $F$ are said to be mutually exclusive
* Complement of $E$
  * consists of all outcomes in the sample space $S$ that are not in $E$
  * is denoted by $E^c$
* Subset and superset
  * For any two events $E$ and $F$, if all of the outcomes in $E$ are alse in $F$,
    then we say that $E$ is contained in $F$, or $E$ is a subset of $F$, and
    write $E \subset F$ (or equivalently, $F \supset E$)
  * If $E \subset F$ and $F \subset E$, we say that $E$ and $F$ are equal
    and write $E = F$
  * Illustrate the logical relations among events using the Venn diagram
* The operations of forming unions, intersections, and complemenets of events
  obey certain rules similar to the rules of algebra,
  * For example, commutative, associative, and distributive laws
  * Also recall the DeMorgan's laws

# 2.3 Axioms of probability
* Relative frequency definition of probability
  * For each event $E$ of the sample space $S$, we define $n(E)$ to be the number of times
    in the first $n$ repetitions of the experiment that the event $E$ occurs
    * Then $P(E)$, the probability of the event $E$, is defined as
      * $P(E) = \lim_{n \to \infty} \frac{n(E)}{n}$
  * Rely on an assumption or axiom of the system that
    $n(E)/n$ will necessarily converge to some constant value
    * but, it does not seem to be a priori evident that this need to be the case
    * therefore, we should have more reasonable assumptions that are more self-evident,
      then attempt to prove that such constant frequency does exist
* Assume that, for each event $E$ in the sample space $S$,
  there exists a value of $P(E)$, referred to as the probability of $E$
  * further assume that all these probabilities satisfy a certain set of axioms
  * when the sample space is an uncountably infinite set,
    $P(E)$ is defined only for a class of events called measurable
* Three axioms of probability
  * Axiom 1: $0 \le P(E) \le 1$
    * that the probability that the outcome of the experiment is an outcome in $E$
      is some number between $0$ and $1$
  * Axiom 2: $P(S) = 1$
    * that with probability 1, the outcome will be a point in the sample space $S$
  * Axiom 3: For any sequence of mutually exclusive events $E_1, E_2, \ldots.
    That is, events for which $Ei$j = \emptyset when i \ne j$,
    * $P\Big( \bigcup_{i=1}^\infty E)i \Big) = \sum_{i=1}^\infty P(E_i)$
    * that for any sequence of mutually exclusive events,
      the probability of at least one of these events occuring is just the sum of their respective probabilities
* If a die is rolled and we suppose that all six sides are equally to appear,
  then we would have $P(\{1\}) = P(\{2\}) = ... = P(\{6\}) = \frac{1}{6}$.
  * From axiom 3, the probability of rolling an even number would equal
    * $P( \{ 2, 4, 6 \}) = P(\{2\}) + P(\{4\}) + P(\{6\}) = 3 \frac{1}{6} = \frac{1}{2}$
* The strong law of large numbers:
  * that if an experiment is repeated over and over again, then,
    with probability 1, the proportion of time during which any specific event $E$ occurs will equal $P(E)$

# 2.4 Some simple proportions
* Proposition 4.1:
  * P(E^c) = 1 - P(E)
* Proposition 4.2:
  * If $E \subset F$, then $P(E) \le P(F)$.
  * Eg: the probability of rolling a 1 with a die is less than or equal to
    the probability of rolling an odd value with the die
* Proposition 4.3
  * $P(E \cup F) = P(E) + P(F) - P(EF)$
