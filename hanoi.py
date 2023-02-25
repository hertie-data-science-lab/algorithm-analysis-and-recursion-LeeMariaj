# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Hannah
"""

def TOH(n_disk, rod_begin, rod_final, rod_auxiliary):
    if n_disk == 1: # Base case, where we move our last disk to our final rod
        print("Move Disk", n_disk, "from Rod", rod_begin, "to Rod", rod_final)
    else: # Rest of cases
        # 1. We make it solve the game for all smaller disks, but placing them in the auxiliary rod
        TOH(n_disk-1, rod_begin, rod_auxiliary, rod_final)
        # 2. It will take the biggest disk, and move it to the final position
        print("Move Disk", n_disk, "from Rod", rod_begin, "to Rod", rod_final)
        # 3. We make it solve the game for all smaller disks again, placing them now in the final rod
        TOH(n_disk - 1, rod_auxiliary, rod_final, rod_begin)

# Example with 3 disks
TOH(3, "A", "C", "B")