likes, views, comments = str( input("Type the number of likes, views and comments:").split())

checkers = [
    likes > 1000,
    views > 3000,
    comments > 2000
]

if any(checkers):
    print("Awesome video!")
else: 
    print("You need to improve your video...")