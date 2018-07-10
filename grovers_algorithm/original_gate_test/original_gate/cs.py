# -*- coding: utf-8 -*-

"""
cs gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import


class CSGate(CompositeGate):
    """cs gate."""

    def __init__(self, ctl, tgt, circ=None):
        """Create new cs gate."""
        super().__init__("cs", [], [ctl, tgt], circ)
        self.cx(ctl, tgt)
        self.tdg(tgt)
        self.cx(ctl, tgt)
        self.t(ctl)
        self.t(tgt)

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cs(self.arg[0], self.arg[1]))


def cs(self, ctl, tgt):
    """Apply cs to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.cs((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(CSGate(ctl, tgt, self))


QuantumCircuit.cs = cs
CompositeGate.cs = cs