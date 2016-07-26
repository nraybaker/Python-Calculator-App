# File Name: calculator.py

from __future__ import division
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout

class Calculator(FloatLayout):
	def back_one(self, s):
		if ('=' in self.display.text) | (self.display.text == 'Error'):
			self.display.text = ''
		else:
			self.display.text = s[:-1]

	def erase(self):
		self.display.text = ''

	def input_char(self, s):
		if s in '/%*-+':
			if '=' in self.display.text:
				lst = (self.display.text).split(' = ')
				self.display.text = lst[1] + s
			elif self.display.text == 'Error':
				self.display.text = s
			else:
				self.display.text += s
		else:
			if ('=' in self.display.text) | (self.display.text == 'Error'):
				self.display.text = s
			else:
				self.display.text += s

	def calculate(self, express):
		express = express.replace('^', '**')
		
		try:		
			self.display.text = self.display.text + ' = ' + str(eval(express))
		except Exception:
			self.display.text = 'Error'

class CalculatorApp(App):
	def build(self):
		return(Calculator())

if __name__ == "__main__":
	CalculatorApp().run()
