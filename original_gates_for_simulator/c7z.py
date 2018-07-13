# -*- coding: utf-8 -*-

"""
c7z gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gate import cccx, ccccx, c5x, c6x
from math import pi


class C7ZGate(CompositeGate):
    """c7z gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt, circ=None):
        """Create new c7z gate."""
        super().__init__("c7z", [], [ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt], circ)
        self.c6x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7)
        self.cu1(-pi/2, ctl7, tgt)
        self.c6x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7)
        self.cu1(pi/2, ctl7, tgt)

        self.c5x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6)
        self.cu1(-pi/4, ctl6, tgt)
        self.c5x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6)
        self.cu1(pi/4, ctl6, tgt)

        self.ccccx(ctl1, ctl2, ctl3, ctl4, ctl5)
        self.cu1(-pi/8, ctl5, tgt)
        self.ccccx(ctl1, ctl2, ctl3, ctl4, ctl5)
        self.cu1(pi/8, ctl5, tgt)
        
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(-pi/16, ctl4, tgt)
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(pi/16, ctl4, tgt)

        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(-pi/32, ctl3, tgt)
        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(pi/32, ctl3, tgt)
        
        self.cx(ctl1, ctl2)
        self.cu1(-pi/64, ctl2, tgt)
        self.cx(ctl1, ctl2)
        self.cu1(pi/64, ctl2, tgt)

        self.cu1(pi/64, ctl1, tgt)


    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.c7z(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4], self.art[5], self.art[6], self.art[7]))


def c7z(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt):
    """Apply c7z to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.c7z((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(C7ZGate(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt, self))


QuantumCircuit.c7z = c7z
CompositeGate.c7z = c7z