# Copyright 2014 Diamond Light Source Ltd.
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

"""
.. module:: tomo_recon
   :platform: Unix
   :synopsis: runner for tests using the MPI framework

.. moduleauthor:: Mark Basham <scientificsoftware@diamond.ac.uk>

"""

import unittest
import tempfile
from savu.test import test_utils as tu

from savu.test.plugin_runner_test import run_protected_plugin_runner
from savu.test.plugin_runner_test \
    import run_protected_plugin_runner_no_process_list


class TestDataReduction(unittest.TestCase):

    def test_mm(self):
        options = {
            "transport": "hdf5",
            "process_names": "CPU0",
            "data_file": tu.get_test_data_path('mm.nxs'),
            "process_file": tu.get_test_process_path(
                'multiple_mm_inputs_test.nxs'),
            "out_path": tempfile.mkdtemp()
            }
        run_protected_plugin_runner(options)

    def test_tomo1(self):
        options = tu.set_experiment('tomo')
        plugin = 'savu.plugins.test_plugin'
        loader_dict = {}
        data_dict = {'in_datasets': ['tomo', 'tomo'], 'out_datasets': ['test']}
        saver_dict = {}
        all_dicts = [loader_dict, data_dict, saver_dict]
        run_protected_plugin_runner_no_process_list(options, plugin,
                                                    data=all_dicts)

    def test_tomo2(self):
        options = tu.set_experiment('tomo')
        plugin = 'savu.plugins.test_plugin'
        loader_dict = {'starts': [10, 10, 10],
                       'stops': [-1, -1, -1],
                       'steps': [1, 1, 1]}
        data_dict = {'in_datasets': ['tomo', 'tomo'], 'out_datasets': ['test']}
        saver_dict = {}
        all_dicts = [loader_dict, data_dict, saver_dict]
        run_protected_plugin_runner_no_process_list(options, plugin,
                                                    data=all_dicts)

    def test_tomo3(self):
        options = tu.set_experiment('tomo')
        plugin = 'savu.plugins.test_plugin'
        loader_dict = {'starts': [10, 10, 10],
                       'stops': [-1, -1, -1],
                       'steps': [10, 10, 10]}
        data_dict = {'in_datasets': ['tomo', 'tomo'], 'out_datasets': ['test']}
        saver_dict = {}
        all_dicts = [loader_dict, data_dict, saver_dict]
        run_protected_plugin_runner_no_process_list(options, plugin,
                                                    data=all_dicts)

    def test_tomo4(self):
        options = tu.set_experiment('tomo')
        plugin = 'savu.plugins.test_plugin'
        loader_dict = {'starts': [10, 10, 10],
                       'stops': [-10, -10, -10],
                       'steps': [10, 10, 10]}
        data_dict = {'in_datasets': ['tomo', 'tomo'], 'out_datasets': ['test']}
        saver_dict = {}
        all_dicts = [loader_dict, data_dict, saver_dict]
        run_protected_plugin_runner_no_process_list(options, plugin,
                                                    data=all_dicts)

if __name__ == "__main__":
    unittest.main()
