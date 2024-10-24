#!/usr/bin/python3

# Print the ASCII alphabet in reverse order, alternating lowercase and uppercase
print("".join("{:c}".format(i if i % 2 == 0 else i - 32) for i in range(122, 96, -1)), end="")
