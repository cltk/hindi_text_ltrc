import os, re
import json
import pdb
import collections

omitted_dirs = ['original_classical_hindi_data']
sourceLink = 'http://ltrc.iiit.ac.in/showfile.php?filename=downloads/Classical_Hindi_Literature/SHUSHA/index.html'
source = 'Language Technologies Research Center, IIIT Hyderabad'
works = []

def jaggedListToDict(text):
	node = { str(i): t for i, t in enumerate(text) }
	node = collections.OrderedDict(sorted(node.items()))
	for child in node:
		if isinstance(node[child], list):
			node[child] = walkText(node[child])
	return node

def main():
	if not os.path.exists('cltk_json'):
		os.makedirs('cltk_json')

	for root, dirs, files in os.walk("."):
		path = root.split('/')
		print((len(path) - 1) * '---', os.path.basename(root))
		for fname in files:
			if fname.endswith('u') or fname.endswith('txt') and path[1] not in omitted_dirs:
				with open(os.path.join(root, fname)) as f:
					# lxml having troubles installing on my env, using html5 parser
					# unless the other parser is problematic
					lines = f.read().splitlines()

				titles = path[1:]
				for title in titles:
					title.title()
				titles = " ".join(titles)

				work = {
					'originalTitle': titles,
					'englishTitle': titles,
					'author': 'Not available',
					'source': source,
					'sourceLink': sourceLink,
					'language': 'hindi',
					'text': {},
				}

				# For these texts, save whitespace
				text = [line for line in lines if len(line.strip())]
				work['text'] = jaggedListToDict(text)
				fname = work['source'] + '__' + work['englishTitle'][0:100] + '__' + work['language'] + '.json'
				fname = fname.replace(" ", "")
				with open('cltk_json/' + fname, 'w') as f:
					json.dump(work, f)

if __name__ == '__main__':
	main()
