from logging import DEBUG, INFO, FileHandler, Formatter, StreamHandler, getLogger

logger = getLogger()
logger.setLevel(DEBUG)

formatter = Formatter("%(asctime)s | %(filename)s | [%(levelname)s] - %(message)s")

file_handler = FileHandler("photoalbum.log")
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = StreamHandler()
console_handler.setLevel(INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
