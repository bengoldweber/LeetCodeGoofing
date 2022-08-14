
import cProfile as profile

from collections import deque

# In outer section of code
pr = profile.Profile()
pr.disable()

pr.enable()

class Solution:
	def addTwoNumbers(self, l1, l2):
		l1.reverse()
		l2.reverse()
		l1Grp = sum(d * 10 ** i for i, d in enumerate(l1))
		l2Grp = sum(d * 10 ** i for i, d in enumerate(l2))
		res = [int(x) for x in str(l1Grp + l2Grp)]
		return res[::-1]

	def reverseList(self, list):
		# initialize variables
		previous = None  # `previous` initially points to None
		current = list.head  # `current` points at the first element
		following = current.next  # `following` points at the second element

		# go till the last element of the list
		while current:
			current.next = previous  # reverse the link
			previous = current  # move `previous` one step ahead
			current = following  # move `current` one step ahead
			if following:  # if this was not the last element
				following = following.next  # move `following` one step ahead

		list.head = previous


l1 = deque([9, 9, 9, 9, 9, 9, 9])
l2 = deque([9, 9, 9, 9])
test = deque([7, 0, 8])
s = Solution.addTwoNumbers(Solution, l1, l2)
print(s)

pr.disable()
pr.dump_stats('profile.pstat')
