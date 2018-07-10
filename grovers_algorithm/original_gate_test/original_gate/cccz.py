# -*- coding: utf-8 -*-

"""
cccz gate.
"""
from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import
from original_gate import csdg, cs, ctdg, ct


class CCCZGate(CompositeGate):
    """cccz gate."""

    def __init__(self, ctl1, ctl2, ctl3, tgt, circ=None):
        """Create new cccz gate."""
        super().__init__("cccz", [], [ctl1, ctl2, ctl3, tgt], circ)
        self.ccx(ctl1, ctl2, ctl3)
        self.csdg(ctl3, tgt)
        self.ccx(ctl1, ctl2, ctl3)
        self.cs(ctl3, tgt)
        self.cx(ctl1, ctl2)
        self.ctdg(ctl2, tgt)
        self.cx(ctl1, ctl2)
        self.ct(ctl2, tgt)
        self.ct(ctl1, tgt)

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cccz(self.arg[0], self.arg[1], self.arg[2], self.arg[3]))


def cccz(self, ctl1, ctl2, ctl3, tgt):
    """Apply cccz to circuit."""
    """Comment out since don't know what to do"""
    """
    if isinstance(ctl1, QuantumRegister) and \
       isinstance(ctl2, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and \
       len(ctl1) == len(ctl2) and len(ctl1) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl1.size):
            instructions.add(self.cccz((ctl1, i), (ctl2, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl1)
    self._check_qubit(ctl2)
    self._check_qubit(tgt)
    self._check_dups([ctl1, ctl2, tgt])
    """
    return self._attach(CCCZGate(ctl1, ctl2, ctl3, tgt, self))


QuantumCircuit.cccz = cccz
CompositeGate.cccz = cccz