"""
https://urqmd.org/en/particle-ids/
"""

import attr

@attr.s(frozen=True)
class ParticleID():
    id = attr.ib(type=int)
    name = attr.ib(type=str)

BARYONS = [
  ParticleID(*params) for params in [
    ( 1,  '0.938 N'),
    ( 2,  '1.440 N*'),
    ( 3,  '1.520'),
    ( 4,  '1.535'),
    ( 5,  '1.650'),
    ( 6,  '1.675'),
    ( 7,  '1.680'),
    ( 8,  '1.700'),
    ( 9,  '1.710'),
    (10,  '1.720'),
    (11,  '1.900'),
    (12,  '1.990'),
    (13,  '2.040'),
    (14,  '2.190'),
    (15,  '2.220'),
    (16,  '2.250'),
    (17,  '1.232 Δ (Delta)'),
    (18,  '1.600 Δ* (Delta*)'),
    (19,  '1.620'),
    (20,  '1.700'),
    (21,  '1.900'),
    (22,  '1.905'),
    (23,  '1.910'),
    (24,  '1.920'),
    (25,  '1.930'),
    (26,  '1.950'),
    (27,  '1.116 Λ (Lambda)'),
    (28, ' Λ* (Lambda*) 28'),
    (29, ' Λ* (Lambda*) 29'),
    (30, ' Λ* (Lambda*) 30'),
    (31, ' Λ* (Lambda*) 31'),
    (32, ' Λ* (Lambda*) 32'),
    (33, ' Λ* (Lambda*) 33'),
    (34, ' Λ* (Lambda*) 34'),
    (35, ' Λ* (Lambda*) 35'),
    (36, ' Λ* (Lambda*) 36'),
    (37, ' Λ* (Lambda*) 37'),
    (38, ' Λ* (Lambda*) 38'),
    (39, ' Λ* (Lambda*) 39'),
    (40,  '1.192 Σ (Sigma)'),
    (41,  'Σ* (Sigma*) 41'),
    (42,  'Σ* (Sigma*) 42'),
    (43,  'Σ* (Sigma*) 43'),
    (44,  'Σ* (Sigma*) 44'),
    (45,  'Σ* (Sigma*) 45'),
    (46,  'Σ* (Sigma*) 46'),
    (47,  'Σ* (Sigma*) 47'),
    (48,  'Σ* (Sigma*) 48'),
    (49,  '1.315 Ξ (Xi)'),
    (50,  'Ξ* (Xi*) 50'),
    (51,  'Ξ* (Xi*) 51'),
    (52,  'Ξ* (Xi*) 52'),
    (53,  'Ξ* (Xi*) 53'),
    (54,  'Ξ* (Xi*) 54'),
    (55,  '1.672 Ω (Omega)'),
  ]
]
# Also add all anti baryons to the list:
BARYONS += [ParticleID(id=-p.id, name='anti ' + p.name) for p in BARYONS]

MESONS = [
  ParticleID(*params) for params in [
    (100, 'γ (gamma)'),
    (101, 'π (pion)'),
    (102, 'η (eta)'),
    (103, 'ω(782) (omega)'),
    (104, 'ρ(770) (rho)'),
    (105, 'f0(980)'),
    (106, 'K (K+, K0)'),
    (107, 'η′(958) (eta\')'),
    (108, 'K*(892)'),
    (109, 'Φ(1020) (phi)'),
    (110, 'K0*(1430)'),
    (111, 'a0(980)'),
    (112, 'f0(1370)'),
    (113, 'K1(1270)'),
    (114, 'a1(1260)'),
    (115, 'f1(1285)'),
    (116, 'f1(1510)'),
    (117, 'K2*(1430)'),
    (118, 'a2(1320)'),
    (119, 'f2(1270)'),
    (120, 'f2′(1525) (f2\')'),
    (121, 'K1(1400)'),
    (122, 'b1(1235)'),
    (123, 'h1(1170)'),
    (124, 'h1′(1380) (h1\')'),
    (125, 'K*(1410)'),
    (126, 'ρ(1465) (rho)'),
    (127, 'ω(1419) (omega)'),
    (128, 'Φ(1680) (phi)'),
    (129, 'K*(1680)') ,
    (130, 'ρ(1700) (rho)'),
    (131, 'ω(1662) (omega)'),
    (132, 'Φ(1900) (phi)'),
    (133, 'D(1866)')  ,
    (134, 'D*(2010)') ,
    (135, 'J/ψ(3097) (J/Psi)'),
    (136, 'χc(3511)') ,
    (137, 'ψ\'(3686)'),
    (138, 'Ds(1986)') ,
    (139, 'D*s(2112)'),
  ]
]
# Also add mesons with strangeness S=-1 to the list:
MESONS += [ParticleID(id=-p.id, name=p.name+' (S=-1)') for p in MESONS]

MULTIPLETS = [
  ParticleID(*params) for params in [
    # Pseudoscalar JPC=0-+
    (101, 'π'),
    (106, 'K'),
    (102, 'η'),
    (107, 'η′(958)'),
    # Vector JPC=1--
    (104, 'ρ(770)'),
    (108, 'K*(892)'),
    (103, 'ω(782)'),
    (109, 'Φ(1020)'),
    # Scalar JPC=0++
    (111, 'a0(980)'),
    (110, 'K0*(1430)'),
    (112, 'f0(980)'),
    (105, 'f0(1370) '),
    # Pseudovector JPC=1+-
    (114, 'a1(1260)'),
    (113, 'K1*(1270)'),
    (115, 'f1(1285)'),
    (116, 'f1(1510) '),
    # Tensor JPC=2++
    (118, 'a2(1320)'),
    (117, 'K2*(1430)'),
    (119, 'f2(1270)'),
    (120, 'f2′(1525)'),
    # Pseudovector JPC=1+-
    (122, 'b1(1235)'),
    (121, 'K1(1400)'),
    (123, 'h1(1170)'),
    (124, 'h1′(1380)'),
    # Vector* JPC=1--
    (126, 'ρ(1465)'),
    (125, 'K*(1410)'),
    (127, 'ω(1419)'),
    (128, 'Φ(1680)'),
    # Vector* JPC=1--
    (130, 'ρ(1700)'),
    (129, 'K*(1680)'),
    (131, 'ω(1662)'),
    (132, 'Φ(1900)'),
  ]
]

ALL = list(set(BARYONS + MESONS))
# make sure our PIDs are all unique
assert len(set(ALL)) == len(ALL)

ALL_SORTED = sorted(ALL, key=lambda pid: pid.id)

LOOKUP_TABLE = {pid.id: pid for pid in ALL}

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('pid', nargs='?', type=int)
    args = parser.parse_args()
    if args.pid:
        pid = LOOKUP_TABLE[args.pid]
        print(pid)
    else:
        for p in ALL_SORTED:
            print(p.id, p.name)

if __name__ == "__main__":
    main()
