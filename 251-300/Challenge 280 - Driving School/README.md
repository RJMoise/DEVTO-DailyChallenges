Write a function that will charge driving students based on the amount of time they spent in their lessons. This particular school charges for lessons as follows:

Time                            Cost
************************************
Up to 1st hour                   $30
Every subsequent half hour**     $10
Subsequent charges are calculated by rounding up to nearest half hour.

For example, if student X has a lesson for 1hr 20 minutes, he will be charged $40 (30+10) for 1 hr 30 mins and if he has a lesson for 10 minutes, he will be charged $30 for the full hour.

Out of the kindness of its heart, the driving school also provides a 5 minutes grace period. So, if student X were to have a lesson for 65 minutes, he will only have to pay for an hour. Lessons under 5 minutes are just talks, so they should be considered free.

For a given lesson time in minutes (min), write a function price to calculate how much the lesson costs.

Tests
cost(84)
cost(102)
cost(273)

Good luck!