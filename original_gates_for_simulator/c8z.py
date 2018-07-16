# -*- coding: utf-8 -*-

"""
c8z gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gates_for_simulator import cccx, ccccx, c5x, c6x, c7x
from math import pi


class C8ZGate(CompositeGate):
    """c8z gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, tgt, circ=None):
        """Create new c8z gate."""
        super().__init__("c8z", [], [ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, tgt], circ)
        self.c7x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8)
        self.cu1(-pi/2, ctl8, tgt)
        self.c7x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8)
        self.cu1(pi/2, ctl8, tgt)

        self.c6x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7)
        self.cu1(-pi/4, ctl7, tgt)
        self.c6x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7)
        self.cu1(pi/4, ctl7, tgt)

        self.c5x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6)
        self.cu1(-pi/8, ctl6, tgt)
        self.c5x(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6)
        self.cu1(pi/8, ctl6, tgt)

        self.ccccx(ctl1, ctl2, ctl3, ctl4, ctl5)
        self.cu1(-pi/16, ctl5, tgt)
        self.ccccx(ctl1, ctl2, ctl3, ctl4, ctl5)
        self.cu1(pi/16, ctl5, tgt)
        
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(-pi/32, ctl4, tgt)
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(pi/32, ctl4, tgt)

        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(-pi/64, ctl3, tgt)
        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(pi/64, ctl3, tgt)
        
        self.cx(ctl1, ctl2)
        self.cu1(-pi/128, ctl2, tgt)
        self.cx(ctl1, ctl2)
        self.cu1(pi/128, ctl2, tgt)

        self.cu1(pi/128, ctl1, tgt)


    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.c8z(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4], self.arg[5], self.arg[6], self.arg[7], self.arg[8]))


def c8z(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, tgt):
    """Apply c8z to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.c8z((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(C8ZGate(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, tgt, self))


QuantumCircuit.c8z = c8z
CompositeGate.c8z = c8z