import						urllib2

class Stack: #We here define a stack, which is useful for managing the HTML syntax
	def __init__(self):
		self.items = []

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return (self.item == [])

	def __unicode__(self):
		return self.items

def getInsideHTMLTag(html_string, tag, my_class=None):
	list_tags = Stack() 
	contents = []
	beg = html_string.find('<body') #We read the HTML file inside the body tags
	end = html_string.find('</body')
	while (beg >= 0 and beg < end): #While reading is not over
		first = html_string.find('<',beg) 
		last = html_string.find('>',beg)
		tag_name = html_string[first+1:last] #Gets the next tag with its attributes
		if tag_name[:3] == '!--': #If the tag is a comment
			last = html_string.find('-->',beg) 
			beg = last + 3 #Skip it
			continue
		if tag_name[-1:] == '/': #If the tag is in one piece (e.g. img, input, etc;)
			tag_inside = ''
			for i in tag_name.split()[1:len(tag_name.split())-1]: #We retrieve the tag and all its attributes
				tag_inside += i + ' '
			contents.append({tag_name.split()[0]:tag_inside}) #And we save it in the contents list
		if tag_name[:1] != '/':
			list_tags.push({tag_name:last+1}) #If the tag is not a 'closer', we add it to our html stack
		else: #If the tag is an "opener"
			if list_tags.isEmpty: #if the html stack is empty, pass!
				beg = last + 1
				continue
			last_added = list_tags.pop() #else, pop the last html tag from the stack
			try: 
				is_same = (tag_name[1:] == last_added.keys()[0].split()[0])  #check if the last added to the stack is the same kind of the last read tag...
			except:
				pass
			if is_same: #...if so, we can get the enclosed content and add it to our contents list !
				contents.append({last_added.keys()[0]:html_string[last_added.values()[0]:last-(len(tag_name[1:])+2)]})
			else:
				list_tags.push(last_added) #else, we go a foot deeper into our html structure...
		beg = last + 1 #so our reading cursor keeps moving on
	# we have a contents list filled with html tags and their contents
	wanted_tags = []
	for i in range(len(contents)): 
		key = contents[i].keys()[0] 
		if tag in key: #if our wanted tag is in the list
			if my_class: #if a class has been precised
				start_class_index = key.find('class="') 
				end_class_index = key.find('"',start_class_index+7) #finds where the 'class="..." is in the tag string'
				if my_class in key[start_class_index:end_class_index]: # if our desired class is in this class="..."
					wanted_tags.append({key:contents[i].values()[0]}) # we add the tag to a list
			else:
				wanted_tags.append({key:contents[i].values()[0]})
	return wanted_tags

if __name__ == "__main__":
	url = raw_input()
	tag = raw_input()
	my_class = raw_input()
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()
	wanted_tags = getInsideHTMLTag(html,tag,my_class)
	print wanted_tags
