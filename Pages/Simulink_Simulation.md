[![image](https://user-images.githubusercontent.com/34621440/94373930-5ab4e680-00ce-11eb-9140-2131acbb4592.png)](https://utkarshcrazy.github.io/hyperloop/)

# Simulation

Target: Designing a practical pod characterization process and configurable simulation to aid control system

Why we are doing model based design and simulation?
  - For efficient motor & battery operation
  - to visualize torque envelope for the motor
  - to realize how my state of charge the battery changes over the drive cycle
  - to get rough idea about battery discharge per km
  - Aiming to play with motor power and vehicle body inputs like rolling resistance ,air drag and weight etc to check out performance.
  
#### Working on
- Part 1: Simulink  # equation based approach
- part 2: Powertrain with esc+battery #
- part 3 complete powertrain+motor+pwm simscape model
>![image](https://user-images.githubusercontent.com/34621440/94374432-d95f5300-00d1-11eb-999a-608ccc0bb810.png)
### Requirements:
* [Mathematics] - flight dynamics model including torque rpm relation, throttle% to rpm, time constant delay
* Test system where we can collect data for finding the parameters required for modeling <throttle control mode and esc scaling>
* •	In test setup we will send the data in real time to computer through raspberry pi, this data -> imported to MATLAB ( here we can make a convenient GUI to run analysis function to analyze the data 
