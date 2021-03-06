#!/opt/rocks/bin/python
#
#

import sys
import string
import rocks.commands
from imgstorage.commandlauncher import CommandLauncher

class Command(rocks.commands.HostArgumentProcessor, rocks.commands.remove.command):
	"""
	Remove a storage volume form a NAS (or virtual machine images 
	repository).
	
	<arg type='string' name='nas' optional='0'>
	The NAS name which hosts the storage image
	</arg>

	<arg type='string' name='zpool' optional='0'>
	The zpool name. The final full zvol path name will be formed as
	zpool + "/" + volume
	</arg>

	<arg type='string' name='volume' optional='0'>
	The volume name which will be deleted
	</arg>

	<example cmd='remove host storageimg nas-0-0 zpool vm-sdsc125-2'>
	It remove the volume zpool/vm-sdsc125-2 from nas-0-0
	</example>
	"""

	def run(self, params, args):
		(args, nas, zpool, volume) = self.fillPositionalArgs(
				('nas', 'zpool', 'volume'))

		# debugging output
		if not (nas and zpool and volume):
			self.abort("3 arguments are required for this command nas zpool volume")

		print "removing  ", nas, ":", zpool, "/", volume
		CommandLauncher().callDelHostStorageimg(nas, zpool, volume)

		self.beginOutput()
		self.addOutput(nas, "Success")
		self.endOutput(padChar='')





RollName = "img-storage"
