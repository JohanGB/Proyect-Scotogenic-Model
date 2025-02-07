# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Fri 22 Nov 2024 08:47:42


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-0.5*ee**2/CW',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = 'ee**2/(2.*CW)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-0.5*(ctheta*ee**2*complex(0,1))/CW',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-gs',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*gs',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*gs**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-2*complex(0,1)*leta',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-4*complex(0,1)*leta',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-6*complex(0,1)*leta',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-6*complex(0,1)*lH',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*lHeta1)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(complex(0,1)*lHeta1) - complex(0,1)*lHeta2 + complex(0,1)*lHeta3',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-2*ctheta*cTri*complex(0,1)*stheta',
                 order = {'1':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '2*ctheta*cTri*complex(0,1)*stheta',
                 order = {'1':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee**2*complex(0,1)*stheta)/(2.*CW)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '2*ctheta*complex(0,1)*leta*stheta - ctheta*complex(0,1)*letasigma*stheta',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = 'ctheta*complex(0,1)*lHeta1*stheta + ctheta*complex(0,1)*lHeta2*stheta + ctheta*complex(0,1)*lHeta3*stheta - ctheta*complex(0,1)*lHsigma*stheta',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(ctheta**2*cTri*complex(0,1)) + cTri*complex(0,1)*stheta**2',
                 order = {'1':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(ctheta**2*complex(0,1)*letasigma) - 2*complex(0,1)*leta*stheta**2',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-2*ctheta**2*complex(0,1)*leta - complex(0,1)*letasigma*stheta**2',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(ctheta**2*complex(0,1)*lHsigma) - complex(0,1)*lHeta1*stheta**2 - complex(0,1)*lHeta2*stheta**2 - complex(0,1)*lHeta3*stheta**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(ctheta**2*complex(0,1)*lHeta1) - ctheta**2*complex(0,1)*lHeta2 - ctheta**2*complex(0,1)*lHeta3 - complex(0,1)*lHsigma*stheta**2',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '3*ctheta**3*complex(0,1)*letasigma*stheta - 6*ctheta**3*complex(0,1)*lsigma*stheta + 6*ctheta*complex(0,1)*leta*stheta**3 - 3*ctheta*complex(0,1)*letasigma*stheta**3',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '6*ctheta**3*complex(0,1)*leta*stheta - 3*ctheta**3*complex(0,1)*letasigma*stheta + 3*ctheta*complex(0,1)*letasigma*stheta**3 - 6*ctheta*complex(0,1)*lsigma*stheta**3',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-6*ctheta**4*complex(0,1)*lsigma - 6*ctheta**2*complex(0,1)*letasigma*stheta**2 - 6*complex(0,1)*leta*stheta**4',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(ctheta**4*complex(0,1)*letasigma) - 6*ctheta**2*complex(0,1)*leta*stheta**2 + 4*ctheta**2*complex(0,1)*letasigma*stheta**2 - 6*ctheta**2*complex(0,1)*lsigma*stheta**2 - complex(0,1)*letasigma*stheta**4',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-6*ctheta**4*complex(0,1)*leta - 6*ctheta**2*complex(0,1)*letasigma*stheta**2 - 6*complex(0,1)*lsigma*stheta**4',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee**2*complex(0,1))/(2.*SW**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-((ee**2*complex(0,1))/SW**2)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ctheta**2*ee**2*complex(0,1))/(2.*SW**2)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CW**2*ee**2*complex(0,1))/SW**2',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-0.5*(ctheta*ee**2*complex(0,1)*stheta)/SW**2',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(ee**2*complex(0,1)*stheta**2)/(2.*SW**2)',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '-0.5*ee/SW',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee*complex(0,1))/(SW*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-0.5*(ctheta*ee*complex(0,1))/SW',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ctheta*ee*complex(0,1))/(2.*SW)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-0.5*(CW*ee*complex(0,1))/SW',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(CW*ee*complex(0,1))/(2.*SW)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(CW*ee*complex(0,1))/SW',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-0.5*ee**2/SW',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = 'ee**2/(2.*SW)',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ctheta*ee**2*complex(0,1))/(2.*SW)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(-2*CW*ee**2*complex(0,1))/SW',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-0.5*(ee*complex(0,1)*stheta)/SW',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee*complex(0,1)*stheta)/(2.*SW)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-0.5*(ee**2*complex(0,1)*stheta)/SW',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-0.16666666666666666*(ee*complex(0,1)*SW)/CW',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1)*SW)/(2.*CW)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-0.5*(CW*ee*complex(0,1))/SW + (ee*complex(0,1)*SW)/(2.*CW)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(CW*ee*complex(0,1))/(2.*SW) + (ee*complex(0,1)*SW)/(2.*CW)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-0.5*(ctheta*CW*ee)/SW - (ctheta*ee*SW)/(2.*CW)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(CW*ee**2*complex(0,1))/SW - (ee**2*complex(0,1)*SW)/CW',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(CW*ee*stheta)/(2.*SW) + (ee*stheta*SW)/(2.*CW)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(ee**2*complex(0,1)) + (CW**2*ee**2*complex(0,1))/(2.*SW**2) + (ee**2*complex(0,1)*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = 'ee**2*complex(0,1) + (CW**2*ee**2*complex(0,1))/(2.*SW**2) + (ee**2*complex(0,1)*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = 'ctheta**2*ee**2*complex(0,1) + (ctheta**2*CW**2*ee**2*complex(0,1))/(2.*SW**2) + (ctheta**2*ee**2*complex(0,1)*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(ctheta*ee**2*complex(0,1)*stheta) - (ctheta*CW**2*ee**2*complex(0,1)*stheta)/(2.*SW**2) - (ctheta*ee**2*complex(0,1)*stheta*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = 'ee**2*complex(0,1)*stheta**2 + (CW**2*ee**2*complex(0,1)*stheta**2)/(2.*SW**2) + (ee**2*complex(0,1)*stheta**2*SW**2)/(2.*CW**2)',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((complex(0,1)*MB)/v)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-((complex(0,1)*MC)/v)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((complex(0,1)*MD)/v)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((complex(0,1)*Me)/v)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((complex(0,1)*MM)/v)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((complex(0,1)*MS)/v)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-((complex(0,1)*MT)/v)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((complex(0,1)*MTA)/v)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((complex(0,1)*MU)/v)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-6*complex(0,1)*lH*v',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(complex(0,1)*lHeta1*v)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ee**2*complex(0,1)*v)/(2.*SW**2)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(complex(0,1)*lHeta1*v) - complex(0,1)*lHeta2*v + complex(0,1)*lHeta3*v',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = 'ctheta*complex(0,1)*lHeta1*stheta*v + ctheta*complex(0,1)*lHeta2*stheta*v + ctheta*complex(0,1)*lHeta3*stheta*v - ctheta*complex(0,1)*lHsigma*stheta*v',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(ctheta**2*complex(0,1)*lHsigma*v) - complex(0,1)*lHeta1*stheta**2*v - complex(0,1)*lHeta2*stheta**2*v - complex(0,1)*lHeta3*stheta**2*v',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-(ctheta**2*complex(0,1)*lHeta1*v) - ctheta**2*complex(0,1)*lHeta2*v - ctheta**2*complex(0,1)*lHeta3*v - complex(0,1)*lHsigma*stheta**2*v',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'ee**2*complex(0,1)*v + (CW**2*ee**2*complex(0,1)*v)/(2.*SW**2) + (ee**2*complex(0,1)*SW**2*v)/(2.*CW**2)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-y1eI + complex(0,1)*y1eR',
                 order = {'1':1})

GC_84 = Coupling(name = 'GC_84',
                 value = 'y1eI + complex(0,1)*y1eR',
                 order = {'1':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(complex(0,1)*y1eI)/cmath.sqrt(2) - y1eR/cmath.sqrt(2)',
                 order = {'1':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(complex(0,1)*y1eI)/cmath.sqrt(2) + y1eR/cmath.sqrt(2)',
                 order = {'1':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((ctheta*y1eI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y1eR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ctheta*y1eI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y1eR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((stheta*y1eI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y1eR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(stheta*y1eI)/cmath.sqrt(2) + (complex(0,1)*stheta*y1eR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-y1mI + complex(0,1)*y1mR',
                 order = {'1':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'y1mI + complex(0,1)*y1mR',
                 order = {'1':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(complex(0,1)*y1mI)/cmath.sqrt(2) - y1mR/cmath.sqrt(2)',
                 order = {'1':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(complex(0,1)*y1mI)/cmath.sqrt(2) + y1mR/cmath.sqrt(2)',
                 order = {'1':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((ctheta*y1mI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y1mR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ctheta*y1mI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y1mR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((stheta*y1mI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y1mR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(stheta*y1mI)/cmath.sqrt(2) + (complex(0,1)*stheta*y1mR)/cmath.sqrt(2)',
                 order = {'1':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-y1tI + complex(0,1)*y1tR',
                 order = {'1':1})

GC_100 = Coupling(name = 'GC_100',
                  value = 'y1tI + complex(0,1)*y1tR',
                  order = {'1':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(complex(0,1)*y1tI)/cmath.sqrt(2) - y1tR/cmath.sqrt(2)',
                  order = {'1':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(complex(0,1)*y1tI)/cmath.sqrt(2) + y1tR/cmath.sqrt(2)',
                  order = {'1':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((ctheta*y1tI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y1tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ctheta*y1tI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y1tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((stheta*y1tI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y1tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(stheta*y1tI)/cmath.sqrt(2) + (complex(0,1)*stheta*y1tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-y2eI + complex(0,1)*y2eR',
                  order = {'1':1})

GC_108 = Coupling(name = 'GC_108',
                  value = 'y2eI + complex(0,1)*y2eR',
                  order = {'1':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(complex(0,1)*y2eI)/cmath.sqrt(2) - y2eR/cmath.sqrt(2)',
                  order = {'1':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(complex(0,1)*y2eI)/cmath.sqrt(2) + y2eR/cmath.sqrt(2)',
                  order = {'1':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((ctheta*y2eI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y2eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(ctheta*y2eI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y2eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((stheta*y2eI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y2eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(stheta*y2eI)/cmath.sqrt(2) + (complex(0,1)*stheta*y2eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-y2mI + complex(0,1)*y2mR',
                  order = {'1':1})

GC_116 = Coupling(name = 'GC_116',
                  value = 'y2mI + complex(0,1)*y2mR',
                  order = {'1':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(complex(0,1)*y2mI)/cmath.sqrt(2) - y2mR/cmath.sqrt(2)',
                  order = {'1':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(complex(0,1)*y2mI)/cmath.sqrt(2) + y2mR/cmath.sqrt(2)',
                  order = {'1':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((ctheta*y2mI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y2mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(ctheta*y2mI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y2mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((stheta*y2mI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y2mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(stheta*y2mI)/cmath.sqrt(2) + (complex(0,1)*stheta*y2mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-y2tI + complex(0,1)*y2tR',
                  order = {'1':1})

GC_124 = Coupling(name = 'GC_124',
                  value = 'y2tI + complex(0,1)*y2tR',
                  order = {'1':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(complex(0,1)*y2tI)/cmath.sqrt(2) - y2tR/cmath.sqrt(2)',
                  order = {'1':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(complex(0,1)*y2tI)/cmath.sqrt(2) + y2tR/cmath.sqrt(2)',
                  order = {'1':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-((ctheta*y2tI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y2tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(ctheta*y2tI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y2tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-((stheta*y2tI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y2tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(stheta*y2tI)/cmath.sqrt(2) + (complex(0,1)*stheta*y2tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-y3eI + complex(0,1)*y3eR',
                  order = {'1':1})

GC_132 = Coupling(name = 'GC_132',
                  value = 'y3eI + complex(0,1)*y3eR',
                  order = {'1':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(complex(0,1)*y3eI)/cmath.sqrt(2) - y3eR/cmath.sqrt(2)',
                  order = {'1':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(complex(0,1)*y3eI)/cmath.sqrt(2) + y3eR/cmath.sqrt(2)',
                  order = {'1':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((ctheta*y3eI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y3eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(ctheta*y3eI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y3eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((stheta*y3eI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y3eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(stheta*y3eI)/cmath.sqrt(2) + (complex(0,1)*stheta*y3eR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-y3mI + complex(0,1)*y3mR',
                  order = {'1':1})

GC_140 = Coupling(name = 'GC_140',
                  value = 'y3mI + complex(0,1)*y3mR',
                  order = {'1':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(complex(0,1)*y3mI)/cmath.sqrt(2) - y3mR/cmath.sqrt(2)',
                  order = {'1':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(complex(0,1)*y3mI)/cmath.sqrt(2) + y3mR/cmath.sqrt(2)',
                  order = {'1':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((ctheta*y3mI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y3mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ctheta*y3mI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y3mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((stheta*y3mI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y3mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(stheta*y3mI)/cmath.sqrt(2) + (complex(0,1)*stheta*y3mR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-y3tI + complex(0,1)*y3tR',
                  order = {'1':1})

GC_148 = Coupling(name = 'GC_148',
                  value = 'y3tI + complex(0,1)*y3tR',
                  order = {'1':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(complex(0,1)*y3tI)/cmath.sqrt(2) - y3tR/cmath.sqrt(2)',
                  order = {'1':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(complex(0,1)*y3tI)/cmath.sqrt(2) + y3tR/cmath.sqrt(2)',
                  order = {'1':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((ctheta*y3tI)/cmath.sqrt(2)) - (ctheta*complex(0,1)*y3tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(ctheta*y3tI)/cmath.sqrt(2) - (ctheta*complex(0,1)*y3tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((stheta*y3tI)/cmath.sqrt(2)) + (complex(0,1)*stheta*y3tR)/cmath.sqrt(2)',
                  order = {'1':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(stheta*y3tI)/cmath.sqrt(2) + (complex(0,1)*stheta*y3tR)/cmath.sqrt(2)',
                  order = {'1':1})

