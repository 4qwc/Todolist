from django.db import models


class Todolist(models.Model):#   id จะป้อนให้อัตโนมัติ
    title = models.CharField(max_length=100) # บังคับใส่ KEY POST ถ้าไม่ใส่จะ return EEOR 
    detail = models.TextField(null=True, blank=True)# ไม่บังคับใส่ KEY POST 


    # ฟังก์ชั่นโชว์รายการในฐานข้อมูลเว็บ
    def __str__(self):
        return self.title


        