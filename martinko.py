import tkinter as tk
from tkinter import *
from tkinter import ttk

# ==========================================
# WINDOW SETUP
# ==========================================
root = tk.Tk()
root.title("Car Suspension Parts Learning System")
root.geometry("1024x768")
root.configure(bg="#0f172a")  # Tailwind Slate-900

# ==========================================
# DATA
# ==========================================
parts_data = {
    "Shock Absorber":
        """1. หน้าที่หลัก
        Shock Absorber หรือโช๊คอัพ เป็นอุปกรณ์สำคัญของระบบช่วงล่าง มีหน้าที่ลดแรงสั่นสะเทือนและควบคุมการยุบ–ยืดของสปริง เพื่อไม่ให้รถเด้งขึ้นลงมากเกินไปหลังจากเจอหลุมหรือพื้นถนนขรุขระ
        นอกจากนี้ยังช่วยให้ล้อสัมผัสพื้นถนนตลอดเวลา เพิ่มการยึดเกาะถนน ทำให้ควบคุมรถได้ง่ายขึ้น และช่วยเพิ่มความนุ่มนวลในการขับขี่
        
        2. หลักการทำงาน
        เมื่อรถวิ่งผ่านหลุมหรือสิ่งกีดขวาง สปริงจะยุบตัวและคืนตัวอย่างรวดเร็ว หากไม่มีโช๊คอัพ รถจะเด้งต่อเนื่องหลายครั้ง
        ภายในโช๊คอัพจะมีลูกสูบเคลื่อนที่ขึ้นลงในกระบอกที่บรรจุน้ำมันไฮดรอลิก เมื่อลูกสูบเคลื่อนที่ น้ำมันจะไหลผ่านรูวาล์วขนาดเล็ก ทำให้เกิดแรงต้าน ช่วยชะลอการเคลื่อนที่ของสปริงและลดการสั่นสะเทือน
        
        3. ส่วนประกอบหลัก
        Piston Rod (ก้านลูกสูบ) : เชื่อมต่อกับตัวรถ รับแรงเคลื่อนที่
        Piston (ลูกสูบ) : ควบคุมการไหลของน้ำมันภายใน
        Cylinder Tube (กระบอกโช๊ค) : ตัวเรือนบรรจุน้ำมันและลูกสูบ
        Hydraulic Oil (น้ำมันไฮดรอลิก) : ช่วยสร้างแรงต้านและลดแรงสั่น
        Valve System (ระบบวาล์ว) : ควบคุมอัตราการไหลของน้ำมัน
        Seal (ซีลกันรั่ว) : ป้องกันน้ำมันรั่วออกจากกระบอกโช๊ค
        
        4. ประเภท
        Oil Shock Absorber : ใช้น้ำมันไฮดรอลิกอย่างเดียว ให้ความนุ่มนวล
        Gas Shock Absorber : เติมแก๊สไนโตรเจนเพื่อลดฟองอากาศ ทำงานตอบสนองเร็ว
        Strut Type Shock Absorber : รวมโช๊คและโครงสร้างรองรับล้อไว้ด้วยกัน นิยมใช้ในรถยนต์สมัยใหม่
        Adjustable Shock Absorber : สามารถปรับความแข็ง–อ่อนได้
        
        5. อาการเมื่อเสื่อม
        รถเด้งหลายครั้งหลังผ่านหลุม
        รถโคลงมากเวลาเข้าโค้ง
        เบรกแล้วหน้าทิ่ม
        มีน้ำมันรั่วบริเวณกระบอกโช๊ค
        ยางสึกผิดปกติ
        มีเสียงดังจากช่วงล่าง
        
        6. ความสำคัญต่อความปลอดภัย
        โช๊คอัพช่วยให้รถทรงตัวได้ดี ลดระยะเบรก และเพิ่มประสิทธิภาพการควบคุมรถ โดยเฉพาะเวลาขับด้วยความเร็วสูง เข้าโค้ง หรือขับบนถนนเปียก หากโช๊คอัพเสื่อมจะทำให้การควบคุมรถแย่ลงและเสี่ยงต่ออุบัติเหตุ""",

    "Springs":
        """1. หน้าที่หลัก
        สปริงช่วงล่างมีหน้าที่รองรับน้ำหนักของตัวรถ ดูดซับแรงกระแทกจากพื้นถนน และช่วยรักษาความสูงของรถให้อยู่ในระดับที่เหมาะสม
        ยังช่วยลดแรงสะเทือนที่ส่งมาถึงห้องโดยสาร ทำให้ผู้โดยสารรู้สึกนุ่มนวลขณะขับขี่
        
        2. หลักการทำงาน
        เมื่อรถได้รับแรงกระแทก สปริงจะยุบตัวเพื่อดูดซับแรง จากนั้นจะคืนตัวกลับสู่ตำแหน่งเดิมเพื่อรักษาสมดุลของรถ
        การทำงานของสปริงจะทำงานร่วมกับโช๊คอัพ ซึ่งช่วยควบคุมการเด้งของสปริง
        
        3. ส่วนประกอบหลัก
        Coil Spring : สปริงขดรูปทรงเกลียว
        Leaf Spring : แหนบเหล็กซ้อนกันหลายชั้น
        Torsion Bar : แกนเหล็กบิดตัวเพื่อรับแรง
        
        4. ประเภท
        Coil Spring (สปริงขด) : ใช้ในรถยนต์นั่งทั่วไป ให้ความนุ่มนวล
        Leaf Spring (แหนบ) : ใช้ในรถบรรทุก รองรับน้ำหนักมาก
        Torsion Spring : ใช้แรงบิดในการรองรับแรงกระแทก
        Air Spring : ใช้แรงดันลมแทนสปริงโลหะ พบในรถหรูหรือรถบรรทุกบางประเภท
        
        5. อาการเมื่อเสื่อม
        รถเอียงหรือเตี้ยลงผิดปกติ
        รถกระแทกแรงกว่าปกติ
        สปริงหักหรือแตกร้าว
        ขับแล้วรู้สึกแข็งหรือย้วยผิดปกติ
        
        6. ความสำคัญต่อความปลอดภัย
        สปริงช่วยให้รถรักษาสมดุล ลดแรงกระแทก และทำให้ล้อสัมผัสพื้นถนนได้อย่างต่อเนื่อง หากสปริงเสียหาย รถอาจเสียการทรงตัวหรือควบคุมยาก""",

    "Control Arm":
        """1. หน้าที่หลัก
        Control Arm หรือปีกนก เป็นชิ้นส่วนที่เชื่อมต่อระหว่างล้อกับโครงรถ ทำหน้าที่ควบคุมตำแหน่งและมุมของล้อ
        ช่วยให้ล้อสามารถเคลื่อนที่ขึ้นลงตามสภาพถนนได้อย่างอิสระ
        
        2. หลักการทำงาน
        ปีกนกทำหน้าที่เป็นแขนยึดระหว่างตัวถังรถกับดุมล้อ โดยมี Ball Joint เป็นจุดหมุน และมี Bushing ช่วยลดแรงสั่นสะเทือน
        เมื่อรถเคลื่อนที่บนพื้นขรุขระ ปีกนกจะช่วยให้ล้อเคลื่อนที่ได้อย่างเหมาะสมโดยไม่กระทบต่อการควบคุมรถ
        
        3. ส่วนประกอบหลัก
        Arm Body : โครงหลักของปีกนก
        Ball Joint : จุดหมุนเชื่อมต่อกับดุมล้อ
        Rubber Bushing : ยางรองลดแรงสั่นสะเทือน
        Mounting Bolt : น็อตยึดกับตัวถังรถ
        
        4. ประเภท
        Upper Control Arm : ปีกนกบน
        Lower Control Arm : ปีกนกล่าง
        A-Arm : รูปทรงคล้ายตัว A
        Multi-link Arm : ระบบหลายจุดยึด เพิ่มความนุ่มนวล
        
        5. อาการเมื่อเสื่อม
        พวงมาลัยสั่น
        รถกินซ้ายหรือกินขวา
        ยางสึกผิดปกติ
        มีเสียงดังเวลาเจอหลุม
        รถควบคุมยาก
        
        6. ความสำคัญต่อความปลอดภัย
        ปีกนกช่วยรักษามุมล้อและเสถียรภาพของรถ หากชำรุดอาจทำให้ควบคุมรถได้ยาก โดยเฉพาะเวลาเข้าโค้งหรือเบรกกะทันหัน""",

    "Ball Joint":
        """1. หน้าที่หลัก
        Ball Joint เป็นข้อต่อสำคัญระหว่างปีกนกกับดุมล้อ ช่วยให้ล้อสามารถเลี้ยวและเคลื่อนที่ขึ้นลงได้พร้อมกัน
        
        2. หลักการทำงาน
        ภายในลูกหมากจะมีลูกบอลเหล็กอยู่ในเบ้ารองรับ ทำให้เคลื่อนที่ได้หลายทิศทาง
        จึงรองรับทั้งการหมุนของพวงมาลัยและการเคลื่อนตัวของช่วงล่างในเวลาเดียวกัน
        
        3. ส่วนประกอบหลัก
        Ball Stud : แกนลูกบอล
        Housing : ตัวเรือนโลหะ
        Grease : จาระบีหล่อลื่น
        Rubber Boot : ยางกันฝุ่นและสิ่งสกปรก
        Bearing Seat : รองรับการเคลื่อนไหวของลูกบอล
        
        4. ประเภท
        Upper Ball Joint
        Lower Ball Joint
        Press-in Ball Joint
        Bolt-on Ball Joint
        Load-carrying Ball Joint : รับน้ำหนักหลักของรถ
        
        5. อาการเมื่อเสื่อม
        มีเสียงกุกกักจากช่วงล่าง
        พวงมาลัยหลวม
        รถส่ายเวลาใช้ความเร็ว
        ล้อเอียงผิดปกติ
        ยางสึกไม่เท่ากัน
        
        6. ความสำคัญต่อความปลอดภัย
        Ball Joint เป็นจุดหมุนหลักของระบบบังคับเลี้ยว หากเสียหายรุนแรงอาจทำให้ล้อหลุดจากระบบช่วงล่าง ส่งผลให้ควบคุมรถไม่ได้และเกิดอุบัติเหตุได้""",

    "Stabilizer Bar":
        """1. หน้าที่หลัก
        ช่วยลดการโคลงของตัวรถขณะเข้าโค้ง และช่วยให้รถมีความสมดุลมากขึ้น
        
        2. หลักการทำงาน
        Stabilizer Bar เชื่อมต่อช่วงล่างด้านซ้ายและขวา เมื่อรถเอียงขณะเข้าโค้ง เหล็กกันโคลงจะบิดตัว
        เพื่อถ่ายแรงไปอีกฝั่ง ทำให้รถไม่เอียงมากเกินไป
        
        3. ส่วนประกอบหลัก
        Stabilizer Bar : เหล็กกันโคลง
        Stabilizer Link : ลูกหมากกันโคลง
        Rubber Bushing : ยางรัดเหล็กกันโคลง
        
        4. ประเภท
        Front Stabilizer Bar : กันโคลงหน้า
        Rear Stabilizer Bar : กันโคลงหลัง
        Solid Stabilizer Bar : แบบตัน
        Hollow Stabilizer Bar : แบบกลวง (น้ำหนักเบา)
        
        5. อาการเมื่อเสื่อม
        รถโคลงมากเวลาเข้าโค้ง
        มีเสียงดังจากช่วงล่าง
        ลูกหมากกันโคลงหลวม
        
        6. ความสำคัญต่อความปลอดภัย
        ช่วยเพิ่มเสถียรภาพของรถ ทำให้ควบคุมรถได้ดีขึ้นในขณะเข้าโค้งหรือเปลี่ยนเลน"""
}


# ==========================================
# FUNCTIONS & EFFECTS
# ==========================================
def show_data(part):
    text_box.config(state=NORMAL)
    text_box.delete(1.0, END)

    # อัปเดตหัวข้อที่เลือก
    content_title.config(text=f"⚙️ {part.upper()}")

    # ดึงข้อมูลและจัดการ Formatting ให้สวยงาม
    lines = parts_data[part].split('\n')
    for line in lines:
        # ตรวจจับหัวข้อหลัก (1., 2., 3., ...) เพื่อเน้นสีและตัวหนา
        if line.strip().startswith(("1.", "2.", "3.", "4.", "5.", "6.")):
            text_box.insert(END, line + '\n', "header")
        # ตรวจจับรายการที่มีเครื่องหมาย : เพื่อเน้นข้อความ
        elif " : " in line:
            parts = line.split(" : ")
            text_box.insert(END, f"• {parts[0]}", "bullet_title")
            text_box.insert(END, f" : {parts[1]}\n", "body")
        else:
            text_box.insert(END, line + '\n', "body")

    text_box.config(state=DISABLED)


def on_enter(e):
    e.widget['background'] = '#0ea5e9'  # โทนสีฟ้าสว่างขึ้นเมื่อชี้เมาส์
    e.widget['foreground'] = '#ffffff'


def on_leave(e):
    e.widget['background'] = '#1e293b'  # กลับเป็นสีเดิม
    e.widget['foreground'] = '#cbd5e1'


# ==========================================
# HEADER SECTION
# ==========================================
top_frame = Frame(root, bg="#0f172a", pady=25)
top_frame.pack(fill=X)

Label(top_frame, text="🚗 VEHICLE SUSPENSION SYSTEM", font=("Segoe UI", 32, "bold"),
      bg="#0f172a", fg="#38bdf8").pack()
Label(top_frame, text="สื่อการเรียนรู้ระบบช่วงล่างรถยนต์สมัยใหม่", font=("Leelawadee UI", 14),
      bg="#0f172a", fg="#94a3b8").pack(pady=(5, 0))

# เส้นคั่น Divider
Frame(root, bg="#334155", height=1).pack(fill=X, padx=30)

# ==========================================
# MAIN LAYOUT (Sidebar + Content)
# ==========================================
main_frame = Frame(root, bg="#0f172a")
main_frame.pack(fill=BOTH, expand=True, padx=30, pady=20)

# =================SIDEBAR==================
menu_frame = Frame(main_frame, bg="#0f172a", width=260)
menu_frame.pack(side=LEFT, fill=Y, padx=(0, 25))
menu_frame.pack_propagate(False)

Label(menu_frame, text="≡ CHOOSE COMPONENT", font=("Segoe UI", 12, "bold"),
      bg="#0f172a", fg="#94a3b8", anchor="w").pack(fill=X, pady=(10, 20), padx=5)

btn_style = {
    "font": ("Segoe UI", 12, "bold"),
    "bg": "#1e293b",
    "fg": "#cbd5e1",
    "activebackground": "#38bdf8",
    "activeforeground": "#0f172a",
    "bd": 0,
    "height": 2,
    "cursor": "hand2",
    "anchor": "w",  # ชิดซ้าย
    "padx": 20  # ระยะขอบซ้ายของปุ่ม
}

menu_items = ["Shock Absorber", "Springs", "Control Arm", "Ball Joint", "Stabilizer Bar"]

for item in menu_items:
    btn = Button(menu_frame, text=item, command=lambda i=item: show_data(i), **btn_style)
    btn.pack(fill=X, pady=4, padx=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# =================CONTENT AREA==================
content_bg = "#ffffff"

content_wrapper = Frame(main_frame, bg="#cbd5e1", padx=1, pady=1)  # สร้างกรอบบางๆ คล้าย Border
content_wrapper.pack(side=RIGHT, fill=BOTH, expand=True)

content_frame = Frame(content_wrapper, bg=content_bg)
content_frame.pack(fill=BOTH, expand=True)

# หัวข้อเนื้อหา
content_title = Label(content_frame, text="👋 WELCOME", font=("Segoe UI", 20, "bold"),
                      bg=content_bg, fg="#0369a1", pady=20, anchor="w", padx=35)
content_title.pack(fill=X)

# Text Box พร้อม Ttk Scrollbar
text_frame = Frame(content_frame, bg=content_bg)
text_frame.pack(fill=BOTH, expand=True, padx=(35, 20), pady=(0, 30))

style = ttk.Style()
style.theme_use('clam')
scrollbar = ttk.Scrollbar(text_frame)

text_box = Text(
    text_frame,
    font=("Leelawadee UI", 12),
    bg=content_bg,
    fg="#334155",
    wrap="word",
    bd=0,
    yscrollcommand=scrollbar.set,
    cursor="arrow"
)
scrollbar.config(command=text_box.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_box.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 15))

# กำหนด Tag ของ Text สำหรับตกแต่งข้อความ
text_box.tag_config("header", font=("Leelawadee UI", 14, "bold"), foreground="#0284c7", spacing1=15, spacing3=5)
text_box.tag_config("body", font=("Leelawadee UI", 12), foreground="#334155", spacing1=3, spacing3=3)
text_box.tag_config("bullet_title", font=("Leelawadee UI", 12, "bold"), foreground="#0f172a", spacing1=3)
text_box.tag_config("welcome", font=("Leelawadee UI", 14), foreground="#64748b", justify="center", spacing1=50)

# ==========================================
# FOOTER SECTION
# ==========================================
bottom_frame = Frame(root, bg="#0f172a", pady=20)
bottom_frame.pack(fill=X)

exit_btn = Button(
    bottom_frame,
    text="EXIT PROGRAM",
    font=("Segoe UI", 11, "bold"),
    bg="#e11d48",  # โทนสีแดง Rose ทันสมัย
    fg="white",
    activebackground="#be123c",
    activeforeground="white",
    width=20,
    height=2,
    bd=0,
    cursor="hand2",
    command=root.destroy
)
exit_btn.pack()

# Initial Message
text_box.insert(END,
                "ยินดีต้อนรับเข้าสู่ระบบเรียนรู้ส่วนประกอบช่วงล่าง\n\n👈 กรุณาคลิกเลือกหัวข้อที่คุณต้องการศึกษาจากเมนูด้านซ้ายมือครับ",
                "welcome")
text_box.config(state=DISABLED)

root.mainloop()