from opensquirrel.ir import Bit, Measure, Qubit, named_measurement


@named_measurement
def measure(q: Qubit, b: Bit) -> Measure:
    return Measure(qubits=[q.index, ], bit=b, axis=(0, 0, 1))
    #return Measure(qubits=[q,], bit=b, axis=(0, 0, 1))


@named_measurement
def measure_z(q: Qubit, b: Bit) -> Measure:
    return Measure(qubits=[q,], bit=b, axis=(0, 0, 1))


default_measurement_set = [measure_z, measure]
