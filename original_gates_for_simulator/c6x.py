# -*- coding: utf-8 -*-

"""
c6x gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gate import c6z


class C6XGate(CompositeGate):
    """c6x gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, tgt, circ=None):
        """Create new c6x gate."""
        super().__init__("c6x", [], [ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, tgt], circ)
        self.h(tgt)
        self.c6z(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, tgt)
        self.h(tgt)

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.c6x(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4], self.art[5], self.art[6]))


def c6x(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, tgt):
    """Apply c6x to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.c6x((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(C6XGate(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, tgt, self))


QuantumCircuit.c6x = c6x
CompositeGate.c6x = c6x