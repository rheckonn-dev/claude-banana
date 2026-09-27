from PIL import Image, ImageDraw, ImageFilter
src='/root/.claude/uploads/2910aa65-1d82-51fb-b1f3-8de31cbe6264/a011ce13-image.jpg'
im=Image.open(src).convert('RGB'); print(im.size)
W,H=im.size; sx,sy=W/1999,H/1500
S=lambda pts:[(x*sx,y*sy) for x,y in pts]
mask=Image.new('L',im.size,0); d=ImageDraw.Draw(mask)
# monitor screen
d.polygon(S([(548,360),(1262,428),(1262,800),(550,806)]),fill=255)
# laptop screen
d.polygon(S([(0,520),(512,548),(548,1012),(0,1045)]),fill=255)
# keep greetings sharp
d.rectangle(S([(884,558),(1094,594)]),fill=0)
d.rectangle(S([(0,724),(300,762)]),fill=0)
d.polygon(S([(1270,600),(1190,625),(1120,670),(1085,740),(1085,815),(1270,815)]),fill=0)
# keep water bottle sharp
d.polygon(S([(1010,676),(1060,676),(1085,760),(1085,810),(980,810),(980,760)]),fill=0)
mask=mask.filter(ImageFilter.GaussianBlur(4*sx))
blur=im.filter(ImageFilter.GaussianBlur(9*sx))
Image.composite(blur,im,mask).save('/home/user/claude-banana/output/escritorio_texto_borroso.jpg',quality=95)
