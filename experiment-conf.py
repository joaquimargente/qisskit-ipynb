#Configuration for running experiments
qasm = '' #QASM 2.0 code to be run, where "\n" is always interpreted as a newline character, even if attached to other characters
dtimeout = None #Extra variable for a default timeout, must be set as a numeric numberm. e.g: "dtimeout = 120", not "dtimeout = '120'"

#Shortcuts
sim = 'simulator' #Shortened 'simulator'
qx2 = 'ibmqx2' #Shortened 'ibmqx2'
tout = timeout #Shortened timeout
dtout = dtimeout #Shortened dtimeout