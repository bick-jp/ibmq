# -*- coding: utf-8 -*-

"""
ccz gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import


class CCZGate(CompositeGate):
    """ccz gate."""

    def __init__(self, ctl1, ctl2, tgt, circ=None):
        """Create new ccz gate."""
        super().__init__("ccz", [], [ctl1, ctl2, tgt], circ)
        self.cx(ctl2, tgt)
        self.tdg(tgt)
        self.cx(ctl1, tgt)
        self.t(tgt)
        self.cx(ctl2, tgt)
        self.tdg(tgt)
        self.cx(ctl1, tgt)
        self.t(ctl2)
        self.t(tgt)
        self.cx(ctl1, ctl2)
        self.tdg(ctl2)
        self.cx(ctl1, ctl2)
        self.t(ctl1)


    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.ccz(self.arg[0], self.arg[1], self.arg[2]))


def ccz(self, ctl1, ctl2, tgt):
    """Apply ccz to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.ccz((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(CCZGate(ctl1, ctl2, tgt, self))


QuantumCircuit.ccz = ccz
CompositeGate.ccz = ccz