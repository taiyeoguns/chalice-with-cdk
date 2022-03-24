from pathlib import Path

from aws_cdk import core as cdk
from chalice.cdk import Chalice


RUNTIME_SOURCE_DIR = Path(__file__).parents[2] / "runtime"


class ChaliceApp(cdk.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.chalice = Chalice(
            self,
            "ChaliceApp",
            source_dir=RUNTIME_SOURCE_DIR,
            stage_config={"environment_variables": {"APP_TABLE_NAME": ""}},
        )
