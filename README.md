# Smart Campus Energy Management System

## Project Overview
This repository contains the complete systems engineering lifecycle—from preliminary systems analysis to robust software design, project management, and computational simulation—for a Smart Campus Energy Management System. Focused on the Engineering Faculty building of Universidad Distrital Francisco José de Caldas, the project evolves from evaluating human-driven energy waste to validating a decentralized, software-defined Proof of Concept (PoC) with autonomous user-space agents.

## Authors (Engineering Team)
* **Omar Yesid Fonseca López** - oyfonsecal@udistrital.edu.co
* **Daniel Felipe Barrera Suárez** - dfbarreras@udistrital.edu.co
* **Daniel Mateo Ballesteros Molina** - dmballesterosm@udistrital.edu.co
* **Dania Lizeth Guzmán Triviño** - dlguzmant@udistrital.edu.co

## Repository Structure
Following the Computer Science Collaboration Guidelines, the repository is organized as follows:
* `/assets/diagrams/`: System architecture diagrams, flowcharts, and performance charts.
* `/data/`: Primary datasets collected during field research (Workshop 1).
* `/docs/`: Final IEEE format papers and design documents (Workshops 1 & 2).
* `/src/agent/`: Autonomous telemetry agent source code for production (Python).
* `/Workshop3_Management/`: Project Management and Enhanced Design Document.
* `/Workshop_4_Simulation/`: System Simulation Report, simulator code (`/code`), and synthetic datasets (`/results`).

---

## Phase 1: Systems Analysis (Workshop 1)
To validate the necessity of an automated architecture, we triangulated Direct Observation, Structured Surveys (n=35), and Environmental Correlation. The analysis revealed a significant gap between sustainability perception and practical actions, demonstrating that energy waste is primarily driven by human behavioral inertia.

## Phase 2: Systems Design (Workshop 2)
Given strict institutional IT constraints (no administrator privileges), the design pivoted to a decentralized, **Software-Defined (User-Space)** architecture using Python executables (`.exe`), behavioral nudges, and local OS Suspend states.

## Phase 3: Robust Design & Project Management (Workshop 3)
This phase elevated the conceptual design into a production-ready PoC by introducing fault-tolerance mechanisms (Encrypted CSV Fallbacks for firewall blocks), strict CPU load validation (>20%), and a comprehensive project execution plan (ISO 31000 Risk Management).
* **Deliverables:** [Project Management and Enhanced Design Document](./Workshop3_Management/Workshop_3_Report.pdf)

## Phase 4: System Simulation and Validation (Workshop 4)
We implemented a discrete-event simulation model in Python to test the architecture against stochastic campus variables (e.g., 80% forgetfulness probability, 15% high-CPU load probability). 
* **Key Finding:** The autonomous agent achieved a **68.72% net reduction** in wasted energy while successfully avoiding false positives that could disrupt critical academic workflows. 
* **Complexity Analysis:** Sensitivity analysis proved that the 20% CPU threshold acts as the system's optimal attractor, preventing system paralysis caused by background OS noise.

**Phase 4 Deliverables:**
* [📄 System Simulation and Validation Report (PDF)](./Workshop_4_Simulation/Workshop_4_Report.pdf)
* [💻 Discrete-Event Simulator Source Code](./Workshop_4_Simulation/code/simulator.py)
* [📊 Data Visualization Script](./Workshop_4_Simulation/code/plot_results.py)
* [📈 Synthetic Telemetry Dataset](./Workshop_4_Simulation/results/simulation_results.csv)