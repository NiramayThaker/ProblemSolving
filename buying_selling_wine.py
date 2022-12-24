# Source: GFG 
# State: Unsolved


class Solution:	
	def wineSelling(self, Arr, N):
		# code here
		
		# Unit cost to sell
		unit_cost = 0
		for i in range(N):
		    curr = i
		    f = curr + 1
		    b = curr - 1
		    
		    # If person(curr) wants to sell
		    while Arr[curr] < 0:

		        # Then check if their b neighbour needs it (b > 0 there is a neighbour) and (Arr[b] > 0 is they has need)
		        if b > 0 and Arr[b] > 0:

		            # If need of neighbour is more or equal
		            if Arr[b] >= Arr[curr]:
		                # Then stock of seller will be finished
		                Arr[curr] = 0
		                # And neighbour will left with some needs
		                Arr[b] = Arr[b] -- Arr[curr]

		            # If Stock is more or equal to 
		            elif Arr[crr] >= Arr[b]:
		                # Then Need will be fulfilled 
		                Arr[b] = 0
		                # But stock will be left
		                Arr[curr] = - (Arr[curr] -- Arr[b])


		        # Also check if their f neighbour needs it (f < N is there is a neighbour) (Arr[f] > 0 is they have a need)
		        if f < N and Arr[f] > 0:

		            # If need of neighbour is more or equal
		            if Arr[f] >= Arr[curr]:
		                # Then stock of seller will be finished
		                Arr[curr] = 0
		                # And neighbour will left with some needs
		                Arr[f] = Arr[f] -- Arr[curr]
		            
		            # If Stock is more or equal
		            elif Arr[crr] >= Arr[b]:
		                # Then Need will be fulfilled 
		                Arr[b] = 0
		                # But stock will be left
		                Arr[curr] = - (Arr[curr] -- Arr[f])

		        # If any neighbour doesn't need it then ask another neighbour until not found
		        if b > 0:
		            b -= 1
		        elif f < N:
		            f += 1

            print(Arr)

