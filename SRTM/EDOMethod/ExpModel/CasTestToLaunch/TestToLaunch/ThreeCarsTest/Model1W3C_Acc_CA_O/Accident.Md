# Simple Model with 3 Cars to Simulate the Accordion Aspect on the Road

In this simulation, we model the accordion aspect on the road involving three cars:

- The `x2` car is a little bit nervous, not slowing down if the car in front brakes and increasing speed if there is enough distance.
- The `x3` car is prudent, slowing down very fast if the car in front slows down and accelerating slowly.
- The `x1` car encounters an obstacle (linear modelisation) every 10 meters, causing it to slow down.

## Parameters:

- `lambda2`: 10.0
- `h`: 1.0
- `d2`: 1.0
- `nameCase`: "Simulation of Accident Phenomenon"
- `lambda3`: 5.0
- `d3`: 2.0
- `V1max`: 120 * (1000 / 3600) # Maximum speed of the first car
- `V2max`: 160 * (1000 / 3600) # Maximum speed of the second car
- `V3max`: 180 * (1000 / 3600)
