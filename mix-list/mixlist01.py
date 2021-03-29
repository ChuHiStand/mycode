# #!/usr/bin/env python3

# create a list
my_list = ["192.168.0.5", 5060, "UP"]

# display first item of list
print("The first item in the list (IP): " + my_list[0])

# display second item of list
print("The second item in the list (port): " + str(my_list[1]))

# display third item of list
print("The last item in the list (state): " + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]


# When I ssh into IP addresses 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.
ssh = new_list[-1]
portOne = str(new_list[0])
portTwo = new_list[1]
portThree = str(new_list[2])
ipAddressOne = new_list[3]
ipAddressTwo = new_list[4]
print("When I ssh into an IP addresses " + ipAddressOne + " or " + ipAddressTwo + " I am unable to ping ports " + portOne
      + ", " + portTwo + ", " + portThree)



