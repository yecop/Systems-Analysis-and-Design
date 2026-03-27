# Smart Campus Energy Management System: A Systems Analysis Approach

## Project Overview
This repository contains the preliminary systems analysis for a Smart Campus Energy Management System, designed to evaluate and optimize energy usage in the Engineering Faculty building of Universidad Distrital Francisco José de Caldas. The project utilizes IoT monitoring concepts to map human behavior and implement automated recommendations, aiming to significantly reduce energy waste.

## Authors
* **Omar Yesid Fonseca López** - oyfonsecal@udistrital.edu.co
* **Daniel Felipe Barrera Suárez** - dfbarreras@udistrital.edu.co
* **Daniel Mateo Ballesteros Molina** - dmballesterosm@udistrital.edu.co
* **Dania Lizeth Guzmán Triviño** - dlguzmant@udistrital.edu.co

## Repository Structure
* `/data`: Contains the primary datasets collected during the field research.
  * `observacion_directa.csv`: Logs of physical walkthroughs checking occupancy vs. energy waste.
  * `luminosidad_caso_1_sin_lluvia_pico_13_00.csv`: Environmental daylight correlation data (Case 1: Sunny day with peak luminosity at 13:00).
  * `luminosidad_caso_2_lluvia_16_00_pico_09_00.csv`: Environmental daylight correlation data (Case 2: Rainy afternoon with an early peak at 09:00).
  * `luminosidad_caso_3_lluvias_08_00_15_00_picos_07_00_12_00_16_30.csv`: Environmental daylight correlation data (Case 3: Intermittent rain and multiple weather fluctuations).
  * `Datos_encuestas.csv`: Raw structured survey responses from 35 participants regarding their energy consumption habits and institutional awareness.
  * `observacion_directa.csv`: Logs of physical walkthroughs in classrooms and labs, cross-referencing occupancy status with energy waste (lights and computers left on in empty rooms).
* `/docs`: Contains the final IEEE format paper (`.pdf`) and the LaTeX source code.
  * `Workshop_1.pdf` & `Workshop_1.tex`: Phase 1 - Systems Analysis.
  * `Workshop_2.pdf` & `Workshop_2.tex`: Phase 2 - System Design Document (includes TikZ native diagrams).
* `/assets`: Contains the system architecture diagrams and survey data visualizations.
  * `/Grafico_Encuestas.png`:Pie chart showing the frequency of manual light switch-off.
  * `IMG-20260307-WA0006`:Data Architecture and Analytical Flow.
  * `IMG-20260307-WA0007`:Detailed IoT architecture and data flow diagram.

## Methodology (Primary Data Collection)
To validate the necessity of an automated IoT architecture, we triangulated three non-invasive data collection techniques:
1. **Direct Observation:** Quantifying the frequency of energy waste (lights/computers left on in empty rooms).
2. **Structured Surveys (n=35):** Assessing user awareness and the "human-in-the-loop" bottleneck.
3. **Environmental Correlation:** Measuring natural light levels (lux) to identify Daylight Harvesting opportunities.

## Key Findings
The analysis revealed a significant gap between sustainability perception and practical actions. The manual management of energy relies heavily on human memory, creating an inertia phenomenon where energy waste is normalized. Transitioning to an automated, IoT-based architecture is highly justified to mitigate human error and provide real-time efficiency alerts.

---
