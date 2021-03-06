# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""TensorFlow Probability experimental NUTS package."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.python.experimental.mcmc.elliptical_slice_sampler import EllipticalSliceSampler
from tensorflow_probability.python.experimental.mcmc.nuts import NoUTurnSampler
from tensorflow_probability.python.experimental.mcmc.particle_filter import particle_filter
from tensorflow_probability.python.experimental.mcmc.particle_filter import reconstruct_trajectories
from tensorflow_probability.python.experimental.mcmc.sample_sequential_monte_carlo import default_make_hmc_kernel_fn
from tensorflow_probability.python.experimental.mcmc.sample_sequential_monte_carlo import gen_make_hmc_kernel_fn
from tensorflow_probability.python.experimental.mcmc.sample_sequential_monte_carlo import gen_make_transform_hmc_kernel_fn
from tensorflow_probability.python.experimental.mcmc.sample_sequential_monte_carlo import make_rwmh_kernel_fn
from tensorflow_probability.python.experimental.mcmc.sample_sequential_monte_carlo import sample_sequential_monte_carlo
from tensorflow_probability.python.experimental.mcmc.sample_sequential_monte_carlo import simple_heuristic_tuning
from tensorflow.python.util.all_util import remove_undocumented  # pylint: disable=g-direct-tensorflow-import

_allowed_symbols = [
    'EllipticalSliceSampler',
    'NoUTurnSampler',
    'particle_filter',
    'reconstruct_trajectories',
    'default_make_hmc_kernel_fn',
    'gen_make_hmc_kernel_fn',
    'gen_make_transform_hmc_kernel_fn',
    'make_rwmh_kernel_fn',
    'sample_sequential_monte_carlo',
    'simple_heuristic_tuning',
]

remove_undocumented(__name__, _allowed_symbols)
