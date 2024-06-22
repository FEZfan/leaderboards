# leaderboards

## create leaderboard
```python3
lb = Leaderboard(3) #standard leaderboard with 3 entries
```
or pass a function for comparisons
```python3
lb = Leaderboard(3, lambda a,b : a<b) #lowest numbers
lb = Leaderboard(500, lambda a,b : a.score>b.score) #highest scores
```

## add to leaderboard

```python3
lb = Leaderboard(3)
lb.add(5) # place 5 on leaderboard
lb.add(4) # appears 2nd, below 5
lb.add(60) # appears 1st, above 5
lb.add(1) # will not be placed on leaderboard
```

## print leaderboard

```python3
>>> lb.print()
60
5
4
```

## convert to list

```
>>> lb.toList()
[4, 5, 60]
