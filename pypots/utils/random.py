"""
Transformer model for time-series imputation.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3

import numpy as np
import torch
from pypots.utils.logging import logger

RANDOM_SEED = 2204


def set_random_seed(random_seed: int = RANDOM_SEED):
    """Manually set the random state to make PyPOTS output reproducible results.

    Parameters
    ----------
    random_seed : int, default = RANDOM_SEED,
        The seed to be set for generating random numbers in PyPOTS.

    """

    np.random.seed(RANDOM_SEED)
    torch.manual_seed(random_seed)
    logger.info(
        f"Done. Have already set the random seed as {random_seed} for numpy and pytorch."
    )
