links:
	-ln -s ../content/ content/\{static\}
	-ln -s ../content/ jupyter/\{static\}

nolinks:
	-rm content/\{static\}
	-rm jupyter/\{static\}
