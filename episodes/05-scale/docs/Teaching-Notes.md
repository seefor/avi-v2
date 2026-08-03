# Episode 05 Teaching Notes — Scale

## Scale Changes Failure Semantics

With one device, a timeout often ends the demo. With many devices, failure becomes partial. The application must preserve completed observations while clearly identifying failed or unreachable targets.

## Why Bounded Concurrency

Unbounded parallelism can overwhelm:
- jump hosts,
- lab devices,
- AAA systems,
- API limits,
- local CPU/file descriptors.

A concurrency limit is both a reliability control and a safety control.

## Inventory Is a Scope Boundary

Target selection should come from an approved inventory. This prevents the model from expanding scope simply by naming additional devices.

## Rollups Need Drill-Down

A summary such as "2 of 3 healthy" is useful only if an engineer can inspect the evidence/state behind each device. Aggregation should never destroy provenance.

## Partial Success

Use explicit categories such as:
- completed/healthy,
- completed/degraded,
- failed,
- unreachable,
- timed out.

Do not convert "no observation" into a health result.

## Key Takeaway

Scaling observation should increase coverage without reducing traceability or widening permissions.