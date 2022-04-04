import phoebe
from astropy import units as u

ptfs = [
#    PTF FILE               PB SET          NAME  EFFWL  UNITS WDIDX REFERENCE                              COMMENT(S)
    # ('stromgren_u.ptf',    'Stromgren',      'u',  3500., u.AA,  1,   'Maiz Apellaniz (2006), AJ 131, 1184', ''),
    # ('stromgren_v.ptf',    'Stromgren',      'v',  4110., u.AA,  2,   'Maiz Apellaniz (2006), AJ 131, 1184', ''),
    # ('stromgren_b.ptf',    'Stromgren',      'b',  4670., u.AA,  3,   'Maiz Apellaniz (2006), AJ 131, 1184', ''),
    # ('stromgren_y.ptf',    'Stromgren',      'y',  5470., u.AA,  4,   'Maiz Apellaniz (2006), AJ 131, 1184', ''),
    # ('johnson_u.ptf',      'Johnson',        'U',  3600., u.AA,  5,   'Maiz Apellaniz (2006), AJ 131, 1184', 'This passband is also a part of the Bessel series.'),
    # ('johnson_b.ptf',      'Johnson',        'B',  4400., u.AA,  6,   'Maiz Apellaniz (2006), AJ 131, 1184', 'This passband is also a part of the Bessel series.'),
    # ('johnson_v.ptf',      'Johnson',        'V',  5500., u.AA,  7,   'Maiz Apellaniz (2006), AJ 131, 1184', 'This passband is also a part of the Bessel series.'),
    # ('cousins_r.ptf',      'Cousins',        'R',  6470., u.AA, 15,   'Cousins, A. W. J. (1976), MNRAS 81, 25', 'This passband is also a part of the Bessel series.'),
    # ('cousins_i.ptf',      'Cousins',        'I',  7865., u.AA, 16,   'Cousins, A. W. J. (1976), MNRAS 81, 25', 'This passband is also a part of the Bessel series.'),
    # ('tycho_bt.ptf',       'Tycho',          'B',  4190., u.AA, 23,   'Hipparcos and Tycho catalogs, ESA pub. SP-1200, Vol. 1, pg. 39', 'Table taken from ADPS http://ulisse.pd.astro.it/Astro/ADPS/Systems/index.html'),
    # ('tycho_vt.ptf',       'Tycho',          'V',  5230., u.AA, 24,   'Hipparcos and Tycho catalogs, ESA pub. SP-1200, Vol. 1, pg. 39', 'Table taken from ADPS http://ulisse.pd.astro.it/Astro/ADPS/Systems/index.html'),
    # ('hipparcos.ptf',      'Hipparcos',     'Hp',  5045., u.AA, 25,   'Hipparcos and Tycho catalogs, ESA pub. SP-1200, Vol. 1, pg. 39', 'Table taken from ADPS http://ulisse.pd.astro.it/Astro/ADPS/Systems/index.html'),
    # ('kepler_mean.ptf',    'Kepler',      'mean',  5920., u.AA, -1,   'Doug Caldwell, priv.comm.', 'Computed by averaging out 42 per-channel transmission functions provided by Doug Caldwell.'),
    # ('tess.ptf',           'TESS',           'T',  7972., u.AA, -1,   'http://svo2.cab.inta-csic.es/theory/fps3/index.php?id=TESS/TESS.Red&&mode=browse&gname=TESS&gname2=TESS', ''),
    # ('brite_blue.ptf',     'BRITE',       'blue',  4275., u.AA, -1,   'Weiss et al. (2014), PASP 126, 573', ''),
    # ('brite_red.ptf',      'BRITE',        'red',  6235., u.AA, -1,   'Weiss et al. (2014), PASP 126, 573', ''),
    # ('gaia_G.ptf',         'Gaia',           'G',   575., u.nm, -1,   'http://www.cosmos.esa.int/web/gaia/transmissionwithoriginal', ''),
    # ('gaia_BP.ptf',        'Gaia',          'BP',   510., u.nm, -1,   'http://www.cosmos.esa.int/web/gaia/transmissionwithoriginal', ''),
    # ('gaia_RP.ptf',        'Gaia',          'RP',   750., u.nm, -1,   'http://www.cosmos.esa.int/web/gaia/transmissionwithoriginal', ''),
    # ('gaia_RVS.ptf',       'Gaia',         'RVS',   860., u.nm, -1,   'http://www.cosmos.esa.int/web/gaia/transmissionwithoriginal', ''),
    # ('kelt.ptf',           'KELT',           'R',  6260., u.AA, -1,   'Rob Siverd by way of Phill Read, private communication, 2018-06-22', 'This PTF includes filter response and the atmosphere'),
    # ('spitzer_b1.ptf',     'Spitzer',    '3.6um', 36000., u.AA, -1,   'https://irsa.ipac.caltech.edu/data/SPITZER/docs/irac/calibrationfiles/spectralresponse/', ''),
    # ('spitzer_b2.ptf',     'Spitzer',    '4.5um', 45000., u.AA, -1,   'https://irsa.ipac.caltech.edu/data/SPITZER/docs/irac/calibrationfiles/spectralresponse/', ''),
    # ('spitzer_b3.ptf',     'Spitzer',    '5.8um', 58000., u.AA, -1,   'https://irsa.ipac.caltech.edu/data/SPITZER/docs/irac/calibrationfiles/spectralresponse/', ''),
    # ('spitzer_b4.ptf',     'Spitzer',    '8.0um', 80000., u.AA, -1,   'https://irsa.ipac.caltech.edu/data/SPITZER/docs/irac/calibrationfiles/spectralresponse/', ''),
    # ('smei.ptf',           'SMEI',       'white',   700., u.nm, -1,   'Andrzej Pigulski by way of Petr Harmanec, priv. comm. on 2019-07-20', 'Solar Mass Ejection Imager (SMEI) aboard the Coriolis satellite'),
    # ('stereo_hi1a.ptf',    'STEREO', 'HI1A-noQE',   678., u.nm, -1,   'Danielle Bewsher by way of Petr Harmanec, private communication, 2018-11-02', 'This passband includes filter response without the quantum efficiency of the detector.'),
    # ('stereo_hi1a_qe.ptf', 'STEREO',   'HI1A-QE',   678., u.nm, -1,   'Danielle Bewsher by way of Petr Harmanec, private communication, 2018-11-02', 'This passband includes filter response with the quantum efficiency of the detector.'),
    # ('stereo_hi1b.ptf',    'STEREO', 'HI1B-noQE',   678., u.nm, -1,   'Danielle Bewsher by way of Petr Harmanec, private communication, 2018-11-02', 'This passband includes filter response without the quantum efficiency of the detector.'),
    # ('stereo_hi1b_qe.ptf', 'STEREO',   'HI1B-QE',   678., u.nm, -1,   'Danielle Bewsher by way of Petr Harmanec, private communication, 2018-11-02', 'This passband includes filter response with the quantum efficiency of the detector.'),
]

for ptf in ptfs:
    pb = phoebe.atmospheres.passbands.Passband(
        ptf='./'+ptf[0],
        pbset=ptf[1],
        pbname=ptf[2],
        effwl=ptf[3],
        wlunits=ptf[4],
        calibrated=True,
        reference=ptf[6],
        version=1.1,
        comments=ptf[7]
    )

    pb.compute_blackbody_response()
    pb.compute_bb_reddening(verbose=True)

    pb.compute_ck2004_response(path='tables/ck2004', verbose=True)
    pb.compute_ck2004_intensities(path='tables/ck2004', verbose=True)
    pb.compute_ck2004_reddening(path='tables/ck2004', verbose=True)

    print('Imputing ck2004 Inorm grids for %s...' % (ptf[0]))
    pb.impute_atmosphere_grid(pb._ck2004_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_photon_grid)
    for i in range(len(pb._ck2004_intensity_axes[3])):
        print('Imputing ck2004 Imu grid for %s, i=%d...' % (ptf[0], i))
        pb.impute_atmosphere_grid(pb._ck2004_Imu_energy_grid[:,:,:,i,:])
        pb.impute_atmosphere_grid(pb._ck2004_Imu_photon_grid[:,:,:,i,:])
    for i in range(len(pb._ck2004_extinct_axes[3])):
        for j in range(len(pb._ck2004_extinct_axes[4])):
            print('Imputing ck2004 Iext grid for %s, i=%d, j=%d...' % (ptf[0], i, j))
            pb.impute_atmosphere_grid(pb._ck2004_extinct_energy_grid[:,:,:,i,j,:])
            pb.impute_atmosphere_grid(pb._ck2004_extinct_photon_grid[:,:,:,i,j,:])

    pb.compute_ck2004_ldcoeffs()
    pb.compute_ck2004_ldints()

    pb.compute_phoenix_response(path='tables/phoenix', verbose=True)
    pb.compute_phoenix_intensities(path='tables/phoenix', verbose=True)
    pb.compute_phoenix_reddening(path='tables/phoenix', verbose=True)

    print('Imputing phoenix Inorm grids for %s...' % (ptf[0]))
    pb.impute_atmosphere_grid(pb._phoenix_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_photon_grid)
    for i in range(len(pb._phoenix_intensity_axes[3])):
        print('Imputing phoenix Imu grid for %s, i=%d...' % (ptf[0], i))
        pb.impute_atmosphere_grid(pb._phoenix_Imu_energy_grid[:,:,:,i,:])
        pb.impute_atmosphere_grid(pb._phoenix_Imu_photon_grid[:,:,:,i,:])
    for i in range(len(pb._phoenix_extinct_axes[3])):
        for j in range(len(pb._phoenix_extinct_axes[4])):
            print('Imputing phoenix Iext grid for %s, i=%d, j=%d...' % (ptf[0], i, j))
            pb.impute_atmosphere_grid(pb._phoenix_extinct_energy_grid[:,:,:,i,j,:])
            pb.impute_atmosphere_grid(pb._phoenix_extinct_photon_grid[:,:,:,i,j,:])

    pb.compute_phoenix_ldcoeffs()
    pb.compute_phoenix_ldints()

    if ptf[5] > 0:
        pb.import_wd_atmcof('tables/wd/atmcofplanck.dat', 'tables/wd/atmcof.dat', ptf[5])

    pb.save('%s.fits' % ptf[0][:-4], history_entry='All missing table values imputed by weighted distance.')
