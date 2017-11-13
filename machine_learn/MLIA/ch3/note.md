# decision trees
* 香农熵： -sum(p_xi * log(p_xi, 2))
* 先计算dataset的熵，用多少类计算，
  * 比如 [1,1,no],[1,0,no],[0,1,yes],[0,0,no]
  * 熵为 -(0.75 * log(0.75, 2) + 0.25 * log(0.25, 2))
* 测试中午