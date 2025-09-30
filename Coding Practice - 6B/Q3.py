a = int(input())

five_note = a // 5
remaining_amt = a - (5 * five_note) 
one_note = remaining_amt // 1

print(f"5:{five_note}")
print(f"1:{one_note}")