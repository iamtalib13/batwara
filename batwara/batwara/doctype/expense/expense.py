# Copyright (c) 2025, Talib Sheikh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Expense(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from batwara.batwara.doctype.expense_split.expense_split import ExpenseSplit
		from frappe.types import DF

		amended_from: DF.Link | None
		amount: DF.Currency
		currency: DF.Link
		date: DF.Date | None
		description: DF.Data
		notes: DF.SmallText | None
		paid_by: DF.Link | None
		split: DF.Table[ExpenseSplit]
		split_method: DF.Literal["Equally", "Manual"]
	# end: auto-generated types
	
	def before_save(self):
		self.apply_split()

	def apply_split(self):
		"""Apply split to the expense"""
		if self.split_method == "Equally":
			self.calculate_split_equally()
		elif self.split_method == "Manual":
			pass	

	def calculate_split_equally(self):
		"""Calculate split equally among all participants"""
		if not self.split:
			return

		total_amount = self.amount
		num_participants = len(self.split)
		split_amount = total_amount / num_participants

		for split in self.split:
			split.amount = split_amount	