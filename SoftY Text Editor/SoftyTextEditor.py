import os
import tkinter as tk
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import ttk

main_window = tk.Tk()
main_window.title('SoftY Text Editor')
main_window.geometry('1200x800')
main_window.wm_iconbitmap('icon.ico')

##################################################### Main Menu frontend ##################################################################
main_menu = tk.Menu(main_window)

# icons

# file icons
new_icon = tk.PhotoImage(file='icon/new.png')
open_icon = tk.PhotoImage(file='icon/open.png')
save_icon = tk.PhotoImage(file='icon/save.png')
save_as_icon = tk.PhotoImage(file='icon/save_as.png')
exit_icon = tk.PhotoImage(file='icon/exit.png')

# edit icons
cut_icon = tk.PhotoImage(file='icon/cut.png')
copy_icon = tk.PhotoImage(file='icon/copy.png')
paste_icon = tk.PhotoImage(file='icon/paste.png')
clear_icon = tk.PhotoImage(file='icon/clear_all.png')
find_icon = tk.PhotoImage(file='icon/find.png')

# view icons
show_tool_bar_icon = tk.PhotoImage(file='icon/tool_bar.png')
show_status_bar_icon = tk.PhotoImage(file='icon/status_bar.png')

# ColorTheme icons
light_icon = tk.PhotoImage(file='icon/light_default.png')
light_plus_icon = tk.PhotoImage(file='icon/light_plus.png')
dark_icon = tk.PhotoImage(file='icon/dark.png')
red_icon = tk.PhotoImage(file='icon/red.png')
monokai_icon = tk.PhotoImage(file='icon/monokai.png')
night_blue_icon = tk.PhotoImage(file='icon/night_blue.png')

# menu items
file = tk.Menu(main_menu, tearoff=0)
edit = tk.Menu(main_menu, tearoff=0)
view = tk.Menu(main_menu, tearoff=0)
colorTheme = tk.Menu(main_menu, tearoff=0)

################################################## Main Menu frontend End ##################################################################

################################################## Tool Bar Frontend End  ##################################################################

# Tool Bar label
TB = ttk.Label(main_window)
TB.pack(side=tk.TOP, fill=tk.X)

# Font Family
selectTextStyle = tk.StringVar()
fontFamily = ttk.Combobox(TB, width=35, state='readonly', textvariable=selectTextStyle)
fontFamily.grid(row=1, column=0, sticky=tk.W, padx=5)
ff = list(tk.font.families())
fontFamily['values'] = ff
fontFamily.current(ff.index('Arial'))

# Font Size

selectTextSize = tk.StringVar()
fontText = ttk.Combobox(TB, width=14, textvariable=selectTextSize)
fontText.grid(row=1, column=1, sticky=tk.W, padx=5)
fontText['values'] = list(range(1, 81, 2))
fontText.current(11)

# icons
bold_icon = tk.PhotoImage(file='icon/bold.png')
italic_icon = tk.PhotoImage(file='icon/italic.png')
left_align_icon = tk.PhotoImage(file='icon/align_left.png')
right_align_icon = tk.PhotoImage(file='icon/align_right.png')
center_align_icon = tk.PhotoImage(file='icon/align_center.png')
underline_icon = tk.PhotoImage(file='icon/underline.png')
fontColor_icon = tk.PhotoImage(file='icon/font_color.png')

# Bold button

boldButton = ttk.Button(TB, image=bold_icon)
boldButton.grid(row=1, column=2, padx=5)

# Italic button

italicButton = ttk.Button(TB, image=italic_icon)
italicButton.grid(row=1, column=3, padx=5)

# Underline button

underLineButton = ttk.Button(TB, image=underline_icon)
underLineButton.grid(row=1, column=4, padx=5)

# Font Color button

fontColorButton = ttk.Button(TB, image=fontColor_icon)
fontColorButton.grid(row=1, column=5, padx=5)

# Left Align button

leftAlignButton = ttk.Button(TB, image=left_align_icon)
leftAlignButton.grid(row=1, column=6, padx=5)

# Center Align button

centerAlignButton = ttk.Button(TB, image=center_align_icon)
centerAlignButton.grid(row=1, column=7, padx=5)

# Right Align button

rightAlignButton = ttk.Button(TB, image=right_align_icon)
rightAlignButton.grid(row=1, column=8, padx=5)

################################### Tool bar Frontend End #########################################################################

##################################### Text Editor #################################################################################

TE = tk.Text(main_window)
TE.config(wrap='word', relief=tk.FLAT)
TE.focus_set()
scrollBar = tk.Scrollbar(main_window)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
scrollBar.config(command=TE.yview)
TE.pack(fill=tk.BOTH, expand=True)

TE.config(yscrollcommand=scrollBar.set)

############################################ Text Editor End ############################################################################

############################################ Tool Bar functionalities #################################################################

# Font family and size change

current_font_size = 11
current_font_family = 'Arial'


def change_font(event=None):
    global current_font_size
    current_font_size = selectTextSize.get()
    TE.configure(font=(current_font_family, current_font_size))


def change_family(event=None):
    global current_font_family
    current_font_family = selectTextStyle.get()
    TE.configure(font=(current_font_family, current_font_size))


fontText.bind('<<ComboboxSelected>>', change_font)
fontFamily.bind('<<ComboboxSelected>>', change_family)

TE.configure(font=('Arial', 11))


# Bolding Up Text

def change_bold():
    textBehaviour = tk.font.Font(font=TE['font'])
    if textBehaviour.actual()['weight'] == 'normal':
        TE.configure(font=(current_font_family, current_font_size, 'bold'))
    elif textBehaviour.actual()['weight'] == 'bold':
        TE.configure(font=(current_font_family, current_font_size, 'normal'))


boldButton.configure(command=change_bold)


# Italifying the Text

def change_italic():
    textBehaviour = tk.font.Font(font=TE['font'])
    if textBehaviour.actual()['slant'] == 'roman':
        TE.configure(font=(current_font_family, current_font_size, 'italic'))
    elif textBehaviour.actual()['slant'] == 'italic':
        TE.configure(font=(current_font_family, current_font_size, 'roman'))


italicButton.configure(command=change_italic)


# Underlining the text

def change_UL():
    textBehaviour = tk.font.Font(font=TE['font'])
    if textBehaviour.actual()['underline'] == 0:
        TE.configure(font=(current_font_family, current_font_size, 'underline'))
    elif textBehaviour.actual()['underline'] == 1:
        TE.configure(font=(current_font_family, current_font_size, 'normal'))


underLineButton.configure(command=change_UL)


# font color Functionality

def change_font_color():
    askedColor = tk.colorchooser.askcolor()
    TE.configure(fg=str(askedColor[1]))


fontColorButton.configure(command=change_font_color)


# align left

def change_alignment_left():
    written_text = TE.get(1.0, tk.END)
    TE.tag_config('left', justify=tk.LEFT)
    TE.delete(1.0, tk.END)
    TE.insert(tk.INSERT, written_text, 'left')


leftAlignButton.configure(command=change_alignment_left)


# align center

def change_alignment_center():
    written_text = TE.get(1.0, tk.END)
    TE.tag_config('center', justify=tk.CENTER)
    TE.delete(1.0, tk.END)
    TE.insert(tk.INSERT, written_text, 'center')


centerAlignButton.configure(command=change_alignment_center)


# align right

def change_alignment_right():
    written_text = TE.get(1.0, tk.END)
    TE.tag_config('right', justify=tk.RIGHT)
    TE.delete(1.0, tk.END)
    TE.insert(tk.INSERT, written_text, 'right')


rightAlignButton.configure(command=change_alignment_right)

############################################# Tool Bar functionality End  ######################################################


############################################# status Bar Frontend ###############################################################

SB = ttk.Label(TE, text='Status Bar')
SB.pack(side=tk.BOTTOM)

############################################ Status Bar FrontEnd End ############################################################################

############################################ Status Bar BackEnd #############################################################################


text_changed = False


def change_status(event=None):
    global text_changed
    if TE.edit_modified():
        text_changed = True
        written_text = TE.get(1.0, 'end-1c')
        no_of_words = len(written_text.split())
        no_of_chars = len(written_text)
        SB.config(text=f'Characters : {no_of_chars} ; Words : {no_of_words}')

    TE.edit_modified(False)


TE.bind('<<Modified>>', change_status)

################################################# Status Bar BackEnd End ###############################################################################


################################################# Main menu functionality ####################################################################


file_loc = ''


# File Backend

# New functionality
def new_func(event=None):
    global file_loc
    file_loc = ''
    TE.delete(1.0, tk.END)


# open functionality
def open_func(event=None):
    global file_loc
    file_loc = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select file',
                                          filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    try:
        TE.delete(1.0, tk.END)
        with open(file_loc, 'r') as fr:
            content = fr.read()
            TE.insert(1.0, content)
    except FileNotFoundError:
        return
    except:
        return
    main_window.title(os.path.basename(file_loc))


# save functionality
def save_func(event=None):
    global file_loc
    try:
        content = str(TE.get(1.0, tk.END))
        if file_loc:
            with open(file_loc, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            file_loc = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
            file_loc.write(content)
            file_loc.close()
    except:
        return


# save as functionality
def save_as_func(event=None):
    global file_loc
    try:
        content = str(TE.get(1.0, tk.END))
        file_loc = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                            filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
        file_loc.write(content)
        file_loc.close()
    except:
        return


# exit functionality
def exit_func(event=None):
    global file_loc, text_changed
    if text_changed:
        mb = messagebox.askyesnocancel('Warning', 'Don\'t forget to save the file!!')
        if mb is True:
            try:
                content = str(TE.get(1.0, tk.END))
                if file_loc:
                    with open(file_loc, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                else:
                    file_loc = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                        filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
                    file_loc.write(content)
                    file_loc.close()
            except:
                return
            main_window.destroy()
        elif mb is False:
            main_window.destroy()
    else:
        main_window.destroy()


# Edit backend

# Find functionality

def find_backend(event=None):
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('400x200+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(False, False)

    def find_func():
        word = find_input.get()
        TE.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = TE.search(word, start_pos, stopindex=tk.END)
                print(start_pos)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                TE.tag_add('match', start_pos, end_pos)
                start_pos = end_pos
                matches += 1
                TE.tag_config('match', foreground='blue', background='cyan')

    def replace_func():
        word = find_input.get()
        replaced_word = replace_input.get()
        content = TE.get(1.0, tk.END)
        TE.delete(1.0, tk.END)
        replacedContent = content.replace(word, replaced_word)
        TE.insert(1.0, replacedContent)

    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(fill=tk.BOTH, padx=30, pady=20)

    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    find_input = ttk.Entry(find_frame, width=35)
    replace_input = ttk.Entry(find_frame, width=35)

    find_button = ttk.Button(find_frame, text='Find', command=find_func)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace_func)

    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=15, pady=4)
    replace_button.grid(row=2, column=1, padx=15, pady=4)

    find_dialogue.mainloop()


# View backend

# show toolbar functionality

def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        TB.pack_forget()
        show_toolbar = False
    else:
        TE.pack_forget()
        SB.pack_forget()
        TB.pack(side=tk.TOP, fill=tk.X)
        TE.pack(fill=tk.BOTH, expand=True)
        SB.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        SB.pack_forget()
        show_statusbar = False
    else:
        SB.pack(side=tk.BOTTOM)
        show_statusbar = True


# theme Backend
color_list = [('#000000', '#ffffff'),
              ('#474747', '#e0e0e0'),
              ('#c4c4c4', '#2d2d2d'),
              ('#2d2d2d', '#ffe8e8'),
              ('#d3b774', '#474747'),
              ('#ededed', '#6b9dc2')
              ]


def change_theme():
    chosenTheme = themeVar.get()
    TE.config(fg=color_list[chosenTheme][0], background=color_list[chosenTheme][1])


# Clubbing Main menu items after backend functions are declared

# file menu
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl + N', command=new_func)
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl + O', command=open_func)
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl + S', command=save_func)
file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl + Q', command=save_as_func)
file.add_separator()
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl + E', command=exit_func)

# Edit menu
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl + X',
                 command=lambda: TE.event_generate("<Control x>"))
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl + C',
                 command=lambda: TE.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl + V',
                 command=lambda: TE.event_generate("<Control v>"))
edit.add_command(label='Clear', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl + D',
                 command=lambda: TE.delete(1.0, tk.END))
edit.add_command(label='Find & Replace', image=find_icon, compound=tk.LEFT, accelerator='Ctrl + F',
                 command=find_backend)

# View menu

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

view.add_checkbutton(label='Show Tool Bar', image=show_tool_bar_icon, variable=show_toolbar, compound=tk.LEFT,
                     command=hide_toolbar)
view.add_checkbutton(label='Show Status Bar', image=show_status_bar_icon, variable=show_statusbar, compound=tk.LEFT,
                     command=hide_statusbar)

# ColorTheme Menu
themeVar = tk.IntVar()
colorTheme.add_radiobutton(label='Light', image=light_icon, variable=themeVar, value=0, compound=tk.LEFT,
                           command=change_theme)
colorTheme.add_radiobutton(label='Light Plus', image=light_plus_icon, value=1, variable=themeVar, compound=tk.LEFT,
                           command=change_theme)
colorTheme.add_radiobutton(label='Dark', image=dark_icon, variable=themeVar, value=2, compound=tk.LEFT,
                           command=change_theme)
colorTheme.add_radiobutton(label='Red', image=red_icon, variable=themeVar, value=3, compound=tk.LEFT,
                           command=change_theme)
colorTheme.add_radiobutton(label='Monokai', image=monokai_icon, variable=themeVar, value=4, compound=tk.LEFT,
                           command=change_theme)
colorTheme.add_radiobutton(label='Night Blue', image=night_blue_icon, variable=themeVar, value=5, compound=tk.LEFT,
                           command=change_theme)

# Cascading File, Edit, View ,ColorTheme
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=colorTheme)

########################################### Main Menu Functionality End ###########################################################

# binding shortcut keys

main_window.bind('<Control-n>', new_func)
main_window.bind('<Control-o>', open_func)
main_window.bind('<Control-s>', save_func)
main_window.bind('<Control-q>', save_as_func)
main_window.bind('<Control-e>', exit_func)

main_window.bind('<Control-d>', lambda: TE.delete(1.0, tk.END))
main_window.bind('<Control-f>', find_backend)

main_window.config(menu=main_menu)
main_window.mainloop()
