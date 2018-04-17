text_in = open('nmt_data/full.in').read()
text_out = open('nmt_data/full.out').read()

file_in = open('words.in','w')
words_in = text_in.split()
for word in words_in:
	word = word+'\n'
	file_in.write(word)

file_out = open('words.out','w')
words_out = text_out.split()
for word in words_out:
	word = word+'\n'
	file_out.write(word)