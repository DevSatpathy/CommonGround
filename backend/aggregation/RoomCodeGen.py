def randomString() {
	chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz"
	string_length = 5
	randomstring = ''
	for i in range (5):
		rnum = random.randint(len(chars))
		randomstring += chars.substring(rnum,rnum+1)

    pass randomstring
}