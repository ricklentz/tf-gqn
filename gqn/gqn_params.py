"""
Contains (hyper-)parameters of the GQN implementation.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

_DEFAULTS = {
    # constants
    'IMG_HEIGHT' : 64,
    'IMG_WIDTH' : 64,
    'IMG_CHANNELS' : 3,
    'POSE_CHANNELS' : 7,
    # batch parameters
    'BATCH_SIZE' : 1,
    'CONTEXT_SIZE' : 5,
    # hyper-parameters: scene representation
    'ENC_HEIGHT' : 16,
    'ENC_WIDTH' : 16,
    'ENC_CHANNELS' : 256,
    # hyper-parameters: generator LSTM
    'LSTM_OUTPUT_CHANNELS' : 256,
    'LSTM_CANVAS_CHANNELS' : 256,
    'LSTM_KERNEL_SIZE' : 5,
    'Z_CHANNELS' : 64, # latent space size per image generation step
    'GENERATOR_INPUT_CHANNELS' : 327, # pose + representation + z
    'INFERENCE_INPUT_CHANNELS' : 263, # pose + representation
    'SEQ_LENGTH' : 12, # number of steps in image generation sequence
}

_GQNParams = collections.namedtuple(
    typename='GQNParams',
    field_names=list(_DEFAULTS.keys())
    )
PARAMS = _GQNParams(**_DEFAULTS)
