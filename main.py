# Please copy and paste your turtle greeting cards into here
import turtle

#turtle.Screen() allows you to define your screen size
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("#579D31") 

# Dictionary of colors
colors = {
  "blue" : "#579FBE",
  "green" : "#579D31",
  "yellow" : "#9DBE57",
  "red" : "#952918",
  "black": "#463735"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color()
artist.color(colors["black"])

#(font-family, font-size, font-style)
style = ("Verdana", 30, "normal")
artist.penup()
artist.goto(-100, -200)
name = input("give me your name noob")
artist.write("To - " + str(name), font = style, align = "center") 

style = ("Helvetica", 12, "normal")
artist.goto(0, 40)
artist.write("sup", font = style, align = "center")

artist.goto(0, 0)
artist.color(colors["blue"])
artist.write("am pro. am good at video games and am pro troller", font = style, align = "center")

artist.goto(0, 20)
artist.color(colors["red"])
artist.write("rekt nob", font = style, align = "center")

artist.goto(0, -20)
artist.color(colors["yellow"])
artist.write("wat you just say do you want fite?", font = style, align = "center")

artist.goto(0,-40)
artist.color(colors["blue"])
artist.write("friknob", font = style, align = "center")

artist.goto(0, -60)
artist.color(colors["black"])
artist.write("- sebee", font = style, align = "center")
artist.hideturtle() 