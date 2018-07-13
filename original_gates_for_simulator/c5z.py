# -*- coding: utf-8 -*-

"""
c5z gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gate import cccx, ccccx
from math import pi


class C5ZGate(CompositeGate):
    """c5z gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, ctl5, tgt, circ=None):
        """Create new c5z gate."""
        super().__init__("c5z", [], [ctl1, ctl2, ctl3, ctl4, ctl5, tgt], circ)
        self.ccccx(ctl1, ctl2, ctl3, ctl4, ctl5)
        self.cu1(-pi/2, ctl5, tgt)
        self.ccccx(ctl1, ctl2, ctl3, ctl4, ctl5)
        self.cu1(pi/2, ctl5, tgt)

        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(-pi/4, ctl4, tgt)
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(pi/4, ctl4, tgt)

        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(-pi/8, ctl3, tgt)
        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(pi/8, ctl3, tgt)
        
        self.cx(ctl1, ctl2)
        self.cu1(-pi/16, ctl2, tgt)
        self.cx(ctl1, ctl2)
        self.cu1(pi/16, ctl2, tgt)
        
        self.cu1(pi/16, ctl1, tgt)


    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.c5z(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4], self.art[5]))


def c5z(self, ctl1, ctl2, ctl3, ctl4, ctl5, tgt):
    """Apply c5z to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.c5z((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(C5ZGate(ctl1, ctl2, ctl3, ctl4, ctl5, tgt, self))


QuantumCircuit.c5z = c5z
CompositeGate.c5z = c5z