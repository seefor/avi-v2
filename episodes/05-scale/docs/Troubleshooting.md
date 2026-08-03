# Episode 05 Troubleshooting — Scale

## Entire Batch Stops on One Failure

Check exception handling around each target. A per-device failure should be captured as a result rather than escape and cancel the whole batch.

## Results Arrive in Unexpected Order

Concurrent tasks may complete out of order. Use device identity in every result instead of relying on list position.

## Too Many Simultaneous Connections

Reduce the concurrency limit. Confirm the runner actually enforces the configured bound.

## Timeout Is Reported as Healthy

Treat timeouts as observation failures. A missing response is not evidence of healthy state.

## Rollup Count Is Wrong

Build rollups from explicit per-device statuses after all tasks settle. Do not infer health only from the absence of an exception.

## Evidence IDs Are Mixed Between Devices

Generate and attach evidence per tool event/target. Check shared mutable variables in concurrent code.

## Debugging Order

```text
1. Run each target individually
2. Confirm per-target result shape
3. Enable bounded concurrency
4. Force one failure
5. Verify isolation
6. Verify rollup counts and evidence links
```