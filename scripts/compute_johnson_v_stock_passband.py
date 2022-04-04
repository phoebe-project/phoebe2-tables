import phoebe
from astropy import units as u

ptfs = [
    ('johnson_v.ptf',  'Johnson', 'V',  5500., 7),
]

for ptf in ptfs:
    pb = phoebe.atmospheres.passbands.Passband(
        ptf='./'+ptf[0],
        pbset=ptf[1],
        pbname=ptf[2],
        effwl=ptf[3],
        wlunits=u.AA,
        calibrated=True,
        reference='Maiz Apellaniz (2006), AJ 131, 1184',
        version=1.1,
        comments='This is an imputed stock Johnson:V passband. It does not support interstellar extinction to keep the file size down.'
    )

    pb.compute_blackbody_response()
    # pb.compute_bb_reddening(verbose=True)

    pb.compute_ck2004_response(path='tables/ck2004', verbose=True)
    pb.compute_ck2004_intensities(path='tables/ck2004', verbose=True)
    pb.compute_ck2004_ldcoeffs()
    pb.compute_ck2004_ldints()
    # pb.compute_ck2004_reddening(path='tables/ck2004', verbose=True)

    print('Imputing ck2004 Inorm grids for %s...' % (ptf[0]))
    pb.impute_atmosphere_grid(pb._ck2004_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_photon_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ld_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ld_photon_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ldint_energy_grid)
    pb.impute_atmosphere_grid(pb._ck2004_ldint_photon_grid)
    for i in range(len(pb._ck2004_intensity_axes[3])):
        print('Imputing ck2004 Imu grid for %s, i=%d...' % (ptf[0], i))
        pb.impute_atmosphere_grid(pb._ck2004_Imu_energy_grid[:,:,:,i,:])
        pb.impute_atmosphere_grid(pb._ck2004_Imu_photon_grid[:,:,:,i,:])

    pb.compute_phoenix_response(path='tables/phoenix', verbose=True)
    pb.compute_phoenix_intensities(path='tables/phoenix', verbose=True)
    pb.compute_phoenix_ldcoeffs()
    pb.compute_phoenix_ldints()
    # pb.compute_phoenix_reddening(path='tables/phoenix', verbose=True)

    print('Imputing phoenix Inorm grids for %s...' % (ptf[0]))
    pb.impute_atmosphere_grid(pb._phoenix_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_photon_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ld_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ld_photon_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ldint_energy_grid)
    pb.impute_atmosphere_grid(pb._phoenix_ldint_photon_grid)
    for i in range(len(pb._phoenix_intensity_axes[3])):
        print('Imputing phoenix Imu grid for %s, i=%d...' % (ptf[0], i))
        pb.impute_atmosphere_grid(pb._phoenix_Imu_energy_grid[:,:,:,i,:])
        pb.impute_atmosphere_grid(pb._phoenix_Imu_photon_grid[:,:,:,i,:])

    pb.import_wd_atmcof('tables/wd/atmcofplanck.dat', 'tables/wd/atmcof.dat', ptf[4])

    pb.save('%s.fits' % ptf[0][:-4], history_entry='All missing table values imputed by weighted distance.')
