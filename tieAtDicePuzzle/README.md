# Puzzle statement

I was watching two people roll dice to decide who goes first in a game. (assume that whoever wins is whoever gets the largest sum) One of them said, "my rule is if we tie, we have to add another die"
I was thinking, statistically, it makes it more likely to roll around the average the more dice you roll... So are you more likely to tie rolling one die, or more?

# My solution

The phrase "it makes it more likely to roll around the average the more dice you roll" is a bit misleading. If you are talking about the sample average of rolling $n$ dice, then this will indeed get closer on average to 3.5 the more dice you add. That is a bit misleading for this puzzle though because what we really care about is not the average of $n$ dice, but the sum of $n$ dice, and the variance of this only increases as you add $n$ dice.


To find the variance of a single fair six-sided die, we use the formula:

$\text{Var}(X) = E[X^2] - (E[X])^2$

$E[X] = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} =  \frac{7}{2}$

$E[X^2] = \frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6} = \frac{91}{6}$


$\text{Var}(X)= E[X^2] - (E[X])^2=  \frac{91}{6} - (\frac{7}{2})^2 =  \frac{35}{12} \approx 2.917$

$\text{SD}(X)= \sqrt{\frac{35}{12}} \approx 1.71$

Since variance adds, the Standard Deviation of the sum of $n$ dice is about $(1.71)\sqrt{n}$, which only increases as n gets larger.

Therefore, if the spread of the distribution of possible sums increases as you add more dice, there is no reason that we should expect the sums of both players to start matching more often as more dice are added. On the contrary, ties should become more rare.


The calculateProbabilityOfTie function in tieAtDice.py calculates the probability of tying with $n$ dice, assuming you already have made it to the point of having $n$ dice. In other words, assuming you are both rolling $n$ dice, this function calculates the probability that you get the same sum.

It does this by calculating:

$P(Tie;n=1) = (1/6)^2 + (1/6)^2 + (1/6)^2 + (1/6)^2 + (1/6)^2 + (1/6)^2$
$P(Tie;n=2) = (1/36)^2 + (2/36)^2 + (3/36)^2 + (4/36)^2 + (5/36)^2 + (6/36)^2 + (5/36)^2 + (4/36)^2 + (3/36)^2 + (2/36)^2 + (1/36)^2$

$\text{and so on...}$

Here is the output of this function run on the first 15 values for $n$:

| Number of dice (n) | Probability of a tie |
|---------------------|----------------------|
| 1                   | 0.16666666666666669  |
| 2                   | 0.11265432098765434  |
| 3                   | 0.09284979423868313  |
| 4                   | 0.08094350137174211  |
| 5                   | 0.07269280597469897  |
| 6                   | 0.06653879609578017  |
| 7                   | 0.061721663719588975 |
| 8                   | 0.05781854587192967  |
| 9                   | 0.05457283023445428  |
| 10                  | 0.051818590196608845 |
| 11                  | 0.04944315689335756  |
| 12                  | 0.047366986256288365 |
| 13                  | 0.04553210761443116  |
| 14                  | 0.0056384059003368485|
| 15                  | 0.00030146500742003675|


As the table shows, $P(Tie;n)$ is a monotonically decreasing function.

Therefore, you are more likely to tie with one tie and ties will only get less likely as you add more dice.