# leaderboards

## create leaderboard
```
lb = Leaderboard(3) #standard leaderboard with 3 entries
```
or pass a function for comparisons
```
lb = Leaderboard(3, lambda a,b : a<b) #lowest numbers
lb = Leaderboard(500, lambda a,b : a.score>b.score) #highest scores
```

## add to leaderboard

```
lb = Leaderboard(3)
lb.add(5) # place 5 on leaderboard
lb.add(4) # appears 2nd, below 5
lb.add(60) # appears 1st, above 5
lb.add(1) # will not be placed on leaderboard
```

## print leaderboard

```
>>> lb.print()
60
5
4
```

## convert to array

```
>>> lb.toArray()
[4, 5, 60]
