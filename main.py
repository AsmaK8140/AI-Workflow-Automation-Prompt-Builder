from src.project3.workflow_builder import build_workflow
from pathlib import Path
import json
def run():
    sample = "Send a weekly sales report email to the manager."
    w = build_workflow(sample)
    out = Path("outputs") / "workflow.json"
    out.write_text(json.dumps(w, indent=2))
    print("Workflow written to outputs/workflow.json")
if __name__ == '__main__':
    run()
