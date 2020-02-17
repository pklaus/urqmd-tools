#!/usr/bin/env python

""" UrQMD F14 File Parser """

import argparse
import math

# if you need multithreading support:
#from cached_property import threaded_cached_property as cached_property
from cached_property import cached_property

class Particle(object):

    def __init__(self, properties):
        self._properties = list(properties)
        assert len(self._properties) == 15
        for i in (9, 10, 11, 12, 13, 14):
            self._properties[i] = int(self._properties[i])
        for i in (0, 1, 2, 3, 4, 5, 6, 7, 8):
            self._properties[i] = float(self._properties[i])
        """
        pvec: r0 rx ry rz p0 px py pz m ityp 2i3 chg lcl# ncl or

        t    eigentime of particle in fm/c
        r_x  x coordinate in fm
        r_y  y coordinate in fm
        r_z  z coordinate in fm
        E    energy of particle in GeV
        p_x  x momentum component in GeV
        p_y  y momentum component in GeV
        p_z  z momentum component in GeV
        m    mass of particle in GeV
        ityp particle-ID
        2i3  isospin z-projection (doubled)
        chg  chargeofparticle
        lcl# index of last collision partner
        ncl  number of collisions
        or   history information (parent process)
        """

        # precalculate expensive values:
        #self.mT
        self.m0
        self.beta
        self.beta3
        self.gamma
        self.w
        self.y

    @property
    def id(self):
        return self._properties[9]

    @property
    def time(self):
        return self._properties[0]

    @property
    def rx(self):
        return self._properties[1]

    @property
    def ry(self):
        return self._properties[2]

    @property
    def rz(self):
        return self._properties[3]

    @property
    def E(self):
        return self._properties[4]

    @property
    def px(self):
        return self._properties[5]

    @property
    def py(self):
        return self._properties[6]

    @property
    def pz(self):
        return self._properties[7]

    @property
    def chg(self):
        return self._properties[11]

    @property
    def m0(self):
        return self.m / self.gamma
        #return math.sqrt(math.sqrt(self.px**2 + self.py**2 + self.pz**2)**2 - self.E**2)

    @property
    def beta(self):
        return math.tanh(self.w)

    @cached_property
    def beta3(self):
        return tuple(p_i/self.E for p_i in (self.px, self.py, self.pz))

    @cached_property
    def gamma(self):
        return math.cosh(self.w)

    @property
    def m(self):
        return self._properties[8]

    @cached_property
    def mT(self):
        return math.sqrt(self.m0**2 + self.px**2 + self.py**2)

    @property
    def ncl(self):
        return self._properties[13]

    def __str__(self):
        fmt = "Particle(t={self.time}, x={self.rx}, y={self.ry}, z={self.rz}, E={self.E}, px={self.px}, py={self.py}, pz={self.pz}"
        return fmt.format(self=self)

    def __repr__(self):
        return self.__str__()

    @property
    def w(self):
        """ rapidity (relativistic definition) """
        p_mag = math.sqrt(self.px**2 + self.py**2 + self.pz**2)
        return .5 * math.log((self.E + p_mag)/(self.E - p_mag))

    @property
    def y(self):
        """ rapidity (experimental particle physics definition - along beam axis z)"""
        return .5 * math.log((self.E + self.pz)/(self.E - self.pz))

    def boost(self, boost_beta):
        """ Lorentz boost in positive z direction """
        boost_gamma = 1.0 / math.sqrt(1-boost_beta**2)
        time = boost_gamma * (self.time + boost_beta * self.rz)
        rz =   boost_gamma * (self.rz +   boost_beta * self.time)
        E =    boost_gamma * (self.E +    boost_beta * self.pz)
        pz =   boost_gamma * (self.pz +   boost_beta * self.E)
        self._properties[0] = time
        self._properties[3] = rz
        self._properties[4] = E
        self._properties[7] = pz

class F14_Parser(object):

    def __init__(self, data_file):
        self.data_file = data_file

    def get_events(self):
        new_event = False
        event = None
        for line in self.data_file:
            parts = line.split()
            if not len(parts): continue
            if parts[0] == 'UQMD': new_event = True
            if new_event:
                if event: yield event
                event = dict()
                event['particle_properties'] = []
                new_event = False
            if parts[0] == 'event#': event['id'] = int(parts[1])
            if len(parts) == 15:
                event['particle_properties'].append(parts)
        if event: yield event


def main():
    parser = argparse.ArgumentParser(description='Read a config file.')
    parser.add_argument('urqmd_file', metavar='URQMD_FILE', type=argparse.FileType('r'), help="Must be of type .f14")
    args = parser.parse_args()

    for event in F14_Parser(args.urqmd_file).get_events():
        print("Event #{} containing {} particles".format(event['id'], len(event['particle_properties'])))


if __name__ == "__main__":
    main()
