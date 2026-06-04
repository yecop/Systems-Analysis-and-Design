# Smart Campus Energy Management System: Analysis, Design & Management

## Project Overview
This repository contains the complete systems engineering lifecycle—from preliminary systems analysis to robust software design and project management—for a Smart Campus Energy Management System. Focused on the Engineering Faculty building of Universidad Distrital Francisco José de Caldas, the project evolves from utilizing IoT monitoring concepts to mapping human behavior, and ultimately designing a decentralized, software-defined Proof of Concept (PoC) with autonomous user-space agents, fault tolerance, and comprehensive risk mitigation.

## Authors (Engineering Team)
* **Omar Yesid Fonseca López** - oyfonsecal@udistrital.edu.co
* **Daniel Felipe Barrera Suárez** - dfbarreras@udistrital.edu.co
* **Daniel Mateo Ballesteros Molina** - dmballesterosm@udistrital.edu.co
* **Dania Lizeth Guzmán Triviño** - dlguzmant@udistrital.edu.co

## Repository Structure
Following computer science collaboration guidelines, the repository is organized as follows:
* `/assets/diagrams`: Contains the system architecture diagrams, flowcharts, and survey data visualizations (e.g., `Grafico_Encuestas.png`).
* `/data`: Contains the primary datasets collected during the field research (e.g., surveys, lux meter readings, direct observation logs).
* `/docs`: Contains the final IEEE format papers (`.pdf`) and the LaTeX source codes for Workshop 1 and Workshop 2.
* `/experiments` & `/results`: Directories reserved for future PoC testing and analytical outputs.
* `/references`: Directory for literature review and external bibliography.
* `/src/agent`: Autonomous telemetry agent source code (Python).
* `/Workshop_3_Management`: Contains the Enhanced System Design and Project Management Document (Workshop 3).

---

## Phase 1: Systems Analysis (Workshop 1)
### Methodology & Key Findings
To validate the necessity of an automated architecture, we triangulated three non-invasive data collection techniques: Direct Observation, Structured Surveys (n=35), and Environmental Correlation. The analysis revealed a significant gap between sustainability perception and practical actions. The manual management of energy relies heavily on human memory, creating an inertia phenomenon where energy waste is normalized. 

---

## Phase 2: Systems Design (Workshop 2)
### Key Design Decisions
Given strict institutional IT constraints (no administrator privileges, no centralized orchestrator servers), the design pivoted to a decentralized, **Software-Defined (User-Space)** architecture:
* **Autonomous Agents:** Python executables (`.exe`) running independently on each workstation.
* **Non-Invasive Actions:** Utilization of behavioral nudges (full-screen deterrents) and local OS Suspend states to prevent data loss.
* **Cloud Persistence:** Telemetry is sent to a cloud MySQL DBaaS and Telegram API.

---

## Phase 3: Robust Design & Project Management (Workshop 3)
### Overview
This phase elevates the conceptual design into a production-ready Proof of Concept (PoC). It introduces fault-tolerance mechanisms, comprehensive risk management (ISO 31000), software quality assurance (ISO/IEC 25010), and a detailed project execution plan to ensure safe implementation in a highly restrictive academic environment.

### Key Enhancements & Management
* **Fault-Tolerant Architecture:** Implementation of a local encrypted CSV persistence module (Fallback) to handle institutional firewall blocks and deferred synchronization.
* **Risk Mitigation (QA):** Strict CPU load validation (>20%) before any suspension sequence to ensure critical academic background tasks are not interrupted.
* **Operational Planning:** A structured 6-week schedule, explicit team roles definition, and a resource management plan.

### Deliverables
* [📄 Project Management and Enhanced Design Document (PDF)](./Workshop_3_Management/Workshop_3_Report.pdf)
* [💻 LaTeX Source Code](./Workshop_3_Management/Workshop_3_Report.tex)