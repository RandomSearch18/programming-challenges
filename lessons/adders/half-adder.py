def half_adder(a: bool, b: bool):
    sum = a is not b
    carry = a and b
    return sum, carry


def full_adder(a: bool, b: bool, carry_in: bool):
    # Add a to b
    sum = a is not b
    carry_out = a and b

    # Add carry to sum
    sum = sum is not carry_in
    carry_out = sum and carry_in

    return sum, carry_out


# TESTS
# Half adder
assert half_adder(False, False) == (False, False)
assert half_adder(False, True) == (True, False)
assert half_adder(True, False) == (True, False)
assert half_adder(True, True) == (False, True)

# Full adder
assert full_adder(False, False, False) == (False, False)
assert full_adder(False, False, True) == (True, False)
assert full_adder(False, True, False) == (True, False)
assert full_adder(False, True, True) == (False, True)
assert full_adder(True, False, False) == (True, False)
assert full_adder(True, False, True) == (False, True)
assert full_adder(True, True, False) == (False, True)
assert full_adder(True, True, True) == (True, True)

print("Passed all tests :D")
