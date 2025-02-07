# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Wed 27 Nov 2024 22:04:04



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

YnRE1x1 = Parameter(name = 'YnRE1x1',
                    nature = 'external',
                    type = 'real',
                    value = -5.36069115e-6,
                    texname = '\\text{YnRE1x1}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 1, 1 ])

YnRE1x2 = Parameter(name = 'YnRE1x2',
                    nature = 'external',
                    type = 'real',
                    value = 3.56680355e-6,
                    texname = '\\text{YnRE1x2}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 1, 2 ])

YnRE1x3 = Parameter(name = 'YnRE1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.0000167216561,
                    texname = '\\text{YnRE1x3}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 1, 3 ])

YnRE2x1 = Parameter(name = 'YnRE2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.0000147518449,
                    texname = '\\text{YnRE2x1}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 2, 1 ])

YnRE2x2 = Parameter(name = 'YnRE2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.0000196864525,
                    texname = '\\text{YnRE2x2}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 2, 2 ])

YnRE2x3 = Parameter(name = 'YnRE2x3',
                    nature = 'external',
                    type = 'real',
                    value = -8.06167919e-6,
                    texname = '\\text{YnRE2x3}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 2, 3 ])

YnRE3x1 = Parameter(name = 'YnRE3x1',
                    nature = 'external',
                    type = 'real',
                    value = 8.23083914e-6,
                    texname = '\\text{YnRE3x1}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 3, 1 ])

YnRE3x2 = Parameter(name = 'YnRE3x2',
                    nature = 'external',
                    type = 'real',
                    value = -9.03703021e-6,
                    texname = '\\text{YnRE3x2}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 3, 2 ])

YnRE3x3 = Parameter(name = 'YnRE3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.0000119844673,
                    texname = '\\text{YnRE3x3}',
                    lhablock = 'COUPLINGSYN',
                    lhacode = [ 3, 3 ])

YnIMG1x1 = Parameter(name = 'YnIMG1x1',
                     nature = 'external',
                     type = 'real',
                     value = 1.14274594e-6,
                     texname = '\\text{YnIMG1x1}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 1, 1 ])

YnIMG1x2 = Parameter(name = 'YnIMG1x2',
                     nature = 'external',
                     type = 'real',
                     value = -5.21611574e-8,
                     texname = '\\text{YnIMG1x2}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 1, 2 ])

YnIMG1x3 = Parameter(name = 'YnIMG1x3',
                     nature = 'external',
                     type = 'real',
                     value = 9.31428046e-6,
                     texname = '\\text{YnIMG1x3}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 1, 3 ])

YnIMG2x1 = Parameter(name = 'YnIMG2x1',
                     nature = 'external',
                     type = 'real',
                     value = 5.50929349e-7,
                     texname = '\\text{YnIMG2x1}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 2, 1 ])

YnIMG2x2 = Parameter(name = 'YnIMG2x2',
                     nature = 'external',
                     type = 'real',
                     value = -4.18613389e-6,
                     texname = '\\text{YnIMG2x2}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 2, 2 ])

YnIMG2x3 = Parameter(name = 'YnIMG2x3',
                     nature = 'external',
                     type = 'real',
                     value = 4.4905086e-6,
                     texname = '\\text{YnIMG2x3}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 2, 3 ])

YnIMG3x1 = Parameter(name = 'YnIMG3x1',
                     nature = 'external',
                     type = 'real',
                     value = -8.19009887e-7,
                     texname = '\\text{YnIMG3x1}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 3, 1 ])

YnIMG3x2 = Parameter(name = 'YnIMG3x2',
                     nature = 'external',
                     type = 'real',
                     value = 1.53826195e-6,
                     texname = '\\text{YnIMG3x2}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 3, 2 ])

YnIMG3x3 = Parameter(name = 'YnIMG3x3',
                     nature = 'external',
                     type = 'real',
                     value = -6.67557635e-6,
                     texname = '\\text{YnIMG3x3}',
                     lhablock = 'IMCOUPLINGSYN',
                     lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 0.007757951900698216,
                  texname = '\\alpha _w^{-1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_F',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1172,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MMZ = Parameter(name = 'MMZ',
                nature = 'external',
                type = 'real',
                value = 91.1876,
                texname = 'm_Z',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

MMW = Parameter(name = 'MMW',
                nature = 'external',
                type = 'real',
                value = 79.947,
                texname = 'm_W',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

MMC = Parameter(name = 'MMC',
                nature = 'external',
                type = 'real',
                value = 1.2,
                texname = 'm_c',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

MMB = Parameter(name = 'MMB',
                nature = 'external',
                type = 'real',
                value = 4.23,
                texname = 'm_b',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

MMT = Parameter(name = 'MMT',
                nature = 'external',
                type = 'real',
                value = 175,
                texname = 'm_t',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

QS = Parameter(name = 'QS',
               nature = 'external',
               type = 'real',
               value = 100.,
               texname = 'Q_s',
               lhablock = 'FRBlock',
               lhacode = [ 6 ])

emH = Parameter(name = 'emH',
                nature = 'external',
                type = 'real',
                value = 125.09,
                texname = 'm_{\\left\\{0,\\frac{h+v}{\\sqrt{2}}\\right\\}}',
                lhablock = 'FRBlock',
                lhacode = [ 7 ])

deltaA = Parameter(name = 'deltaA',
                   nature = 'external',
                   type = 'real',
                   value = 10.,
                   texname = '\\text{deltaA}',
                   lhablock = 'FRBlock',
                   lhacode = [ 8 ])

emN1 = Parameter(name = 'emN1',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{emN1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 9 ])

emN2 = Parameter(name = 'emN2',
                 nature = 'external',
                 type = 'real',
                 value = 0.2,
                 texname = '\\text{emN2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 10 ])

emN3 = Parameter(name = 'emN3',
                 nature = 'external',
                 type = 'real',
                 value = 0.3,
                 texname = '\\text{emN3}',
                 lhablock = 'FRBlock',
                 lhacode = [ 11 ])

delta1 = Parameter(name = 'delta1',
                   nature = 'external',
                   type = 'real',
                   value = 20.,
                   texname = '\\text{delta1}',
                   lhablock = 'FRBlock',
                   lhacode = [ 12 ])

emetaI = Parameter(name = 'emetaI',
                   nature = 'external',
                   type = 'real',
                   value = 115.,
                   texname = '\\text{emetaI}',
                   lhablock = 'FRBlock',
                   lhacode = [ 13 ])

emphi2 = Parameter(name = 'emphi2',
                   nature = 'external',
                   type = 'real',
                   value = 125.,
                   texname = '\\text{emphi2}',
                   lhablock = 'FRBlock',
                   lhacode = [ 14 ])

emphi1 = Parameter(name = 'emphi1',
                   nature = 'external',
                   type = 'real',
                   value = 105.,
                   texname = '\\text{emphi1}',
                   lhablock = 'FRBlock',
                   lhacode = [ 15 ])

etheta = Parameter(name = 'etheta',
                   nature = 'external',
                   type = 'real',
                   value = 0.7854,
                   texname = '\\text{etheta}',
                   lhablock = 'FRBlock',
                   lhacode = [ 16 ])

leta = Parameter(name = 'leta',
                 nature = 'external',
                 type = 'real',
                 value = 0.0001,
                 texname = '\\text{leta}',
                 lhablock = 'FRBlock',
                 lhacode = [ 17 ])

lsigma = Parameter(name = 'lsigma',
                   nature = 'external',
                   type = 'real',
                   value = 0.0002,
                   texname = '\\text{lsigma}',
                   lhablock = 'FRBlock',
                   lhacode = [ 18 ])

lHeta1 = Parameter(name = 'lHeta1',
                   nature = 'external',
                   type = 'real',
                   value = 0.0003,
                   texname = '\\text{lHeta1}',
                   lhablock = 'FRBlock',
                   lhacode = [ 19 ])

lHeta2 = Parameter(name = 'lHeta2',
                   nature = 'external',
                   type = 'real',
                   value = 0.0004,
                   texname = '\\text{lHeta2}',
                   lhablock = 'FRBlock',
                   lhacode = [ 20 ])

lHsigma = Parameter(name = 'lHsigma',
                    nature = 'external',
                    type = 'real',
                    value = 0.0005,
                    texname = '\\text{lHsigma}',
                    lhablock = 'FRBlock',
                    lhacode = [ 21 ])

letasigma = Parameter(name = 'letasigma',
                      nature = 'external',
                      type = 'real',
                      value = 0.0006,
                      texname = '\\text{letasigma}',
                      lhablock = 'FRBlock',
                      lhacode = [ 22 ])

s12sq = Parameter(name = 's12sq',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = '\\text{s12sq}',
                  lhablock = 'FRBlock',
                  lhacode = [ 23 ])

s13sq = Parameter(name = 's13sq',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = '\\text{s13sq}',
                  lhablock = 'FRBlock',
                  lhacode = [ 24 ])

s23sq = Parameter(name = 's23sq',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = '\\text{s23sq}',
                  lhablock = 'FRBlock',
                  lhacode = [ 25 ])

alpha = Parameter(name = 'alpha',
                  nature = 'external',
                  type = 'real',
                  value = 1.2,
                  texname = '\\alpha',
                  lhablock = 'FRBlock',
                  lhacode = [ 26 ])

deltaCP = Parameter(name = 'deltaCP',
                    nature = 'external',
                    type = 'real',
                    value = 1.3,
                    texname = '\\text{deltaCP}',
                    lhablock = 'FRBlock',
                    lhacode = [ 27 ])

zeta1 = Parameter(name = 'zeta1',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{zeta1}',
                  lhablock = 'FRBlock',
                  lhacode = [ 28 ])

zeta2 = Parameter(name = 'zeta2',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{zeta2}',
                  lhablock = 'FRBlock',
                  lhacode = [ 29 ])

zeta3 = Parameter(name = 'zeta3',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{zeta3}',
                  lhablock = 'FRBlock',
                  lhacode = [ 30 ])

sign = Parameter(name = 'sign',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{sign}',
                 lhablock = 'FRBlock',
                 lhacode = [ 31 ])

Dm21sq = Parameter(name = 'Dm21sq',
                   nature = 'external',
                   type = 'real',
                   value = 7.1e-23,
                   texname = '\\text{Dm21sq}',
                   lhablock = 'FRBlock',
                   lhacode = [ 32 ])

Dm3lsq = Parameter(name = 'Dm3lsq',
                   nature = 'external',
                   type = 'real',
                   value = 2.5e-21,
                   texname = '\\text{Dm3lsq}',
                   lhablock = 'FRBlock',
                   lhacode = [ 33 ])

NOorIO = Parameter(name = 'NOorIO',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{NOorIO}',
                   lhablock = 'FRBlock',
                   lhacode = [ 34 ])

Mnue = Parameter(name = 'Mnue',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Mnue}',
                 lhablock = 'MASS',
                 lhacode = [ 12 ])

Mnum = Parameter(name = 'Mnum',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Mnum}',
                 lhablock = 'MASS',
                 lhacode = [ 14 ])

Mnut = Parameter(name = 'Mnut',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{Mnut}',
                 lhablock = 'MASS',
                 lhacode = [ 16 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.1057,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 2.,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 0.01,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9000006 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 0.02,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9000007 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 0.03,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9000008 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 1.,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Wetach = Parameter(name = 'Wetach',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{Wetach}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000009 ])

WetaI = Parameter(name = 'WetaI',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{WetaI}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000010 ])

Wphi2 = Parameter(name = 'Wphi2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{Wphi2}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000011 ])

Wphi1 = Parameter(name = 'Wphi1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{Wphi1}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000012 ])

c1 = Parameter(name = 'c1',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cmath.sin(zeta1)**2)',
               texname = '\\text{c1}')

c12 = Parameter(name = 'c12',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - s12sq)',
                texname = '\\text{c12}')

c13 = Parameter(name = 'c13',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - s13sq)',
                texname = '\\text{c13}')

c2 = Parameter(name = 'c2',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cmath.sin(zeta2)**2)',
               texname = '\\text{c2}')

c23 = Parameter(name = 'c23',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - s23sq)',
                texname = '\\text{c23}')

c3 = Parameter(name = 'c3',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cmath.sin(zeta3)**2)',
               texname = '\\text{c3}')

MB = Parameter(name = 'MB',
               nature = 'internal',
               type = 'real',
               value = 'MMB',
               texname = 'm_b')

metaI = Parameter(name = 'metaI',
                  nature = 'internal',
                  type = 'real',
                  value = 'emetaI',
                  texname = '\\text{metaI}')

mH = Parameter(name = 'mH',
               nature = 'internal',
               type = 'real',
               value = 'emH',
               texname = '\\text{mH}')

mN1 = Parameter(name = 'mN1',
                nature = 'internal',
                type = 'real',
                value = 'emN1',
                texname = '\\text{mN1}')

mN2 = Parameter(name = 'mN2',
                nature = 'internal',
                type = 'real',
                value = 'emN2',
                texname = '\\text{mN2}')

mN3 = Parameter(name = 'mN3',
                nature = 'internal',
                type = 'real',
                value = 'emN3',
                texname = '\\text{mN3}')

mnu2 = Parameter(name = 'mnu2',
                 nature = 'internal',
                 type = 'real',
                 value = 'NOorIO*cmath.sqrt(Dm21sq) + (1 - NOorIO)*cmath.sqrt(abs(Dm3lsq))',
                 texname = '\\text{mnu2}')

mnum = Parameter(name = 'mnum',
                 nature = 'internal',
                 type = 'real',
                 value = 'NOorIO*cmath.sqrt(abs(Dm3lsq)) + (1 - NOorIO)*cmath.sqrt(-Dm21sq + abs(Dm3lsq))',
                 texname = '\\text{mnum}')

mphi1 = Parameter(name = 'mphi1',
                  nature = 'internal',
                  type = 'real',
                  value = 'emphi1',
                  texname = '\\text{mphi1}')

mphi2 = Parameter(name = 'mphi2',
                  nature = 'internal',
                  type = 'real',
                  value = 'emphi2',
                  texname = '\\text{mphi2}')

MT = Parameter(name = 'MT',
               nature = 'internal',
               type = 'real',
               value = 'MMT',
               texname = 'm_t')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'MMW',
               texname = 'm_W')

MZ = Parameter(name = 'MZ',
               nature = 'internal',
               type = 'real',
               value = 'MMZ',
               texname = 'm_Z')

s1 = Parameter(name = 's1',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(zeta1)',
               texname = '\\text{s1}')

s12 = Parameter(name = 's12',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(s12sq)',
                texname = '\\text{s12}')

s13 = Parameter(name = 's13',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(s13sq)',
                texname = '\\text{s13}')

s2 = Parameter(name = 's2',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(zeta2)',
               texname = '\\text{s2}')

s23 = Parameter(name = 's23',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(s23sq)',
                texname = '\\text{s23}')

s3 = Parameter(name = 's3',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(zeta3)',
               texname = '\\text{s3}')

theta = Parameter(name = 'theta',
                  nature = 'internal',
                  type = 'real',
                  value = 'etheta',
                  texname = '\\theta')

u11I = Parameter(name = 'u11I',
                 nature = 'internal',
                 type = 'real',
                 value = '0.',
                 texname = '\\text{u11I}')

u23I = Parameter(name = 'u23I',
                 nature = 'internal',
                 type = 'real',
                 value = '0.',
                 texname = '\\text{u23I}')

u33I = Parameter(name = 'u33I',
                 nature = 'internal',
                 type = 'real',
                 value = '0.',
                 texname = '\\text{u33I}')

x1I = Parameter(name = 'x1I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x1I}')

x2I = Parameter(name = 'x2I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x2I}')

x3I = Parameter(name = 'x3I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x3I}')

x4I = Parameter(name = 'x4I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x4I}')

x5I = Parameter(name = 'x5I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x5I}')

x6I = Parameter(name = 'x6I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x6I}')

x7I = Parameter(name = 'x7I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x7I}')

x8I = Parameter(name = 'x8I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x8I}')

x9I = Parameter(name = 'x9I',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{x9I}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEWM1)*cmath.sqrt(cmath.pi)',
               texname = '\\text{ee}')

gs = Parameter(name = 'gs',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
               texname = 'g_s')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '0.8408964152537146/cmath.sqrt(Gf)',
              texname = 'v')

ctheta = Parameter(name = 'ctheta',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.cos(theta)',
                   texname = '\\text{ctheta}')

CW2 = Parameter(name = 'CW2',
                nature = 'internal',
                type = 'real',
                value = 'MW**2/MZ**2',
                texname = 'c_w^2')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(mH**2)/cmath.sqrt(2)',
                texname = '\\text{muH}')

stheta = Parameter(name = 'stheta',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sin(theta)',
                   texname = '\\text{stheta}')

u11R = Parameter(name = 'u11R',
                 nature = 'internal',
                 type = 'real',
                 value = 'c12*c13',
                 texname = '\\text{u11R}')

u12I = Parameter(name = 'u12I',
                 nature = 'internal',
                 type = 'real',
                 value = 'c13*s12*cmath.sin(alpha)',
                 texname = '\\text{u12I}')

u12R = Parameter(name = 'u12R',
                 nature = 'internal',
                 type = 'real',
                 value = 'c13*s12*cmath.cos(alpha)',
                 texname = '\\text{u12R}')

u13I = Parameter(name = 'u13I',
                 nature = 'internal',
                 type = 'real',
                 value = '-(s13*cmath.sin(deltaCP))',
                 texname = '\\text{u13I}')

u13R = Parameter(name = 'u13R',
                 nature = 'internal',
                 type = 'real',
                 value = 's13*cmath.cos(deltaCP)',
                 texname = '\\text{u13R}')

u21I = Parameter(name = 'u21I',
                 nature = 'internal',
                 type = 'real',
                 value = '-(c12*s13*s23*cmath.sin(deltaCP))',
                 texname = '\\text{u21I}')

u21R = Parameter(name = 'u21R',
                 nature = 'internal',
                 type = 'real',
                 value = '-(c23*s12) - c12*s13*s23*cmath.cos(deltaCP)',
                 texname = '\\text{u21R}')

u22I = Parameter(name = 'u22I',
                 nature = 'internal',
                 type = 'real',
                 value = 'c12*c23*cmath.sin(alpha) - s12*s13*s23*cmath.sin(alpha + deltaCP)',
                 texname = '\\text{u22I}')

u22R = Parameter(name = 'u22R',
                 nature = 'internal',
                 type = 'real',
                 value = 'c12*c23*cmath.cos(alpha) - s12*s13*s23*cmath.cos(alpha + deltaCP)',
                 texname = '\\text{u22R}')

u23R = Parameter(name = 'u23R',
                 nature = 'internal',
                 type = 'real',
                 value = 'c13*s23',
                 texname = '\\text{u23R}')

u31I = Parameter(name = 'u31I',
                 nature = 'internal',
                 type = 'real',
                 value = '-(c12*c23*s13*cmath.sin(deltaCP))',
                 texname = '\\text{u31I}')

u31R = Parameter(name = 'u31R',
                 nature = 'internal',
                 type = 'real',
                 value = 's12*s23 - c12*c23*s13*cmath.cos(deltaCP)',
                 texname = '\\text{u31R}')

u32I = Parameter(name = 'u32I',
                 nature = 'internal',
                 type = 'real',
                 value = '-(c12*s23*cmath.sin(alpha)) - c23*s12*s13*cmath.sin(alpha + deltaCP)',
                 texname = '\\text{u32I}')

u32R = Parameter(name = 'u32R',
                 nature = 'internal',
                 type = 'real',
                 value = '-(c12*s23*cmath.cos(alpha)) - c23*s12*s13*cmath.cos(alpha + deltaCP)',
                 texname = '\\text{u32R}')

u33R = Parameter(name = 'u33R',
                 nature = 'internal',
                 type = 'real',
                 value = 'c13*c23',
                 texname = '\\text{u33R}')

x1R = Parameter(name = 'x1R',
                nature = 'internal',
                type = 'real',
                value = 'c2*c3',
                texname = '\\text{x1R}')

x2R = Parameter(name = 'x2R',
                nature = 'internal',
                type = 'real',
                value = '-(c1*s3) - s1*s2*s3',
                texname = '\\text{x2R}')

x3R = Parameter(name = 'x3R',
                nature = 'internal',
                type = 'real',
                value = '-(c1*c3*s2) + s1*s3',
                texname = '\\text{x3R}')

x4R = Parameter(name = 'x4R',
                nature = 'internal',
                type = 'real',
                value = 'c2*s3',
                texname = '\\text{x4R}')

x5R = Parameter(name = 'x5R',
                nature = 'internal',
                type = 'real',
                value = 'c1*c3 - s1*s2*s3',
                texname = '\\text{x5R}')

x6R = Parameter(name = 'x6R',
                nature = 'internal',
                type = 'real',
                value = '-(c3*s1) - c1*s2*s3',
                texname = '\\text{x6R}')

x7R = Parameter(name = 'x7R',
                nature = 'internal',
                type = 'real',
                value = 's2',
                texname = '\\text{x7R}')

x8R = Parameter(name = 'x8R',
                nature = 'internal',
                type = 'real',
                value = 'c2*s1',
                texname = '\\text{x8R}')

x9R = Parameter(name = 'x9R',
                nature = 'internal',
                type = 'real',
                value = 'c1*c2',
                texname = '\\text{x9R}')

lH = Parameter(name = 'lH',
               nature = 'internal',
               type = 'real',
               value = 'mH**2/(2.*v**2)',
               texname = '\\text{lH}')

cTri = Parameter(name = 'cTri',
                 nature = 'internal',
                 type = 'real',
                 value = '(ctheta*(-mphi1**2 + mphi2**2)*stheta)/v',
                 texname = '\\text{cTri}')

CW = Parameter(name = 'CW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(CW2)',
               texname = 'c_w')

m1hat = Parameter(name = 'm1hat',
                  nature = 'internal',
                  type = 'real',
                  value = 'mN1*(-((metaI**2*cmath.log(metaI**2/mN1**2))/(metaI**2 - mN1**2)) + (mphi1**2*stheta**2*cmath.log(mphi1**2/mN1**2))/(-mN1**2 + mphi1**2) + (ctheta**2*mphi2**2*cmath.log(mphi2**2/mN1**2))/(-mN1**2 + mphi2**2))',
                  texname = '\\text{m1hat}')

m2hat = Parameter(name = 'm2hat',
                  nature = 'internal',
                  type = 'real',
                  value = 'mN2*(-((metaI**2*cmath.log(metaI**2/mN2**2))/(metaI**2 - mN2**2)) + (mphi1**2*stheta**2*cmath.log(mphi1**2/mN2**2))/(-mN2**2 + mphi1**2) + (ctheta**2*mphi2**2*cmath.log(mphi2**2/mN2**2))/(-mN2**2 + mphi2**2))',
                  texname = '\\text{m2hat}')

m3hat = Parameter(name = 'm3hat',
                  nature = 'internal',
                  type = 'real',
                  value = 'mN3*(-((metaI**2*cmath.log(metaI**2/mN3**2))/(metaI**2 - mN3**2)) + (mphi1**2*stheta**2*cmath.log(mphi1**2/mN3**2))/(-mN3**2 + mphi1**2) + (ctheta**2*mphi2**2*cmath.log(mphi2**2/mN3**2))/(-mN3**2 + mphi2**2))',
                  texname = '\\text{m3hat}')

msigmasq = Parameter(name = 'msigmasq',
                     nature = 'internal',
                     type = 'real',
                     value = 'ctheta**2*mphi1**2 + mphi2**2*stheta**2 - (lHsigma*v**2)/2.',
                     texname = '\\text{msigmasq}')

SW2 = Parameter(name = 'SW2',
                nature = 'internal',
                type = 'real',
                value = '1 - CW2',
                texname = 's_w^2')

lHeta3 = Parameter(name = 'lHeta3',
                   nature = 'internal',
                   type = 'real',
                   value = '(-metaI**2 + ctheta**2*mphi2**2 + mphi1**2*stheta**2)/v**2',
                   texname = '\\text{lHeta3}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/CW',
               texname = 'g_1')

invsqrtm1I = Parameter(name = 'invsqrtm1I',
                       nature = 'internal',
                       type = 'real',
                       value = '(0.5 - (0.5*abs(m1hat))/m1hat)/cmath.sqrt(abs(m1hat))',
                       texname = '\\text{invsqrtm1I}')

invsqrtm1R = Parameter(name = 'invsqrtm1R',
                       nature = 'internal',
                       type = 'real',
                       value = '(0.5 + (0.5*abs(m1hat))/m1hat)/cmath.sqrt(abs(m1hat))',
                       texname = '\\text{invsqrtm1R}')

invsqrtm2I = Parameter(name = 'invsqrtm2I',
                       nature = 'internal',
                       type = 'real',
                       value = '(0.5 - (0.5*abs(m2hat))/m2hat)/cmath.sqrt(abs(m2hat))',
                       texname = '\\text{invsqrtm2I}')

invsqrtm2R = Parameter(name = 'invsqrtm2R',
                       nature = 'internal',
                       type = 'real',
                       value = '(0.5 + (0.5*abs(m2hat))/m2hat)/cmath.sqrt(abs(m2hat))',
                       texname = '\\text{invsqrtm2R}')

invsqrtm3I = Parameter(name = 'invsqrtm3I',
                       nature = 'internal',
                       type = 'real',
                       value = '(0.5 - (0.5*abs(m3hat))/m3hat)/cmath.sqrt(abs(m3hat))',
                       texname = '\\text{invsqrtm3I}')

invsqrtm3R = Parameter(name = 'invsqrtm3R',
                       nature = 'internal',
                       type = 'real',
                       value = '(0.5 + (0.5*abs(m3hat))/m3hat)/cmath.sqrt(abs(m3hat))',
                       texname = '\\text{invsqrtm3R}')

metasq = Parameter(name = 'metasq',
                   nature = 'internal',
                   type = 'real',
                   value = 'ctheta**2*mphi2**2 + mphi1**2*stheta**2 - ((lHeta1 + lHeta2 + lHeta3)*v**2)/2.',
                   texname = '\\text{metasq}')

SW = Parameter(name = 'SW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(SW2)',
               texname = 's_w')

g2 = Parameter(name = 'g2',
               nature = 'internal',
               type = 'real',
               value = 'ee/SW',
               texname = 'g_2')

metachsq = Parameter(name = 'metachsq',
                     nature = 'internal',
                     type = 'real',
                     value = 'metasq + (lHeta1*v**2)/2.',
                     texname = '\\text{metachsq}')

metach = Parameter(name = 'metach',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(abs(metachsq))',
                   texname = '\\text{metach}')

