# PLL Phase Noise Modeler

This repository contains a Python script for modeling and exporting system-level phase noise profiles for Phase-Locked Loop (PLL) subsystems. In mixed-signal system modeling, accurately estimating the phase noise contributions (both flicker and thermal noise) of individual blocks is critical for predicting overall jitter and phase margin.

This tool calculates theoretical noise profiles across a specified frequency range for the VCO, Charge Pump, Reference Oscillator, and frequency dividers, automating the extraction of this data into a clean CSV format for further integration into system-level simulations.

## Features
* **Component-Specific Noise Modeling:** Calculates theoretical $1/f$ (flicker) and thermal noise profiles for standard PLL components.
* **Charge Pump Scaling:** Automatically adjusts the charge pump noise floor based on the designed $I_{cp}$ versus a reference current.
* **Automated CSV Extraction:** Compiles all frequency vectors and corresponding phase noise values (in dBc/Hz) into a structured CSV file for easy import into MATLAB, Excel, or other system-level simulators.

## Prerequisites
To run this script, you need Python installed along with the `numpy` library.
```bash
pip install numpy
