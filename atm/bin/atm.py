import os
import sys
from atm.core import main

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

if __name__ == "__main__":
    main.run()
