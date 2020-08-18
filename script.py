import os, sys

requirements = [
			'BOOKS',
			'RESOURCES'
			]

SUBJECTS = []

SEM = 'sem' + sys.argv[1]

PATH = os.path.join('Z:\\college', SEM) 
if not os.path.exists(PATH):
	os.mkdir(PATH)
else:
	print("You already passed that way man !!!")
	exit()

print(f"Congratulations on getting to {sys.argv[1]} semester!!!\n Lets get ready for the new one ...")

noOfSub = int(input("How amny subject to crack this year ???\n>>>"))

for _ in range(noOfSub):
	SUBJECTS.append(input("enter Subject Name As per Syllabus \n>>>"))
# print(SUBJECTS)

for subject in SUBJECTS:
	subjectPath = os.path.join(PATH, subject)
	os.mkdir(subjectPath)
	print("Created " + subjectPath)
	newPath = os.chdir(subjectPath)
	for requirement in requirements:
		contentPath = os.path.join(subjectPath, requirement)
		os.mkdir(contentPath)
		print('created' + contentPath)

	print()


