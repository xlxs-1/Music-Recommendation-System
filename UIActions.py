from Recomendation_System import *
from tkinter import *



def init():



  def runRecomenderPerfectlyBalanced():
    playlist=RecomenderPerfectlyBalanced(txt.get())

    lbl2.configure(text=getAsStringPlaylistAtMost50(playlist))
  def runRecomenderBalanced():
    playlist=RecomenderBalanced(txt.get())

    lbl2.configure(text=getAsStringPlaylistAtMost50(playlist))
  def runRecomenderObscure():
    playlist=RecomenderObscure(txt.get())

    lbl2.configure(text=getAsStringPlaylistAtMost50(playlist))
  def runRecomenderPlaylistArtist():
    playlist=RecomenderPlaylistArtist(txt.get())

    lbl2.configure(text=getAsStringPlaylistAtMost50(playlist))
  def runRecomenderPopular():
    playlist=RecomenderPopular(txt.get())

    lbl2.configure(text=getAsStringPlaylistAtMost50(playlist))

  def runPlotmostPopularSongs():
    PlotmostPopularSongs()
  def runPlotmostPopularArtists():
    PlotmostPopularArtists()
  def runPlotmostPopularPlaylists():
    PlotmostPopularPlaylists()









  window = Tk()

  window.title("Music Recomendation")
  window.geometry("1050x512") 
  #window.resizable(0, 0)
  lbl1 = Label(window, text="Please input user ID")
  lbl1.grid(column=0, row=0)

  txt = Entry(window,width=128)
  txt.grid(column=1, row=0)

  btn1 = Button(window, text="Daily Mix 1",command=runRecomenderPerfectlyBalanced)
  btn1.grid(column=0, row=1)
  btn2 = Button(window, text="Daily Mix2",command=runRecomenderBalanced)
  btn2.grid(column=0, row=2)
  btn3 = Button(window, text="Discover",command=runRecomenderObscure)
  btn3.grid(column=0, row=3)
  btn4 = Button(window, text="Epic Mix",command=runRecomenderPlaylistArtist)
  btn4.grid(column=0, row=4)
  btn5 = Button(window, text="Popular",command=runRecomenderPopular)
  btn5.grid(column=0, row=5)

  lbl2 = Label(window, text="")
  lbl2.grid(column=1,rowspan=9000, row=1)

  btn6 = Button(window, text="PlotmostPopularSongs",command=runPlotmostPopularSongs)
  btn6.grid(column=2, row=0)
  btn7 = Button(window, text="PlotmostPopularArtists",command=runPlotmostPopularArtists)
  btn7.grid(column=2, row=1)
  btn8 = Button(window, text="PlotmostPopularPlaylists",command=runPlotmostPopularPlaylists)
  btn8.grid(column=2, row=2)

  window.mainloop()
  





  