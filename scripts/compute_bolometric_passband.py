import phoebe
from astropy import units as u

ptfs = [
    ('bolometric.ptf',  'Bolometric', '900-40000',  20450.),
]

for ptf in ptfs:
    pb = phoebe.atmospheres.passbands.Passband(
        ptf='./'+ptf[0],
        pbset=ptf[1],
        pbname=ptf[2],
        effwl=ptf[3],
        wlunits=u.m,
        calibrated=True,
        reference='Uniform response from 900A to 40um.',
        version=1.1,
        comments='This passband is needed for reflection effect in PHOEBE. This passband does not support interstellar extinction. It should not be used as an actual passband.'
    )

    pb.compute_blackbody_response()
    # pb.compute_bb_reddening(verbose=True)

    pb.compute_ck2004_response(path='tables/ck2004', verbose=True)
    pb.compute_ck2004_intensities(path='tables/ck2004', verbose=True)
    pb.compute_ck2004_ldcoeffs()
    pb.compute_ck2004_ldints()
    # pb.compute_ck2004_reddening(path='tables/ck2004', verbose=True)

    print('Imputing Inorm grids...')
    pb.impute_atmosphere_grid(pb._ck2004_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_photon_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ld_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ld_photon_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ldint_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ldint_photon_grid)
    for i in range(len(pb._ck2004_intensity_axes[3])):
        print('Imputing Imu grid for i=%d...' % i)
        pb.impute_atmosphere_grid(pb._ck2004_Imu_energy_grid[:,:,:,i,:])
        pb.impute_atmosphere_grid(pb._ck2004_Imu_photon_grid[:,:,:,i,:])

    pb.compute_phoenix_response(path='tables/phoenix', verbose=True)
    pb.compute_phoenix_intensities(path='tables/phoenix', verbose=True)
    pb.compute_phoenix_ldcoeffs()
    pb.compute_phoenix_ldints()
    # pb.compute_phoenix_reddening(path='tables/phoenix', verbose=True)

    print('Imputing Inorm grids...')
    pb.impute_atmosphere_grid(pb._phoenix_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_photon_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ld_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ld_photon_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ldint_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ldint_photon_grid)
    for i in range(len(pb._phoenix_intensity_axes[3])):
        print('Imputing Imu grid for i=%d...' % i)
        pb.impute_atmosphere_grid(pb._phoenix_Imu_energy_grid[:,:,:,i,:])
        pb.impute_atmosphere_grid(pb._phoenix_Imu_photon_grid[:,:,:,i,:])

    pb.save('%s.fits' % ptf[0][:-4], history_entry='All missing table values imputed by weighted distance.')
