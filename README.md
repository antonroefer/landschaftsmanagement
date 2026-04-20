# Flood Damage Estimation

Geo411 course project repository for the practical assignment "09_Flood_Damage_Estimation: Multi-Event Comparison and Solution Labs for Infrastructure Siting".

This repository is currently a project scaffold. The Python modules in `src/` are placeholders, so the README focuses on the course task, expected workflow, and how to organize the project while the analysis is being developed.

## Course context

The module combines geoinformatics, remote sensing, and project work. For this assignment, the topic is flood damage estimation with a focus on comparing one or more flood events and translating the analysis into a compact planning workflow for resilient infrastructure siting.

Course material:

- [Course description](references/course-notes/Geo411_s2026_Kursbeschreibung.pdf)
- [Task sheet: Flood Damage Estimation](references/course-notes/09_Flood_Damage_Estimation_Multi_Event_Comparison_and_Solution_Labs_for_Infrastructure_Siting_Schultz.pdf)

## Assignment goal

The task goes beyond flood extent mapping. The goal is to assess where flood impacts recur, which exposed assets are affected, and where resilient siting or adaptation measures would be most suitable.

The expected outcomes are:

- An event-specific or comparative flood impact assessment based on open earth observation data.
- An exposure-based estimate of relative flood damage or affected assets.
- A suitability map for resilient infrastructure siting or adaptation measures.
- A transparent multi-criteria workflow with explicit assumptions and limitations.

## Project timeline (Summer Term 2026)

The project is organized into four phases and follows the detailed time plan below.

### Phase 1: Exploration, Methodology, and Planning (group task)

**1.1 Literature review and method benchmark**
- Scope: Build a method overview and select algorithms for Sentinel-1 and Sentinel-2 processing workflows.
- Start: April 13, 2026
- End: April 24, 2026 (18:00)

**1.2 Event research and data acquisition**
- Scope: Select two comparable flood events with a strong data basis.
- Start: April 13, 2026
- End: April 24, 2026 (18:00)

**1.3 Workflow specification and time planning**
- Scope: Define work packages and structure the project
- Start: April 20, 2026
- End: April 24, 2026 (18:00)
- Predecessor: 1.1

**Submission S1: Planning documents and review matrix**
- Date: April 24, 2026 (deadline)

**Milestone M1: Presentation of methodology and timeline**
- Date: April 27, 2026 (in class)

### Phase 2: Flood impact analysis (group task)

**2.1 Remote sensing: flood delineation**
- Scope: Process Sentinel-1 data and create flood extent masks.
- Start: April 28, 2026
- End: May 15, 2026
- Predecessor: M2
- Outcome: Event-specific comparative flood impact assessment.

**2.2 Asset overlay and exposure assessment**
- Scope: Overlay flood masks with buildings, transport infrastructure, and land use (OSM).
- Start: May 18, 2026
- End: June 5, 2026
- Predecessor: 2.1

**Submission S2: Webinar to present the project's approach**
- Date: May 22, 2026 (deadline)

**2.3 Hotspot identification and damage estimation**
- Scope: Identify repetitive hotspots and estimate affected assets.
- Start: June 8, 2026
- End: June 19, 2026
- Predecessor: 2.2
- Outcome: Exposure-based estimate of relative flood damage.

**Milestone M2: Data ready for flood impact assessment**
- Date: June 19, 2026

### Phase 3: Measures, suitability analysis, and visualization (group task)

**3.1 Multi-criteria suitability analysis (MCA)**
- Scope: Develop the model (hazard avoidance, elevation, accessibility).
- Start: June 22, 2026
- End: June 30, 2026
- Predecessor: 2.3

**3.2 Final visualization package (map package / WebGIS concept)**
- Scope: Cartographic preparation of project results.
- Start: June 25, 2026
- End: July 3, 2026 (12:00)
- Outcome: Suitability map for resilient infrastructure siting.

**3.3 Final results presentation (PPTX)**
- Scope: Summarize workflow, assumptions, and results.
- Start: June 29, 2026
- End: July 3, 2026 (12:00)

**Submission S3: Final presentation slides**
- Date: July 3, 2026 (12:00)

**Milestone M3: Presentation of project results**
- Date: July 6 / July 7, 2026

### Phase 4: Finalization and documentation (group task)

**4.1 Mini-paper drafting (methods and results)**
- Scope: Scientific write-up of the transparent workflow.
- Start: July 8, 2026
- End: July 17, 2026
- Predecessor: M4

**4.2 Mini-paper finalization (discussion and review)**
- Scope: Interpret results and assess limitations (maximum 10 pages).
- Start: July 18, 2026
- End: July 24, 2026 (18:00)

**Milestone M4: Final mini-paper submission (project close)**
- Date: July 24, 2026 (18:00)

## Key deliverables and milestone dates

- Planning documents and review matrix (M1): April 24, 2026 (18:00).
- In-class methodology and timeline presentation (M2): April 27, 2026.
- Event-specific comparative flood impact assessment: after task 2.1.
- Exposure-based relative damage estimate: after task 2.3.
- Suitability map for resilient infrastructure siting: after task 3.2.
- Final presentation slides (M3): July 3, 2026 (12:00).
- Final project presentation (M4): July 6 / July 7, 2026.
- Mini-paper submission (M5): July 24, 2026 (18:00).

## Repository structure

The structure below is aligned with both the practical flood-damage workflow and the required GEO 411 deliverables.

```
├── data
│   ├── external       <- Third-party input data
│   ├── interim        <- Intermediate processing results
│   ├── processed      <- Cleaned analysis-ready datasets
│   └── raw            <- Original source data
│
├── references        <- Course notes, manuals, and other source material
│   └── course-notes   <- Course documents used for this project
│
├── reports           <- Generated analysis outputs
│   ├── figures        <- Maps and figures for reports
│   ├── presentations  <- Slides for milestone and final presentations
│   ├── webinar        <- Webinar video, guide, and supporting assets
│   ├── mini-paper     <- Drafts and final mini-paper submission files
│   └── project-plan   <- Work packages, milestones, and Gantt artifacts
│
├── src               <- Python project code
│   ├── main.py       <- Entry point for the current Python scaffold
│   ├── classes
│   ├── helpers
│   └── test
│
└── requirements.txt  <- Python dependencies
```

## Working with the project

The repository keeps the Python scaffold intentionally small at the moment, so the recommended workflow is to organize the data and analysis products first, then extend `src/` only as new processing steps are needed.

- Put source data in `data/raw/`.
- Save cleaned or merged datasets in `data/processed/`.
- Keep intermediate transformation outputs in `data/interim/`.
- Store milestone and final presentation slides in `reports/presentations/`.
- Store webinar recordings and companion guidance in `reports/webinar/`.
- Keep mini-paper drafts and final exports in `reports/mini-paper/`.
- Keep work package descriptions and Gantt planning files in `reports/project-plan/`.
- Store figures and map exports in `reports/figures/`.
- Use `references/course-notes/` for the PDF source material and other course documents.

## Environment setup

This project uses Python 3.13.3. The environment is intentionally minimal at the moment. Install the listed dependencies and create a local `.env` file if you need configuration variables.

```bash
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

## Current code entry points

At the moment, the primary code entry point is:

- `src/main.py` as the current entry point.

Add new modules here only when they support the flood-damage workflow directly.

## Notes

The course task emphasizes a transparent, defensible workflow. Keep assumptions, limitations, and data sources documented alongside the analysis so they can be reused in the presentation and mini-paper.