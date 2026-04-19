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

## Suggested workflow

1. Select one flood event or two comparable events.
2. Derive flood extent or flood-damage proxies with Sentinel-1.
3. Optionally support the analysis with Sentinel-2 or other open raster layers.
4. Overlay the hazard footprint with exposed assets such as buildings, transport lines, land use, or other relevant layers.
5. Identify repeatedly exposed areas and estimate relative damage or affected assets.
6. Build a compact suitability analysis for resilient siting based on hazard avoidance, elevation, accessibility, land cover, and practical constraints.
7. Present the results as a map package or a lightweight WebGIS concept.

## Deliverables for the module

The course description asks for several outputs in addition to the practical analysis:

- A literature review matrix that justifies the method choice.
- A work package description with milestones and a Gantt chart.
- A short webinar or teaching unit for fellow students.
- A presentation of the results.
- A mini-paper of up to 10 pages.

If you are using this repository for the 09_Flood_Damage_Estimation task, the practical analysis should feed those deliverables directly.

## Repository structure

```
├── data
│   ├── external       <- Third-party input data
│   ├── interim        <- Intermediate processing results
│   ├── processed      <- Cleaned analysis-ready datasets
│   └── raw            <- Original source data
│
├── references        <- Course notes, manuals, and other source material
│   └── course-notes   <- PDFs used for this project
│
├── reports           <- Generated analysis outputs
│   └── figures       <- Maps and figures for reports
│
├── src               <- Python project code
│   ├── __init__.py
│   └── main.py       <- Entry point for the current Python scaffold
│
└── requirements.txt  <- Python dependencies
```

## Working with the project

The repository keeps the Python scaffold intentionally small at the moment, so the recommended workflow is to organize the data and analysis products first, then extend `src/` only as new processing steps are needed.

- Put source data in `data/raw/`.
- Save cleaned or merged datasets in `data/processed/`.
- Keep intermediate transformation outputs in `data/interim/`.
- Store figures and report exports in `reports/`.
- Use `references/course-notes/` for the PDF source material and other course documents.

## Environment setup

The environment is intentionally minimal at the moment. Install the listed dependencies and create a local `.env` file if you need configuration variables.

```bash
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

## Current code entry points

At the moment, the Python package only contains a minimal scaffold:

- `src/main.py` as the current entry point.
- `src/__init__.py` to keep the package importable.

Add new modules here only when they support the flood-damage workflow directly.

## Notes

The course task emphasizes a transparent, defensible workflow. Keep assumptions, limitations, and data sources documented alongside the analysis so they can be reused in the presentation and mini-paper.