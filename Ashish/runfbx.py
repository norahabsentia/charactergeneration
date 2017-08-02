import requests
import shutil
import sys

#call(["./biocharnorahserver.sh", "5000"]) #this should be done manually before starting
params = {'action':'fbx'}

files = {'design': open(sys.argv[1], 'rb'), 'render': open("render.json", "rb")}
rinput = requests.post("http://localhost:5000/render", files=files, data=params, stream=True)
with open(sys.argv[2], "wb") as f:
	rinput.raw.decode_content = True
	shutil.copyfileobj(rinput.raw, f)

