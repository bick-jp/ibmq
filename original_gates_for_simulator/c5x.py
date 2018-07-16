# -*- coding: utf-8 -*-

"""
c5x gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gates_for_simulator import c5z


class C5XGate(CompositeGate):
    """c5x gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, ctl5, tgt, circ=None):
        """Create new c5x gate."""
        super().__init__("c5x", [], [ctl1, ctl2, ctl3, ctl4, ctl5, tgt], circ)
        self.h(tgt)
        self.c5z(ctl1, ctl2, ctl3, ctl4, ctl5, tgt)
        self.h(tgt)

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.c5x(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4], self.arg[5]))


def c5x(self, ctl1, ctl2, ctl3, ctl4, ctl5, tgt):
    """Apply c5x to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.c5x((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(C5XGate(ctl1, ctl2, ctl3, ctl4, ctl5, tgt, self))


QuantumCircuit.c5x = c5x
CompositeGate.c5x = c5x