from PIL import Image, ImageDraw, ImageFilter
src='/root/.claude/uploads/2910aa65-1d82-51fb-b1f3-8de31cbe6264/a011ce13-image.jpg'
im=Image.open(src).convert('RGB')
W,H=im.size; s=W/1999
mask=Image.new('L',im.size,0); d=ImageDraw.Draw(mask)
boxes=[
 (563,512,700,526),   # Programadas: Recordatorio semanal
 (563,547,695,578),   # Dispatch items
 (563,619,698,753),   # Chats y tareas list
 (848,716,1000,766),  # En curso (monitor)
 (0,928,90,990),      # En curso (laptop)
]
for x0,y0,x1,y1 in boxes: d.rectangle([x0*s,y0*s,x1*s,y1*s],fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(3*s))
blur=im.filter(ImageFilter.GaussianBlur(6*s))
out=Image.composite(blur,im,mask)
out.save('/home/user/claude-banana/output/escritorio_titulos_borrosos.jpg',quality=95)


