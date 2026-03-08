import logging

# Configure the logger
logger = logging.getLogger("ai_code_explainer")
logger.setLevel(logging.INFO)

# Console handler with formatting
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)