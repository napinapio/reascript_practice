import tkinter as tk

root = tk.Tk()


#(Int xOut, Int yOut) 
mouse_poji= RPR_GetMousePosition(0,0)

root.attributes("-topmost", True)
root.geometry("200x100+"+str(mouse_poji[0])+"+"+str(mouse_poji[1]))

root.title('•À‚Ñ‘Ö‚¦')

var=tk.IntVar()
hed_end=RPR_GetExtState("sunatomo","interval_hed_end")

item_count=RPR_CountSelectedMediaItems(0)
list_number=0
        
list_box=[]
while list_number < item_count:
        list={}
        item_id=RPR_GetSelectedMediaItem(0,list_number)
        list["item_id_list"]=item_id
            
        start_time=RPR_GetMediaItemInfo_Value(item_id,"D_POSITION")
        list["start_time_list"]=start_time
            
        list_box.append(list) 
            
        list_number+=1
            
list_box.sort(key=lambda x: x["start_time_list"])
        

var.set(hed_end)


def btn_clicl():
    num=var.get()
    user_input=txt.get() 
    RPR_SetExtState("sunatomo","item_interval_hed_end",user_input,1)
    RPR_SetExtState("sunatomo","interval_hed_end",num,1)
    root.destroy()
    
    if num==0:      
        #count=0
        for count in range(len(list_box)):
            id_list=list_box[count]
            item=id_list["item_id_list"]
            if count ==0:
                first_position=RPR_GetMediaItemInfo_Value(item,"D_POSITION")                           
                item_end_position=first_position+float(user_input)
            else:
                RPR_SetMediaItemInfo_Value(item,"D_POSITION",item_end_position)             
                psition=RPR_GetMediaItemInfo_Value(item,"D_POSITION")
                item_end_position=psition+float(user_input)
                
            count+=1    
    elif num==1:      
        for count in range(len(list_box)):
            id_list=list_box[count]
            item=id_list["item_id_list"]
            if count ==0:
                first_position=RPR_GetMediaItemInfo_Value(item,"D_POSITION")
                RPR_SetMediaItemInfo_Value(item,"D_POSITION",first_position)
                first_lemgth=RPR_GetMediaItemInfo_Value(item,"D_LENGTH")                 
                item_end_position=first_lemgth+first_position+float(user_input)
            else:
                RPR_SetMediaItemInfo_Value(item,"D_POSITION",item_end_position)
                lemgth=RPR_GetMediaItemInfo_Value(item,"D_LENGTH")
                psition=RPR_GetMediaItemInfo_Value(item,"D_POSITION")
                item_end_position=lemgth+psition+float(user_input)
  

rdo1 = tk.Radiobutton(root,value=0,variable=var, text='item_strat')
rdo1.pack()

rdo2 = tk.Radiobutton(root,value=1,variable=var, text='item_end')
rdo2.pack()

lbl=tk.Label(text="•b”Žw’è")
lbl.pack(fill="x",padx=20,side="left")

txt= tk.Entry(width=5)
txt.pack(fill="x",padx=0,side="left")


time=RPR_GetExtState("sunatomo","item_interval_hed_end")
txt.insert(tk.END,time)

btn= tk.Button(root,text="ok",command=btn_clicl)
btn.pack(fill="x",ipadx=20,side="left")

root.mainloop()

RPR_ShowConsoleMsg("dekita")
