# -*- coding: utf-8 -*-

"""
ccccz gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gates_for_simulator import cccx
from math import pi


class CCCCZGate(CompositeGate):
    """ccccz gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, tgt, circ=None):
        """Create new ccccz gate."""
        super().__init__("ccccz", [], [ctl1, ctl2, ctl3, ctl4, tgt], circ)
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(-pi/2, ctl4, tgt)
        self.cccx(ctl1, ctl2, ctl3, ctl4)
        self.cu1(pi/2, ctl4, tgt)

        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(-pi/4, ctl3, tgt)
        self.ccx(ctl1, ctl2, ctl3)
        self.cu1(pi/4, ctl3, tgt)

        self.cx(ctl1, ctl2)
        self.cu1(-pi/8, ctl2, tgt)
        self.cx(ctl1, ctl2)
        self.cu1(pi/8, ctl2, tgt)

        self.cu1(pi/8, ctl2, tgt)


    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.ccccz(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4]))


def ccccz(self, ctl1, ctl2, ctl3, ctl4, tgt):
    """Apply ccccz to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.ccccz((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(CCCCZGate(ctl1, ctl2, ctl3, ctl4, tgt, self))


QuantumCircuit.ccccz = ccccz
CompositeGate.ccccz = ccccz