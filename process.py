class rev_gen_proc:
	def __init__(self, purpose, tax_status, avg_rev, total_stores, total_slaves):
		self.purpose = purpose
		self.tax_status = tax_status
		self.avg_rev = avg_rev
		self.total_slaves = total_slaves
	

#examples

lowes = rev_gen_proc('materials', 'nonexempt', '$68B', 2200, 3000000)
st_joseph = rev_gen_proc('doctrine', 'exempt', '$8T', 112, 40)
geico = rev_gen_proc('fear', 'nonexempt', '$1B', 40, 600)
mercy = rev_gen_proc('health', 'nonexempt', '$334M', 28, 700)
