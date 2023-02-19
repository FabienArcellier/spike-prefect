import os

import alfred

ROOT_DIR = os.path.realpath(os.path.join(__file__, "..", ".."))


@alfred.command("docker:build", help="workflow to build docker container")
def docker_build():
    """
    construit l'image docker pour l'application

    >>> $ alfred docker:build
    """
    docker = alfred.sh("docker", "docker should be present")
    os.chdir(ROOT_DIR)
    alfred.run(docker, ['build', '.'])
