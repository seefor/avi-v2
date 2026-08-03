# Episode 14 Troubleshooting — Change Planning

## Plan Validates Without Rollback

Make rollback presence a required validation rule for action classes that modify state.

## Approval Reference Does Not Match

Resolve the approval packet/record and compare target/action scope. Do not accept a generic approval ID without checking what it authorized.

## Proposed Command Is Outside Allowed Class

Reject the plan. Do not automatically expand the allowed action class to accommodate generated output.

## Precheck Is Vague

Convert prose such as "make sure the device is healthy" into observable checks with explicit pass/fail criteria.

## Postcheck Cannot Prove Success

Tie postchecks to the expected diff. The check should verify the state the plan claims it will produce.

## Rollback Is Not the Inverse

Review whether rollback actually restores the pre-change state. Prefer using the pre-change snapshot when appropriate.

## Debugging Order

```text
1. Validate target/action class
2. Resolve evidence + approval
3. Inspect proposed delta
4. Run plan schema validation
5. Check prechecks
6. Check postchecks
7. Check rollback
8. Confirm execution_allowed is false
```