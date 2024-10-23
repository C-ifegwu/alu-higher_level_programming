#!/usr/bin/python3

# Print the ASCII lowercase alphabet in one loop without a newline at the end
print("".join("{:c}".format(i) for i in range(97, 123)), end="")
