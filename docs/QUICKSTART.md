# AVI v2 Quick Start

## Clone and install

```bash
git clone https://github.com/seefor/avi-v2.git
cd avi-v2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
git clone https://github.com/seefor/avi-v2.git
cd avi-v2
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Episode 01 — real lab observation

Episode 01 is the only starter that expects a pyATS testbed immediately.

```bash
cd episodes/01-tools
cp testbed.example.yaml testbed.yaml
# Edit testbed.yaml with your lab credentials.
python avi_pilot_01_tools.py
```

Do not commit `testbed.yaml`.

## Episode starters

From the repository root:

```bash
python episodes/02-evidence/avi_pilot_02_evidence.py
python episodes/03-state/avi_pilot_03_state.py
python episodes/04-structure/avi_pilot_04_structure.py
python episodes/05-scale/avi_pilot_05_scale.py
python episodes/06-context/avi_pilot_06_context.py
python episodes/07-intent/avi_pilot_07_intent.py
```

Episode 08 uses a small local knowledge folder, so run it from its episode directory:

```bash
cd episodes/08-rag
python avi_pilot_08_rag.py
cd ../..
```

Continue:

```bash
python episodes/09-harness/avi_pilot_09_harness.py
python episodes/10-loops/avi_pilot_10_loops.py
python episodes/11-verification/avi_pilot_11_verification.py
```

## Episode 12 — MCP

```bash
cd episodes/12-mcp
python mcp_server.py
```

Use an MCP-capable client or inspector to discover `device_status` and `bgp_status`. The starter intentionally exposes demo data for approved lab device names only.

## Episodes 13–15

```bash
python episodes/13-human-approval/avi_pilot_13_approval.py
python episodes/14-change-planning/avi_pilot_14_change_plan.py
python episodes/15-controlled-action/avi_pilot_15_controlled_action.py
```

Episode 15 uses an in-memory lab state by default. That is intentional. Do not replace it with a live write backend until the approval, plan, preflight, postcheck, evidence, and rollback controls have been reviewed for your lab.

## Teaching material

Every episode includes a camera-ready walkthrough under:

```text
episodes/NN-name/docs/episode-NN-walkthrough.md
```

Use the episode README for the technical scope and safety boundary, and the walkthrough while preparing or recording the matching YouTube video.
