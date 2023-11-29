# greedy-algorithms
 A greedy algorithms arrives at a solution by making a sequence of choices each of which looks best at the time.
 
1. Greedy method suggests you can decide an algorithm that works in stages .... considering one input at a time.
2. At  each stage a decision is made regarding whether a particular input is an optimal solution.
3. This is done by considering the inputs order
4. If the inclusion of the next input into a partially constructed optimal solution would result in an infeasible solution, the input is not used.
   
    - **Selection** : select an input from **a[]** and remove it 
    - **Feasible** : a predicate function that determines if **x** can be included into the solution vector. 
    - **Union**: combine **x** with partial solution.

# Greedy (int n, a[])
  - Solution = Empty
  - for (i = 1; i<=n;i++)
    - x = Select(a)
    - if (Feasible(Solution,x))
      - Solution = Union(Solution,x)
  - return Solution
 