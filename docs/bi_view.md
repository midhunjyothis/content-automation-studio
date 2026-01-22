# BI View: Creative Production Observability

## Core Questions the Dashboard Must Answer
- What is being produced right now?
- Where is work stuck or slowing down?
- What quality signals exist before publishing?
- What changed between versions?

## Primary Metrics
- Throughput: jobs completed per day/week
- Cycle time: ingest → approved
- Revision rate: scripts revised per job
- Render failure rate
- Average video duration vs target
- Words-per-second pacing

## Creative Analytics
- Script length timeline (seconds)
- Sentiment arc over time
- Concept density per scene
- Hook strength proxy (first 3 seconds)

## Drill-Down Hierarchy
KPI → ContentJob → ScriptVersion → Scene → Asset / ModelRun
