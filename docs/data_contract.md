# Data Contract (v0)

## ContentJob
- id
- input_type
- target_platform
- target_duration_sec
- status
- created_at

## ScriptVersion
- job_id
- version
- word_count
- estimated_duration_sec
- sentiment_series
- approved

## Scene
- job_id
- scene_index
- scene_type
- duration_sec
- concept_tags

## Asset
- asset_id
- asset_type
- source
- prompt_hash
- fingerprint

## ModelRun
- model_name
- artifact_type
- start_time
- end_time
- success
- latency_ms
