from logging import getLogger
from pathlib import Path

logger = getLogger(__name__)


class Files:
    """
    Simple object to mange the creation of directories and files.
    """

    @classmethod
    def create_directory(cls, directory_path: str) -> bool:
        """
        Create a directory if it does not exist.
        """
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        if Path(directory_path).exists():
            logger.info("Directory %s created successfully", directory_path)
            return True
        else:
            logger.error("Directory %s could not be created", directory_path)
