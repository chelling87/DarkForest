# DarkForest
A simulation of the dark forest

## Idea
Use cellular automoton to simulate how civilizations in the galaxy interact with one another

### Setup
Say, 100 X 100 grid of solar systems. Populated by some percent.

#### Civilization properties
##### Intrinsic 
- malicious => true/false
- technological growth rate ?
##### Dynamic
- population size
- number of solar systems occupied
- resources
- technological prowess/power

#### Evolution
- population size grows proportional to resources and technological prowess
  - Increase if has enough resources and technological prowess
  - Decrease if not enough resources or low technological prowess
- technological prowess exponential grows according to technological growth rate and population size
- if civ. has enough technological prowess, will expand to find more resources
- if malicious, will kill any weaker civ.
- if not malicious, will reach out to try to join another non-malicious civ.
  - if other civ. was malicious and stronger, original civ. dies
  - if other civ. was malicious and weaker, other civ. dies. Chance that original becomes malicious
  - if other civ. wasn't malicious, they combine
