from __future__ import print_function
from utils import *

total_coding_score = 0.0;

q_nums = [2.2, 6, 7, 8]

for q_num in q_nums:
	pass_num = get_ok_num_perq("grades/Q%sres_.txt" % q_num)

	if q_num == 2.2:
		q1_score = pass_num * 5
		print("Item 2-2:", pass_num, "/", 2, "passed | score:", q1_score)
		total_coding_score += q1_score
	elif q_num == 6:
		cur_score = pass_num * 2
		print("Item 6:", pass_num, "/", 6, "passed | score:", cur_score)
		total_coding_score += cur_score
	elif q_num == 7:
		cur_score = pass_num * 2.5
		print("Item 7:", pass_num, "/", 2, "passed | score:", cur_score)
		total_coding_score += cur_score
	elif q_num == 8:
		cur_score = pass_num * 2.5
		print("Item 8:", pass_num, "/", 2, "passed | score:", cur_score)
		total_coding_score += cur_score
	else:
		raise ValueError('Wrong question number')


print("-----------------------------------------")
print("Phase 2: your score of coding section:", total_coding_score, " (part)")
print("-----------------------------------------")
	

	
	
