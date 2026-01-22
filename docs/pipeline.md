# Content Automation Pipeline (v0)

## Stages
1. Ingest
2. Normalize
3. Script Generation
4. Storyboard / Scene Planning
5. Asset Generation / Selection
6. Voiceover
7. Video Assembly
8. Review
9. Approved / Published

## Core Artifacts
- ContentJob
- ScriptVersion
- Scene
- Asset
- ModelRun
- RenderRun

## Non-negotiables
- Every stage produces a stored artifact
- No regeneration without diff detection
- Dashboard reflects ground truth from artifacts
