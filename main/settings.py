from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'


SOURCES_LIST = [IMAGE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'sample.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'sample_detected.jpg'


# ML Model config
CLASS_SIZE = 'class9' # [option] select class folder among class1 class9,class392
MODEL_DIR = ROOT  /'weights' / CLASS_SIZE
DETECTION_MODEL = MODEL_DIR / 'best.pt'
# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'