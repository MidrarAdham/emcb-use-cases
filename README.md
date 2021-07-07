# emcb-usecases

Test and validate the benefit of Energy-Management-Circuit-Breakers with Actual DERs.

### Objectives:
In this project, we study the benefits of EMCBs in demand response and peak load mitigation.

### DERs:

Distributed Energy Resources used in this study include the following:

* A. O. Smith Electrical Water Heater.
* A. O. Smith Hybrid Water Heater.
* NHR 9430 Load Simulator (Simulating EVs)

### Simulation:

The simulation part of this project uses GridLAB-D. GridLAB-D is an open source ssoftware developed by PNNL.

### Use-cases:

* Programmable Load Control.
* Load Research.
* EV Managed Charging.
* Cold Load Pickup Mitigation.
* Islanding Support

### Data Files Naming Convention:

\<EWH\>-\<HPWH\>-\<HPWH_mode\>

For example, if a heat pump water heater is in a Hybrid mode:

* ewh_hpwh_Electric

Heat_Pump_Water_Heater is in Resistive Mode.

* hpwh_ewh_Hybrid

Heat_Pump_Water_Heater is in Heat Pump Mode.
