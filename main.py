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

artist.penup()
artist.goto(0, 0)
#(font-family, font-size, font-style)
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
artist.hideturtle()