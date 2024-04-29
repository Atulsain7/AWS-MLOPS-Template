import os
import sys
import hydra
from omegaconf import DictConfig

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

sys.path.append(project_root)
from src.processes.setup_process import setup_general_process


@hydra.main(config_path="../../configs", config_name="config", version_base=None)
def main(cfg: DictConfig) -> None:
    processes = setup_general_process(cfg)
    processes.initialize_project()


if __name__ == "__main__":
    main()
