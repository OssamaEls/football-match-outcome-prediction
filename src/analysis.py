from glob import glob
import os
from pathlib import Path

import pandas as pd


path = str(
        (
            Path(__file__).parent.parent / 'files/Football-Dataset'
        ).resolve()
    )

files = glob(f'{path}/**/*.csv')

df = pd.concat([
        pd.read_csv(file) for file in files
    ])

