aa51253-24             eRO-ExTra catalog                        (Grotova+, 2024)
================================================================================
eRO-ExTra: eROSITA extragalactic non-AGN X-ray transients and variables in 
eRASS1 and eRASS2
I. Grotova, A. Rau, M. Salvato, J. Buchner, A. J. Goodwin, Z. Liu,  
A. Malyali, A. Merloni, D. Tubín-Arenas, D. Homan, M. Krumpe, K. Nandra, 
R. Shirley, G. E. Anderson, R. Arcodia, S. Bahic, P. Baldini, 
D. A. H. Buckley, S. Ciroi, A. Kawka, M. Masterson, J. C. A. Miller-Jones, 
F. Di Mille
   <Reference (200Y)>
   =20YYjjjjjvvvvLppppA
================================================================================
ADC_Keywords: Surveys ; X-ray sources
Keywords: X-rays: galaxies / galaxies: nuclei / catalogs

Abstract:

Aims. The eROSITA telescope aboard the Spectrum Roentgen Gamma (SRG)
satellite provides an unprecedented opportunity to explore the transient
and variable extragalactic X-ray sky due to the sensitivity, sky coverage,
and cadence of the all-sky survey. While previous studies showed the
dominance of regular active galactic nuclei (AGN) variability, a small
fraction of sources expected in such a survey arise from more exotic
phenomena such as tidal disruption events (TDEs), quasi-periodic eruptions,
or other short-lived events associated with supermassive black hole
accretion. This paper describes the systematic selection of X-ray
extragalactic transients found in the first two eROSITA all-sky surveys
(eRASS) that are not associated with known AGN prior to eROSITA
observations.
Methods. We generate a variability sample using the data from the
first and second eRASS, which includes sources with variability
significance and fractional amplitude larger than four in the 0.2–2.3 keV
energy band, discovered between December 2019 and December 2020, and
located in the Legacy Survey DR10 (LS10) footprint. When possible,
transients are associated with optical LS10 counterparts. The properties
of these counterparts are used to exclude stars and known active galaxies.
The sample is additionally cleaned from known AGN using pre-eROSITA
SIMBAD and the Million Quasars Catalog (Milliquas) classifications,
archival optical spectra, and archival X-ray data. We explore archival
X-ray variability, long-term (2–2.5 years) eROSITA light curves, and
peak X-ray spectra to characterize the X-ray properties of the sample.
Sources with radio counterparts are identified using the Rapid ASKAP
Continuum Survey (RACS) and Karl G. Jansky Very Large Array Sky Survey
(VLASS).
Results. We present a catalog of 304 extragalactic eROSITA transients
and variables not associated with known AGN, called eRO-ExTra. More than
90% of sources are associated with reliable LS10 optical counterparts.
For each source, we provide archival X-ray data from Swift, ROSAT, and
XMM-Newton, the eROSITA long-term light curve with light curve
classification, as well as the best power law fit spectral results at the
peak eROSITA epoch. Reliable spectroscopic and photometric redshifts,
both archival and from follow-up data, are provided for more than 80% of
the sample. Several sources in the catalog are eROSITA discovered known
TDE candidates. In addition, 31 sources are radio detected. The origin of
radio emission needs to be further identified.
Conclusions. The eRO-ExTra transients constitute a relatively clean
parent sample of non-AGN variability phenomena associated with massive
black holes. The eRO-ExTra catalog includes more than 95% of sources
discovered in X-rays with eROSITA for the first time, making it a
valuable resource for studying unique nuclear transients.

Description: 
This is the catalog of extragalactic non-AGN X-ray transients and 
variables found in the first two eROSITA all-sky surveys (eRASS). The 
catalog contains 304 unique sources with variability significance and 
fractional amplitude larger than 4 between eRASS1 and eRASS2 in the 
0.2 - 2.3 keV energy band. More than 90% of sources are associated with 
reliable LS10 optical counterparts, properties of which were used to 
exclude stars and regular or known AGN. For each source, we provide 
archival X-ray data from Swift, ROSAT and XMM-Newton, the eROSITA 
long-term lightcurve, which includes eRASS1-4 (5 if available), with 
lightcurve classification as well as the best power-law fit spectral 
results at the peak eROSITA epoch. Spectroscopic and photometric 
redshifts, both archival and from follow-up data, are provided for more 
than 90% of the sample. The eRO-ExTra catalog is the largest of its kind 
to date with more than 95% of sources discovered in X-rays with eROSITA 
for the first time.


File Summary:
--------------------------------------------------------------------------------
 FileName           Lrecl  Records  Explanations
--------------------------------------------------------------------------------
ReadMe                 80        .  This file
eroextra_final.dat   2221      304  



Description of file: -

See also:
We omitted eRASS3-4(5) fluxes for 1eRASS J113028.2-080612, 1eRASS 
J053016.3-412535 and 1eRASS J060056.2-293922, since their detailed 
follow-up and analysis will be presented in Tubín-Arenas et al., in 
prep.

We omitted information about archival X-ray observations for 
eRASSU J074426.3+291606, since the extracted data describes a galaxy 
nearby, and the correct counterpart is a smaller nearby galaxy 
(arXiv:2301.05484).
	
Byte-by-byte Description of file: eroextra_final.dat
--------------------------------------------------------------------------------
   Bytes   Format   Units         Label                Explanations
--------------------------------------------------------------------------------
   1- 23   A23      ---           ERO_NAME             official IAU name of the 
						       source from Merloni 2024 
                                                       or source name in the 
                                                       format 
                                                       eRASSU Jhhmmss.s-ddmmss
   25- 44  F20.16   deg           ERO_RA               eROSITA Right Ascension
						       (ICRS) from eRASS:5
						       (cumulative
                                                       catalogue of 4(5) eRASS)
   46- 66  F21.17   deg           ERO_DEC              eROSITA Declination 
                                                       (ICRS) from eRASS:5
   68- 85  F18.16   arcsec        ERO_POSERR           1-σ position uncertainty 
                                                       from eRASS:5
   87-100  E14.8    erg/(cm^2sec) ERO_FLUX_eRASS1      source flux in energy  
                                                       band 0.2-2.3 keV 
						       in eRASS1
  102-115  E14.8    erg/(cm^2sec) ERO_FLUX_eRASS2      source flux in the energy  
                                                       band 0.2-2.3 keV 
						       in eRASS2          
  117-130  E14.8    erg/(cm^2sec) ERO_FLUX_eRASS3      source flux in the energy  
                                                       band 0.2-2.3 keV 
						       in eRASS3         
  132-145  E14.8    erg/(cm^2sec) ERO_FLUX_eRASS4      source flux in the energy 
                                                       band 0.2-2.3 keV 
						       in eRASS4         
  147-160  E14.8    erg/(cm^2sec) ERO_FLUX_eRASS5      source flux in the energy
                                                       band 0.2-2.3 keV 
						       in eRASS5 
  162-177  E16.8    erg/(cm^2sec) ERO_FLUX_ERR_eRASS1  error flux (68 %) 
						       in energy  
                                                       band 0.2-2.3 keV 
						       in eRASS1; -1=flux upper 
						       limit (99.7%)
  179-194  E16.8    erg/(cm^2sec) ERO_FLUX_ERR_eRASS2  error flux (68 %) in
						       energy band 0.2-2.3 keV 
                                                       in eRASS2; -1=flux upper 
                                                       limit (99.7%)    
  196-211  E16.8    erg/(cm^2sec) ERO_FLUX_ERR_eRASS3  error flux (68 %) in
						       energy band 0.2-2.3 keV
                                                       in eRASS3; -1=flux upper 
                                                       limit (99.7%)        
  213-228  E16.8    erg/(cm^2sec) ERO_FLUX_ERR_eRASS4  error flux (68 %) in  
                                                       energy band 0.2-2.3 keV 
						       in eRASS4; -1=flux upper 
                                                       limit (99.7%)        
  230-245  E16.8    erg/(cm^2sec) ERO_FLUX_ERR_eRASS5  error flux (68 %) in
						       energy band 0.2-2.3 keV
                                                       in eRASS5; -1=flux upper 
                                                       limit (99.7%)  
  247-266  F20.16   ---           Amplitude            amplitude of variability  
                                                       between eRASS1 and eRASS2
  268-286  F19.16   ---           Significance         significance of
						       variability between 
                                                       eRASS1 and eRASS2
  288-290  F3.1     ---           ERO_LCCLASS          eROSITA lightcurve class: 
                                                       1=decline, 2=flare,
             					       3=brightening, 4=other
  292-332  A41      mjd           ERO_DATE             dates of eROSITA
						       observations:
						       (MJD_1,..,MJD_<N>),
                                                       N =1,2,3,4, 
                                                       (5, if available)

  334-340  E7.2     1/cm^2        NH                   Galactic equivalent  
                                                       neutral hydrogen column 
						       density in the line of
						       sight
  342-359  F18.16   ---           ERO_GAMMA            photon index for the peak
					               eRASS 
  361-380  F20.18   ---           ERO_GAMMA_ERR        error photon index (68 %)  
                                                       for the peak eRASS
  382-393  A12      ---           ERO_CSTAT_DOF        C-statistic per degree of
						       freedom, used to assess 
                                                       the goodness of fit
  395-416  E22.16   erg/(cm^2sec) ERO_FLUX_MOD         source flux in energy 
                                                       band 0.2-2.3 keV for the 
						       peak eRASS
  418-439  E22.16   erg/(cm^2sec) ERO_FLUX_MOD_ERR     error flux (68 %) in energy 
                                                       band 0.2-2.3 keV for the 
						       peak eRASS
  441-444  F4.1     ---           ARCH_FLAG            archival X-ray 
						       constraints: 
                                                       0=not constraining UL, 
                                                       1=constraining UL, 
                                                       2=previously detected
  446-688  A243     mjd           ARCH_DATE            dates of N archival 
						       observations: 
                                                       (X_1,..,X_<N>)
  690-981  A292     erg/(cm^2sec) ARCH_FLUX            source flux of N archival
						       observations: 
                                                       (F_1,..,F_<N>) in energy 
						       band 0.2-2.0 keV
  983-1090 A108     erg/(cm^2sec) ARCH_FLUX_ERR        error flux (68 %) of N
						       archival observations:
                                                       (F_err_1,..,F_err_<N>) 
                                                       in energy band 
						       0.2-2.0 keV;-1=flux upper 
                                                       limit (99.7%) 
  1092-1473 A382    ---           ARCH_INSTRUMENT      instruments of N archival 
						       observations 
                                                       (Instrument_1,..,
							Instrument_<N>)
  1475-1490 E16.5    ---          NWAY_bias_LS10_Xray_proba probability 
						       weighting introduced by 
                                                       Xray_proba prior (see 
						       Salvato et al 2018
                                                       for clarification)

  1492-1501 F10.7    ---          NWAY_dist_bayesfactor logarithm of the ratio
						       of the prior and
						       posterior from 
                                                       separation, positional	    
                                                       error, and number 
						       density (see appendix in
                                                       Salvato et al 2018 for
                                                       clarification)
  1503-1514 F12.10   ---          NWAY_dist_post       distance posterior
						       probability comparing 
                                                       this association vs. no 
                                                       association (see appendix
						       in Salvato et al 2018
                                                       for clarification)
  1516-1530 E15.7    ---          NWAY_p_single        same as dist_post, but 
						       weighted by the prior
                                                       (see appendix in 
                                                       Salvato et al 2018 
						       for clarification)
  1532-1546 E15.7    ---          NWAY_p_any           for each entry in the
						       X-ray catalogue, the
                                                       probability that there is
						       a counterpart (see
                                                       appendix in 
						       Salvato et al 2018
                                                       for clarification)
  1548-1557 F10.8    ---          NWAY_p_i             relative probability of 
						       the eROSITA/LS10 match
                                                       (see the appendix in 
						       Salvato et  al 2018
                                                       for clarification)

  1559-1563 I5       ---          LS10_RELEASE         integer denoting the
						       camera and filter set 
                                                       used in Legacy survey 
                                                       DR10 (LS10), which will 
                                                       be unique for a given 
						       processing run of data
  1565-1570 I6       ---          LS10_BRICKID         LS10 Brick ID
  1572-1576 I5       ---          LS10_OBJID           catalog object number  
                                                       within thisLS10 brick
  1578-1597 F20.16   deg          LS10_RA              J2000 Right Ascension 
                                                       of the LS10 counterpart
  1599-1618 F20.16   deg          LS10_DEC             J2000 Declination of  
                                                       the LS10counterpart
  1620-1632 E13.8    1/deg^2      LS10_RA_IVAR         inverse variance of RA,  
                                                       excluding astrometric 
					               calibration errors 
  1634-1646 E13.8    1/deg^2      LS10_DEC_IVAR        inverse variance of DEC, 
                                                       excluding astrometric 
						       calibration errors 
  1648-1662 F15.10   nanomaggy    LS10_FLUX_G          LS10 model flux g
  1664-1676 F13.8    nanomaggy    LS10_FLUX_R          LS10 model flux r
  1678-1690 F13.8    nanomaggy    LS10_FLUX_I          LS10 model flux i
  1692-1704 F13.8    nanomaggy    LS10_FLUX_Z          LS10 model flux z
  1706-1717 F12.7    nanomaggy    LS10_FLUX_W1         LS10 model flux W1
  1719-1731 F13.8    nanomaggy    LS10_FLUX_W2         LS10 model flux W2
  1733-1744 F12.7    1/nanomaggy^2 LS10_FLUX_IVAR_G    Inverse variance of 
						       flux g
  1746-1757 F12.7    1/nanomaggy^2 LS10_FLUX_IVAR_R    Inverse variance of
						       flux r
  1759-1771 F13.8    1/nanomaggy^2 LS10_FLUX_IVAR_I    Inverse variance of
						       flux r
  1773-1784 F12.8    1/nanomaggy^2 LS10_FLUX_IVAR_Z    Inverse variance of
						       flux z

  1786-1797 F12.9    1/nanomaggy^2 LS10_FLUX_IVAR_W1   Inverse variance of
						       flux W1
  1799-1809 F11.9    1/nanomaggy^2 LS10_FLUX_IVAR_W2   Inverse variance of
						       flux W2
  1811-1820 F10.8    ---          LS10_MW_TRANSMISSION_G  Galactic 
                                                       transmission in g filter
						       in linear units [0, 1]
  1822-1831 F10.8    ---          LS10_MW_TRANSMISSION_R  Galactic 
                                                       transmission in r filter
						       in linear units [0, 1]
  1833-1842 F10.8    ---          LS10_MW_TRANSMISSION_I  Galactic 
                                                       transmission in i filter
						       in linear units [0, 1]
  1844-1853 F10.8    ---          LS10_MW_TRANSMISSION_Z  Galactic 
                                                       transmission in z filter
						       in linear units [0, 1]
  1855-1864 F10.8    ---          LS10_MW_TRANSMISSION_W1 Galactic 
                                                       transmission in W1 filter
						       in linear units [0, 1]
  1866-1875 F10.8    ---          LS10_MW_TRANSMISSION_W2 Galactic 
                                                       transmission in W2 filter
						       in linear units [0, 1]
  1877-1879 A3       ---          LS10_TYPE            morphological model from
						       LS10
  1881-1898 F18.16   ---          Z_REDSHIFT           redshift
  1900-1905 A6       ---          Z_TYPE               redshift type: 
						       photoz = photometric, 
                                                       specz = spectroscopic
  1907-1927 A21      ---          Z_REFERENCE          redshift origin
  1929-1964 A36      ---          SIMBAD_NAME          SIMBAD source ID
  1966-1979 F14.10   deg          SIMBAD_RA            SIMBAD J2000 Right
					               Ascension
  1981-1994 F14.10   deg          SIMBAD_DEC           SIMBAD J2000 Declination
  1996-2012 A17      ---          SIMBAD_TYPE          SIMBAD main type
  2014-2023 A10      ---          TNS_NAME             Transient Name Server 
						       (TNS) source name
  2025-2040 F16.12   deg          TNS_RA               TNS Right Ascension
  2042-2059 F18.14   deg          TNS_DEC              TNS Declination
  2061-2078 F18.12   mjd          TNS_DATE             TNS discovery date
  2080-2110 A31      ---          VLASS_NAME           The Very Large Array Sky
				                       Survey (VLASS)
  2112-2129 F18.14   deg          VLASS_RA             VLASS Right Ascension
  2131-2149 F19.15   deg          VLASS_DEC            VLASS Declination
  2151-2168 F18.16   mJy          VLASS_FLUX           VLASS total flux density
 						       at 3GHz
  2170-2194 A25      ---          RACS_NAME            Rapid ASKAP Continuum
					               Survey (RACS)
  2196-2205 F10.6    deg          RACS_RA              RACS Right Ascension
  2207-2216 F10.6    deg          RACS_DEC             RACS Declination
  2218-2224 F7.3     mJy          RACS_FLUX            RACS total flux density 
                				       at 0.88GHz


Acknowledgements: Iuliia Grotova, grotova@mpe.mpg.de

References:

================================================================================
