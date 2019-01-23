"""
Run this in python 2 to read in the marshalled passband file and save it as a legacy pickle.
"""

import numpy as np
import os
import marshal
import pickle
import glob
import time
import libphoebe

for legacy_pb in glob.glob('*.pb'):
    print('processing %s.' % legacy_pb)
    # Read in the marshalled passband:
    with open(legacy_pb, 'rb') as f:
        struct = marshal.load(f)

    content = struct['content']
    atmlist = struct['atmlist']
    pbset = struct['pbset']
    pbname = struct['pbname']
    effwl = struct['effwl']
    calibrated = struct['calibrated']

    # these are new additions and not every pb file has them.
    opv = struct.get('originating_phoebe_version', 2.0)
    version = struct.get('version', 1.0)
    comments = struct.get('comments', 'Converted from the marshalled passband version.')
    reference = struct.get('reference', None)
    timestamp = struct.get('timestamp', time.ctime())

    ptf_table = struct['ptf_table']
    ptf_table['wl'] = np.fromstring(ptf_table['wl'], dtype='float64')
    ptf_table['fl'] = np.fromstring(ptf_table['fl'], dtype='float64')
    wl = np.fromstring(struct['ptf_wl'], dtype='float64')
    ptf_area = struct['ptf_area']
    ptf_photon_area = struct['ptf_photon_area']

    ptf_func = list(struct['ptf_func'])
    ptf_func[0] = np.fromstring(ptf_func[0])
    ptf_func[1] = np.fromstring(ptf_func[1])
    ptf_func = tuple(ptf_func)
    ptf = lambda wl: interpolate.splev(wl, ptf_func)

    ptf_photon_func = list(struct['ptf_photon_func'])
    ptf_photon_func[0] = np.fromstring(ptf_photon_func[0])
    ptf_photon_func[1] = np.fromstring(ptf_photon_func[1])
    ptf_photon_func = tuple(ptf_photon_func)
    ptf_photon = lambda wl: interpolate.splev(wl, ptf_photon_func)

    if 'blackbody' in content:
        _bb_func_energy = list(struct['_bb_func_energy'])
        _bb_func_energy[0] = np.fromstring(_bb_func_energy[0])
        _bb_func_energy[1] = np.fromstring(_bb_func_energy[1])
        _bb_func_energy = tuple(_bb_func_energy)
        _log10_Inorm_bb_energy = lambda Teff: interpolate.splev(Teff, _bb_func_energy)

        _bb_func_photon = list(struct['_bb_func_photon'])
        _bb_func_photon[0] = np.fromstring(_bb_func_photon[0])
        _bb_func_photon[1] = np.fromstring(_bb_func_photon[1])
        _bb_func_photon = tuple(_bb_func_photon)
        _log10_Inorm_bb_photon = lambda Teff: interpolate.splev(Teff, _bb_func_photon)

    if 'extern_atmx' in content and 'extern_planckint' in content:
        planck = ('/usr/local/share/phoebe/wd/atmcofplanck.dat').encode('utf8')
        atm = ('/usr/local/share/phoebe/wd/atmcof.dat').encode('utf8')
        wd_data = libphoebe.wd_readdata(planck, atm)
        extern_wd_idx = struct['extern_wd_idx']

    if 'ck2004' in content:
        # CASTELLI & KURUCZ (2004):
        # Axes needs to be a tuple of np.arrays, and grid a np.array:
        _ck2004_axes  = tuple(map(lambda x: np.fromstring(x, dtype='float64'), struct['_ck2004_axes']))
        _ck2004_energy_grid = np.fromstring(struct['_ck2004_energy_grid'], dtype='float64')
        _ck2004_energy_grid = _ck2004_energy_grid.reshape(len(_ck2004_axes[0]), len(_ck2004_axes[1]), len(_ck2004_axes[2]), 1)
        _ck2004_photon_grid = np.fromstring(struct['_ck2004_photon_grid'], dtype='float64')
        _ck2004_photon_grid = _ck2004_photon_grid.reshape(len(_ck2004_axes[0]), len(_ck2004_axes[1]), len(_ck2004_axes[2]), 1)

    if 'ck2004_all' in content:
        # CASTELLI & KURUCZ (2004) all intensities:
        # Axes needs to be a tuple of np.arrays, and grid a np.array:
        _ck2004_intensity_axes  = tuple(map(lambda x: np.fromstring(x, dtype='float64'), struct['_ck2004_intensity_axes']))
        _ck2004_Imu_energy_grid = np.fromstring(struct['_ck2004_Imu_energy_grid'], dtype='float64')
        _ck2004_Imu_energy_grid = _ck2004_Imu_energy_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), len(_ck2004_intensity_axes[3]), 1)
        _ck2004_Imu_photon_grid = np.fromstring(struct['_ck2004_Imu_photon_grid'], dtype='float64')
        _ck2004_Imu_photon_grid = _ck2004_Imu_photon_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), len(_ck2004_intensity_axes[3]), 1)
        _ck2004_boosting_energy_grid = np.fromstring(struct['_ck2004_boosting_energy_grid'], dtype='float64')
        _ck2004_boosting_energy_grid = _ck2004_boosting_energy_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), len(_ck2004_intensity_axes[3]), 1)
        _ck2004_boosting_photon_grid = np.fromstring(struct['_ck2004_boosting_photon_grid'], dtype='float64')
        _ck2004_boosting_photon_grid = _ck2004_boosting_photon_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), len(_ck2004_intensity_axes[3]), 1)

    if 'ck2004_ld' in content:
        _ck2004_ld_energy_grid = np.fromstring(struct['_ck2004_ld_energy_grid'], dtype='float64')
        _ck2004_ld_energy_grid = _ck2004_ld_energy_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), 11)
        _ck2004_ld_photon_grid = np.fromstring(struct['_ck2004_ld_photon_grid'], dtype='float64')
        _ck2004_ld_photon_grid = _ck2004_ld_photon_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), 11)

    if 'ck2004_ldint' in content:
        _ck2004_ldint_energy_grid = np.fromstring(struct['_ck2004_ldint_energy_grid'], dtype='float64')
        _ck2004_ldint_energy_grid = _ck2004_ldint_energy_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), 1)
        _ck2004_ldint_photon_grid = np.fromstring(struct['_ck2004_ldint_photon_grid'], dtype='float64')
        _ck2004_ldint_photon_grid = _ck2004_ldint_photon_grid.reshape(len(_ck2004_intensity_axes[0]), len(_ck2004_intensity_axes[1]), len(_ck2004_intensity_axes[2]), 1)


    ################################################# PACK BACK INTO THE DICTIONARY #######################################################

    struct = dict()

    struct['originating_phoebe_version'] = opv

    struct['content']         = content
    struct['atmlist']         = atmlist
    struct['pbset']           = pbset
    struct['pbname']          = pbname
    struct['effwl']           = effwl
    struct['calibrated']      = calibrated
    struct['version']         = version
    struct['comments']        = comments
    struct['reference']       = reference
    struct['ptf_table']       = ptf_table
    struct['ptf_wl']          = wl
    struct['ptf_func']        = ptf_func
    struct['ptf_area']        = ptf_area
    struct['ptf_photon_func'] = ptf_photon_func
    struct['ptf_photon_area'] = ptf_photon_area
    if 'blackbody' in content:
        struct['_bb_func_energy'] = _bb_func_energy
        struct['_bb_func_photon'] = _bb_func_photon
    if 'ck2004' in content:
        struct['_ck2004_axes'] = _ck2004_axes
        struct['_ck2004_energy_grid'] = _ck2004_energy_grid
        struct['_ck2004_photon_grid'] = _ck2004_photon_grid
    if 'ck2004_all' in content:
        struct['_ck2004_intensity_axes'] = _ck2004_intensity_axes
        struct['_ck2004_Imu_energy_grid'] = _ck2004_Imu_energy_grid
        struct['_ck2004_Imu_photon_grid'] = _ck2004_Imu_photon_grid
        struct['_ck2004_boosting_energy_grid'] = _ck2004_boosting_energy_grid
        struct['_ck2004_boosting_photon_grid'] = _ck2004_boosting_photon_grid
    if 'ck2004_ld' in content:
        struct['_ck2004_ld_energy_grid'] = _ck2004_ld_energy_grid
        struct['_ck2004_ld_photon_grid'] = _ck2004_ld_photon_grid
    if 'ck2004_ldint' in content:
        struct['_ck2004_ldint_energy_grid'] = _ck2004_ldint_energy_grid
        struct['_ck2004_ldint_photon_grid'] = _ck2004_ldint_photon_grid
    if 'extern_planckint' in content and 'extern_atmx' in content:
        struct['extern_wd_idx'] = extern_wd_idx

    # Finally, timestamp the file:
    struct['timestamp'] = timestamp

    # Save as a protocol-1 pickle:
    with open(legacy_pb+'.pkl2', 'wb') as f:
        pickle.dump(struct, f)
