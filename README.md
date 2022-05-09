# bag
bag - bitcoin address generator. Generator of custom Bitcoin addresses.
## Setup
```
git clone https://github.com/GREYSERGING/bag.git
cd bag
```

## Using
```
Use : bag.py [-h] [-t %] [-ms] [-st] [-op %] [-ds] [-p2s %] [-p2pf %]
  [-h] - help message
  [-t] - number of threads
  [-ms] - max speed (no notifications)
  [-st] - stop after finding
  [-ds] - disable saving
  [-p2s] - path to save (standard "ADDRESS.TXT")
  [-op] - one pattern
  [-p2pf] - path to patterns file
```
> :warning: No need to write the front digit.

You can create your own file with patterns by specifying each one from a new line (without spaces).

## Example
```
Example:
 bag.py -t 2 -p2s addresses.txt -p2pf pattern.txt
 bag.py -t 2 -ms -ds -op address
```
