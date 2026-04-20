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

## Suggested workflow (Project Phases)

To align this project with the official GEO 411 timeline (Summer Term 2026), the work is structured into five phases that match the required submissions and presentation dates.

**Phase 1: Literature Review and Project Planning (April 13 - April 27)**
- Review project management requirements and define the analysis scope.
- Build a literature review matrix to justify method selection.
- Draft the work package description with milestones and a Gantt chart.
- Submission deadline: April 24, 18:00 (presentation slides, review matrix, and Gantt chart).
- In-class presentation: April 27, 12:00 - 16:00 (10 min talk + 5 min discussion).

**Phase 2: Data Preparation, Event Selection, and Webinar Production (April 28 - May 22)**
- Select flood events and collect relevant EO and ancillary datasets.
- Perform preprocessing and initial flood/exposure mapping.
- Prepare the teaching webinar and short practical guide.
- Webinar deadline: May 22, 18:00.

**Phase 3: Core Analysis and Suitability Modelling (May 23 - June 29)**
- Continue exposure and relative damage estimation across event(s).
- Develop and refine the multi-criteria suitability workflow for resilient siting.
- Integrate peer-learning inputs and webinar feedback (feedback session: June 8).
- Consolidate intermediate outputs into map-ready and report-ready results.
- Note: May 25 is a public holiday (Pfingstmontag).

**Phase 4: Results Presentation (June 30 - July 7)**
- Finalize figures, maps, and conference-style result narrative.
- Prepare the final presentation (20 min talk + 15 min discussion).
- PPT submission deadline: Friday before presentation at 12:00 (expected July 3).
- Final presentations: July 6 and July 7.

**Phase 5: Mini-Paper Finalization (July 8 - July 24)**
- Write and polish the mini-paper (max. 10 pages, excluding table of contents and references).
- Ensure consistency between methods, results, discussion, and conclusions.
- Final submission deadline: July 24, 18:00.

## Deliverables for the module

The course description asks for several outputs in addition to the practical analysis:

- Literature review matrix plus short presentation (presented April 27; files due April 24, 18:00).
- Work package description including milestones and Gantt chart (submitted with the April 24 package; presented April 27).
- Webinar (about 20 minutes) plus short guide (due May 22, 18:00).
- Final results presentation in conference format (July 6/7; slides due Friday before at 12:00).
- Mini-paper (max. 10 pages) due July 24, 18:00.

If you are using this repository for the 09_Flood_Damage_Estimation task, the practical analysis should feed those deliverables directly.

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