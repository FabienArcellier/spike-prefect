import os.path
from typing import Tuple, List

from prefect import Flow
from prefect.deployments import Deployment

from app.main import my_favorite_function

deployments: List[Tuple[Flow, str]] = [
    (my_favorite_function, "main.my_favorite_function")
]

if __name__ == "__main__":
    for deploy in deployments:
        deployment = Deployment.build_from_flow(
            flow=deploy[0],
            name=deploy[1],
            path='/app/src/app/'
        )
        deployment.apply()
