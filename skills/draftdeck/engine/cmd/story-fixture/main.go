package main
import("image";"image/color";"image/draw";"image/png";"os")
func main(){const w,h=1600,900;im:=image.NewRGBA(image.Rect(0,0,w,h));draw.Draw(im,im.Bounds(),&image.Uniform{color.RGBA{255,255,255,255}},image.Point{},draw.Src)
for x:=0;x<w;x+=28{for y:=0;y<h;y++{im.Set(x,y,color.RGBA{244,245,245,255})}}
for y:=0;y<h;y+=28{for x:=0;x<w;x++{im.Set(x,y,color.RGBA{244,245,245,255})}}
for i:=0;i<700;i++{x:=550+i/2;y:=i;if x<w&&y<h{im.Set(x,y,color.RGBA{230,231,231,255})};x=1080-i/2;if x>=0&&y<h{im.Set(x,y,color.RGBA{230,231,231,255})}}
f,e:=os.Create("scenes/story.png");if e!=nil{panic(e)};defer f.Close();if e=png.Encode(f,im);e!=nil{panic(e)}
}
