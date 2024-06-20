# Explaining Beecrowd 1021

## Understanding the Basics

Brazilian currency denominations:
- Notes: 100, 50, 20, 10, 5, 2 (in Reais)
- Coins: 1.00, 0.50, 0.25, 0.10, 0.05, 0.01 (in Reais)

## Solving the Problem

- First, we see how many R$ 100 notes (the largest denomination) we can use without exceeding our total amount.
- Then, we see how many R$ 50 notes we can use with the remaining amount.
- We continue this process for each denomination, from largest to smallest.
- Finally, we print out the number of each denomination used.

## Example

Assume we have R$ 576.73
- We can use 5 R$ 100 notes
- We can use 1 R$ 50 note
- We can use 1 R$ 20 note
- We can use 1 R$ 5 note
- We can use 1 R$ 1 coin
- We can use 1 R$ 0.50 coin
- We can use 2 R$ 0.10 coins
- We can use 3 R$ 0.01 coins