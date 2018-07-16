# -*- coding: utf-8 -*-

"""
c7x gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gates_for_simulator import c7z


class C7XGate(CompositeGate):
    """c7x gate."""

    def __init__(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt, circ=None):
        """Create new c7x gate."""
        super().__init__("c7x", [], [ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt], circ)
        self.h(tgt)
        self.c7z(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt)
        self.h(tgt)        

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.c7x(self.arg[0], self.arg[1], self.arg[2], self.arg[3], self.arg[4], self.arg[5], self.arg[6], self.arg[7]))


def c7x(self, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt):
    """Apply c7x to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.c7x((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(C7XGate(ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, tgt, self))


QuantumCircuit.c7x = c7x
CompositeGate.c7x = c7x