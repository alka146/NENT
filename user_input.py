import re

class Input:


    def ReadEnv(self):
        while True:
            env = raw_input("Please enter the Environment you want to have the template for:\n")
            if env.lower() not in ('development', 'experimental', 'production'):
                print("Not an appropriate choice. Valid choices are Development, Experimental or Production")
            else:
                break
        print("You have entered")
        print env
        print("Press Enter to go ahead.\n")
        raw_input ()
        return env
    
    def ReadEnv(self, env):
            if env.lower() not in ('development', 'experimental', 'production'):
                print("Not an appropriate choice. Valid choices are Development, Experimental or Production")
                env = INVALID
            else:
                print("You have entered")
                print env
                print("Press Enter to go ahead.\n")
                raw_input ()
            return env
    
    def ReadCIDR(self):
        while True:
            cidr = raw_input("Please enter the CIDR you want to have for the VPC:\n")
            if re.match("^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$", cidr) is None:
                print("Not an appropriate entry. Please enter a valid CIDR")
            else:
                break
        print("You have entered")
        print cidr
        print("Press Enter to go ahead.\n")
        raw_input ()
        return cidr
        
    def ReadCIDR(self, cidr):
            if re.match("^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$", cidr) is None:
                print("Not an appropriate entry. Please enter a valid CIDR")
                cidr = INVALID
            else:
                print("You have entered")
                print cidr
                print("Press Enter to go ahead.\n")
                raw_input ()
            return cidr
