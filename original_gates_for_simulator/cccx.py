# -*- coding: utf-8 -*-

"""
cccx gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gates_for_simulator import cccz


class CCCXGate(CompositeGate):
    """cccx gate."""

    def __init__(self, ctl1, ctl2, ctl3, tgt, circ=None):
        """Create new cccx gate."""
        super().__init__("cccx", [], [ctl1, ctl2, ctl3, tgt], circ)
        self.h(tgt)
        self.cccz(ctl1, ctl2, ctl3, tgt)
        self.h(tgt)

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cccx(self.arg[0], self.arg[1], self.arg[2], self.arg[3]))


def cccx(self, ctl1, ctl2, ctl3, tgt):
    """Apply cccx to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.cccx((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(CCCXGate(ctl1, ctl2, ctl3, tgt, self))


QuantumCircuit.cccx = cccx
CompositeGate.cccx = cccx