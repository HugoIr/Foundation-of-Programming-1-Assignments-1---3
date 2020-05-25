# Import turtle dan di rename sebagai t
# Import random dan di rename sebagai rd
import turtle as t
import random as rd

# Masukkan sisi dari persegi yang diinginkan mulai dari 20-60 dengan default input 40
side = t.numinput("Rotating Colourful Squares and Disks", "Please enter the side length of the first square [20-60]",40, minval=20, maxval=60 )
# Membentuk mengatur ukuran layar
t.screensize(1500, 1500)
# Mempercepat pen
t.speed(0)
# Memilih warna yang akan digunakan sebanyak 255 pilihan warna
t.colormode(255)
# Menyembunyikan arah turtle
t.hideturtle()

# Menggeser pen kearah -220 dan 0 terhadap sumbu x dan y
t.penup()
t.setpos(-220,0)
t.pendown()

# Untuk membuat persegi sebanyak 72 buah
for i in range(72) :
    # Memilih angka secara acak 
    r= rd.randint(0,255)
    g= rd.randint(0,255)
    b= rd.randint(0,255)
    # Menerjemahkan angka acak kedalam warna
    t.fillcolor(r, g, b)
    # Mulai mengisikan warna
    t.begin_fill()

    # Membuat bentuk persegi
    for a in range(4):
        t.left(90)
        t.forward(side)
    # Berhenti mengisikan warna
    t.end_fill()
    # Mengeser arah pen 5 derajat ke kanan
    t.right(5)
    # Menambahkan sisi sebanyak 2 unit
    side +=2

# Menggeser pen kearah kanan layar
t.penup()
t.setpos(220,0)
t.pendown()
# Membuat variabel radius dengan ukuran setengah dari sisi terakhir
radius = side/2

# Untuk membuat lingkaran sebanyak 36 buah
for i in range (36):
    # Memilih angka secara acak 
    r= rd.randint(0,255)
    g= rd.randint(0,255)
    b= rd.randint(0,255)
    # Menerjemahkan angka acak kedalam warna
    t.fillcolor(r,g,b)
    # Mulai mengisikan warna
    t.begin_fill()
    # Membuat lingkaran dengan jari-jari sebesar radius
    t.circle(radius)
    # Menggeser pen sebanyak 10 derajat kearah kiri
    t.left(10)
    # Berhenti mengisikan warna
    t.end_fill()
    # Mengurangi radius sebanyak 2 unit
    radius -= 2

# Menggeser pen kearah bawah pada 0 dan -265 terhadap sumbu x dan y, mengganti warna pen, dan menuliskan keterangan
t.penup()
t.setpos(0, -265)
t.pencolor('blue')
t.write('There are 72 Squares and 36 Disks', font=('Arial', 20, 'normal') ,align='center',)

# Exit saat turtle di klik
t.exitonclick()
# Untuk menghindari terjadinya error
t.mainloop()

    
    
    