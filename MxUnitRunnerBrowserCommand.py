#
# History:
#
# 2014-10-13:
#    * Created
#

import re
import sys
import webbrowser
import sublime_plugin

PLUGIN_VERSION = "0.1"

class MxUnitRunnerBrowserCommand(sublime_plugin.TextCommand):
	_pythonVersion = sys.version_info[0]

	def getProjectSettings(self, view):
		return view.settings().get("mxunit-runner")

	def convertToTestURL(self, fileToOpen, basePath, baseUrl, testMethod, additionalUrlParameters):
		urlPath = fileToOpen.replace(basePath, baseUrl)
		urlPath = re.sub(r"\\", "/", urlPath) + "?method=runtestremote&output=html"

		#if a user selected a specific test method to run we should just run that one test instead of the entire file.
		tmLen = len(testMethod)
		if tmLen > 0:
			urlPath += "&testMethod=" + testMethod
		urlPath += additionalUrlParameters
		return urlPath

	def run(self, edit):
		print("MXUnit Runner plugin v{0}, Python {1}".format(PLUGIN_VERSION, self._pythonVersion))

		selectedRegion = self.view.sel()
		testMethod = self.view.substr(selectedRegion[0])


		projectSettings = self.getProjectSettings(self.view)
		fileToOpen = self.view.file_name()

		if not projectSettings:
			print("You must provide project-specific settings to configure and run MXUnit tests!!")
			return

		additionalUrlParameters = projectSettings["additionalUrlParameters"] if "additionalUrlParameters" in projectSettings else ""
		urlPath = self.convertToTestURL(fileToOpen, projectSettings["testsDirectory"], projectSettings["urlPrefix"], testMethod, additionalUrlParameters)

		#
		# Run tests in default web browser
		#
		webbrowser.open_new_tab(urlPath)
