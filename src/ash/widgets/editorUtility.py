# ---------------------------------------------------------------------------------------------
#  Copyright (c) Akash Nag. All rights reserved.
#  Licensed under the MIT License. See LICENSE.md in the project root for license information.
# ---------------------------------------------------------------------------------------------

# This module is a helper class for Editor

from ash.widgets import *
from ash.widgets.utils.formatting import *
from ash.widgets.utils.utils import *

class EditorUtility:
	def __init__(self, ed):
		self.ed = ed

	# delete the selected text
	def delete_selected_text(self):
		start, end = self.ed.get_selection_endpoints()
		del_text = ""

		if(start.y == end.y):
			sel_len = end.x - start.x
			del_text = self.ed.lines[start.y][start.x:end.x]
			self.ed.lines[start.y] = self.ed.lines[start.y][0:start.x] + self.ed.lines[start.y][end.x:]			
		else:
			del_text = self.ed.lines[start.y][start.x:] + self.ed.newline
						
			# delete entire lines between selection start and end
			lc = end.y - start.y - 1
			while(lc > 0):
				del_text += self.ed.lines[start.y+1] + self.ed.newline
				self.ed.lines.pop(start.y + 1)
				self.ed.curpos.y -= 1
				end.y -= 1
				lc -= 1

			# delete a portion of the selection start line
			self.ed.lines[start.y] = self.ed.lines[start.y][0:start.x]

			# delete a portion of the selection end line
			del_text += self.ed.lines[end.y][0:end.x]
			self.ed.lines[end.y] = self.ed.lines[end.y][end.x:]

			# bring the selection end line up towards the end of the selection start line
			text = self.ed.lines[end.y]
			self.ed.lines.pop(end.y)
			self.ed.curpos.y = start.y
			self.ed.curpos.x = len(self.ed.lines[start.y])
			self.ed.lines[start.y] += text
		
		# turn off selection mode
		self.ed.selection_mode = False
		self.ed.curpos.x = max(self.ed.curpos.x, 0)
		self.ed.curpos.x = min(self.ed.curpos.x, len(self.ed.lines[self.ed.curpos.y]))
		self.ed.save_status = False
		return del_text

	# returns the selected text
	def get_selected_text(self):
		start, end = self.ed.get_selection_endpoints()
		sel_text = ""

		if(start.y == end.y):
			sel_len = end.x - start.x
			sel_text = self.ed.lines[start.y][start.x:end.x]
		else:
			sel_text = self.ed.lines[start.y][start.x:] + self.ed.newline
			for row in range(start.y+1, end.y):
				sel_text = self.ed.lines[row] + self.ed.newline
			sel_text += self.ed.lines[end.y][0:end.x]

		return sel_text

	# increase indent of selected lines
	def shift_selection_right(self):
		start, end = self.ed.get_selection_endpoints()
		for i in range(start.y, end.y+1):
			self.ed.lines[i] = "\t" + self.ed.lines[i]
		self.ed.curpos.x += 1
		self.ed.sel_start.x += 1
		self.ed.sel_end.x += 1
		self.ed.save_status = False

	# decrease indent of selected lines
	def shift_selection_left(self):
		start, end = self.ed.get_selection_endpoints()

		# check if all lines have at least 1 indent
		has_tab_in_all = True
		for i in range(start.y, end.y+1):
			if(not self.ed.lines[i].startswith("\t")):
				has_tab_in_all = False
				break

		# decrease indent only if all lines are indented
		if(has_tab_in_all):
			for i in range(start.y, end.y+1):
				self.ed.lines[i] = self.ed.lines[i][1:]
			self.ed.curpos.x -= 1
			self.ed.sel_start.x -= 1
			self.ed.sel_end.x -= 1
			self.ed.save_status = False

	# returns the block of leading whitespaces on a given line 
	def get_leading_whitespaces(self, line_index):
		text = self.ed.lines[line_index]
		nlen = len(text)
		ws = ""
		for i in range(nlen):
			if(text[i] == " " or text[i] == "\t"): 
				ws += text[i]
			else:
				break
		return ws
	
	# checks if line_index is within the text that was selected
	def is_in_selection(self, line_index):
		if(self.ed.selection_mode):
			if(is_start_before_end(self.ed.sel_start, self.ed.sel_end)):
				return(True if (line_index >= self.ed.sel_start.y and line_index <= self.ed.sel_end.y) else False)
			else:
				return(True if (line_index >= self.ed.sel_end.y and line_index <= self.ed.sel_start.y) else False)
		else:
			return False

	# returns the selection endpoints in the correct order
	def get_selection_endpoints(self):
		forward_sel = is_start_before_end(self.ed.sel_start, self.ed.sel_end)
		if(forward_sel):
			start = copy.copy(self.ed.sel_start)
			end = copy.copy(self.ed.sel_end)
		else:
			start = copy.copy(self.ed.sel_end)
			end = copy.copy(self.ed.sel_start)
		return (start, end)

	# count lines and SLOC
	def get_loc(self):
		nlines = len(self.ed.lines)
		sloc = 0
		
		for x in self.ed.lines:
			if(len(x.strip()) == 0):
				sloc += 1

		return (nlines, nlines - sloc)

	# get file size
	def get_file_size(self):
		if(self.ed.has_been_allotted_file):
			return get_file_size(self.ed.filename)
		else:
			return "0 bytes"

	# implements search
	def find(self, str):
		pass

	# replaces the first occurrence (after last find/replace operation)
	def find_and_replace(self, strf, strr):
		pass