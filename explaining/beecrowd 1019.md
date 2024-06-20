# Explaining Beecrowd 1019

We need to understand how to convert a given number of seconds into hours, minutes and seconds

## Understanding the Basics
- 1 minute has 60 seconds
- 1 hour has 60 minutes
- 1 hour has 3600 seconds (60 minutes * 60 seconds)

## Solving the Problem

### Calculating Hours
- Divide the total number of seconds by 3600 to get the number of hours. The quotient is the number of hours

### Calculating Minutes
- Take the remainder of the division of the total number of seconds by 3600.
- Divide this remainder by 60 to get the number of minutes. The quotient is the number of minutes

### Calculating Seconds
- Take the remainder of the division of the remainder by 60. This is the number of seconds

## Example

Assuming we have 7625 seconds

### Hours
- 7625 / 3600 = 2 hours (with a remainder of 425)
- So, there are 2 hours
### Minutes
- 425 / 60 = 7 minutes (with a remainder of 25)
- So, there are 7 minutes
### Seconds
- The remainder is 25
- So, there are 25 seconds

