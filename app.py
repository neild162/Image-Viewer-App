from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer App')



my_img1 = ImageTk.PhotoImage(Image.open("details.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("remove.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("front.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("add_employee.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("login.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]


my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)


def forward(image_number):     #initial image_number=2
	global my_label
	global button_forward
	global button_back
	my_label.grid_forget() #when the forward function gets called we want to take the image that is already there and get rid of it.
	#If we dont get rid of current image and after that we click forward then the 2 images(next and current) will overlap
        my_label=Label(image=image_list[image_number-1]) #telling the program what the new image should be
        #image we want to show when we click forward first time is the image at index 1.(remember we have set image_number=2)
        button_forward=Button(root,text="Forward",command=lambda:forward(image_number+1))
        button_back=Button(root,text="Back",command=lambda:back(image_number-1))

        if image_number==5:
    	   button_forward=Button(root,text="Forward",state=DISABLED)
   
        my_label.grid(row=0,column=0,columnspan=3)
        button_forward.grid(row=1,column=2)
        button_back.grid(row=1,column=0)
 
    
     
def back(image_number):
	global my_label
	global button_forward
	global button_back
	my_label.grid_forget()   #again to prevent overlapping as in forward function
	my_label=Label(image=image_list[image_number-1])
	button_forward=Button(root,text="Forward",command=lambda:forward(image_number+1))
        button_back=Button(root,text="Back",command=lambda:back(image_number-1))

        my_label.grid(row=0,column=0,columnspan=3)
        button_forward.grid(row=1,column=2)
        button_back.grid(row=1,column=0)


button_back=Button(root,text="Back",command=back)
#no need to pass anything as we dont need back option when we run the program and are on the 1st image
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward=Button(root,text="Forward",command=lambda:forward(2))
#we pass '2' because when we run the program the first image is image 1 and we want to click and go to image 2


button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)


root.mainloop()
