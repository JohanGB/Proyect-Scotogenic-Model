# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Wed 27 Nov 2024 22:04:04


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

ne = Particle(pdg_code = 12,
              name = 'ne',
              antiname = 'Ne',
              spin = 2,
              color = 1,
              mass = Param.Mnue,
              width = Param.ZERO,
              texname = 'ne',
              antitexname = 'Ne',
              charge = 0,
              GhostNumber = 0)

Ne = ne.anti()

nm = Particle(pdg_code = 14,
              name = 'nm',
              antiname = 'Nm',
              spin = 2,
              color = 1,
              mass = Param.Mnum,
              width = Param.ZERO,
              texname = 'nm',
              antitexname = 'Nm',
              charge = 0,
              GhostNumber = 0)

Nm = nm.anti()

nl = Particle(pdg_code = 16,
              name = 'nl',
              antiname = 'Nl',
              spin = 2,
              color = 1,
              mass = Param.Mnut,
              width = Param.ZERO,
              texname = 'nl',
              antitexname = 'Nl',
              charge = 0,
              GhostNumber = 0)

Nl = nl.anti()

e = Particle(pdg_code = 11,
             name = 'e',
             antiname = 'E',
             spin = 2,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'e',
             antitexname = 'E',
             charge = -1,
             GhostNumber = 0)

E = e.anti()

m = Particle(pdg_code = 13,
             name = 'm',
             antiname = 'M',
             spin = 2,
             color = 1,
             mass = Param.MM,
             width = Param.ZERO,
             texname = 'm',
             antitexname = 'M',
             charge = -1,
             GhostNumber = 0)

M = m.anti()

l = Particle(pdg_code = 15,
             name = 'l',
             antiname = 'L',
             spin = 2,
             color = 1,
             mass = Param.MTA,
             width = Param.ZERO,
             texname = 'l',
             antitexname = 'L',
             charge = -1,
             GhostNumber = 0)

L = l.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'U',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'U',
             charge = 2/3,
             GhostNumber = 0)

U = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'C',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'C',
             charge = 2/3,
             GhostNumber = 0)

C = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 'T',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 'T',
             charge = 2/3,
             GhostNumber = 0)

T = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'D',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'D',
             charge = -1/3,
             GhostNumber = 0)

D = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 'S',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 'S',
             charge = -1/3,
             GhostNumber = 0)

S = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'B',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'B',
             charge = -1/3,
             GhostNumber = 0)

B = b.anti()

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.ZERO,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.ZERO,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 9000005,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1)

ghG__tilde__ = ghG.anti()

P__tilde__N1 = Particle(pdg_code = 9000006,
                        name = '~N1',
                        antiname = '~N1',
                        spin = 2,
                        color = 1,
                        mass = Param.mN1,
                        width = Param.WN1,
                        texname = '~N1',
                        antitexname = '~N1',
                        charge = 0,
                        GhostNumber = 0)

P__tilde__N2 = Particle(pdg_code = 9000007,
                        name = '~N2',
                        antiname = '~N2',
                        spin = 2,
                        color = 1,
                        mass = Param.mN2,
                        width = Param.WN2,
                        texname = '~N2',
                        antitexname = '~N2',
                        charge = 0,
                        GhostNumber = 0)

P__tilde__N3 = Particle(pdg_code = 9000008,
                        name = '~N3',
                        antiname = '~N3',
                        spin = 2,
                        color = 1,
                        mass = Param.mN3,
                        width = Param.WN3,
                        texname = '~N3',
                        antitexname = '~N3',
                        charge = 0,
                        GhostNumber = 0)

h = Particle(pdg_code = 25,
             name = 'h',
             antiname = 'h',
             spin = 1,
             color = 1,
             mass = Param.mH,
             width = Param.WH,
             texname = 'h',
             antitexname = 'h',
             charge = 0,
             GhostNumber = 0)

P__tilde__eta__plus__ = Particle(pdg_code = 9000009,
                                 name = '~eta+',
                                 antiname = '~eta-',
                                 spin = 1,
                                 color = 1,
                                 mass = Param.metach,
                                 width = Param.Wetach,
                                 texname = '~eta+',
                                 antitexname = '~eta-',
                                 charge = 1,
                                 GhostNumber = 0)

P__tilde__eta__minus__ = P__tilde__eta__plus__.anti()

P__tilde__etaI = Particle(pdg_code = 9000010,
                          name = '~etaI',
                          antiname = '~etaI',
                          spin = 1,
                          color = 1,
                          mass = Param.metaI,
                          width = Param.WetaI,
                          texname = '~etaI',
                          antitexname = '~etaI',
                          charge = 0,
                          GhostNumber = 0)

P__tilde__phi2 = Particle(pdg_code = 9000011,
                          name = '~phi2',
                          antiname = '~phi2',
                          spin = 1,
                          color = 1,
                          mass = Param.mphi2,
                          width = Param.Wphi2,
                          texname = '~phi2',
                          antitexname = '~phi2',
                          charge = 0,
                          GhostNumber = 0)

P__tilde__phi1 = Particle(pdg_code = 9000012,
                          name = '~phi1',
                          antiname = '~phi1',
                          spin = 1,
                          color = 1,
                          mass = Param.mphi1,
                          width = Param.Wphi1,
                          texname = '~phi1',
                          antitexname = '~phi1',
                          charge = 0,
                          GhostNumber = 0)

