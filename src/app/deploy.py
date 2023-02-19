import os.path
import time
from typing import List

from prefect import Flow
from prefect.deployments import Deployment


def deploy(flows: List[Flow]):
    root_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')
    deployments_logs = []
    for flow in flows:
        deployment = Deployment.build_from_flow(
            flow=flow,
            name="deploy",
            path=root_dir,
        )
        deployment_id = deployment.apply()
        deployments_logs.append(f"{flow.name}: {deployment_id}")

    print(flows)


if __name__ == "__main__":
    from app import flows
    time.sleep(5)
    logs = deploy(flows)
