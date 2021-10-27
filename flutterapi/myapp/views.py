from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist


#GET Data
@api_view(['GET'])
def all_todolist(request):
	alltodolist = Todolist.objects.all()# ดึงข้อมูลจาก model Todolist
	serializer = TodolistSerializer(alltodolist, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)




# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
	if request.method == 'POST':
		serializer = TodolistSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status-status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):
	todo = Todolist.objects.get(id=TID)

	if request.method == 'PUT':
		data = {}
		serializer = TodolistSerializer(todo,data=request.data)
		if serializer.is_valid():
			serializer.save()
			data['status'] = 'updated'
			return Response(data=data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_todolist(request,TID):
	todo = Todolist.objects.get(id=TID)


	if request.method == 'DELETE':
		delete = todo.delete()
		data = {}
		if delete:
			data['status'] = 'delete'
			statuscode = status.HTTP_200_OK
		else:
			data['status'] = 'failed'
			statuscode = status.HTTP_400_BAD_REQUEST
	return Response(data=data, status=statuscode)


data = [
	{
		"title":"คอมพิวเตอร์คืออะไร?",
		"subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ใช้ในการคำนวณและทำงานอื่นๆ",
		"image_url":"https://cdn.pixabay.com/photo/2015/01/21/14/14/apple-606761__480.jpg",
		"detail":"คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์[2][3] เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์ โดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย\n\nคอมพิวเตอร์ถูกประดิษฐ์ออกมาให้ประกอบไปด้วยความจำรูปแบบต่าง ๆ เพื่อเก็บข้อมูล อย่างน้อยหนึ่งส่วนที่มีหน้าที่ดำเนินการคำนวณเกี่ยวกับตัวดำเนินการทางตรรกศาสตร์ และตัวดำเนินการทางคณิตศาสตร์ และส่วนควบคุมที่ใช้เปลี่ยนแปลงลำดับของตัวดำเนินการโดยยึดสารสนเทศที่ถูกเก็บไว้เป็นหลัก อุปกรณ์เหล่านี้จะยอมให้นำเข้าข้อมูลจากแหล่งภายนอก และส่งผลจากการคำนวณตัวดำเนินการออกไป\n\nหน่วยประมวลผลของคอมพิวเตอร์มีหน้าที่ดำเนินการกับคำสั่งต่าง ๆ ที่คอยสั่งให้อ่าน ประมวล และเก็บข้อมูลไว้ คำสั่งต่าง ๆ ที่มีเงื่อนไขจะแปลงชุดคำสั่งให้ระบบและสิ่งแวดล้อมรอบ ๆ เป็นฟังก์ชันที่สถานะปัจจุบัน\n\nคอมพิวเตอร์อิเล็กทรอนิกส์เครื่องแรกถูกพัฒนาขึ้นในช่วงกลางคริสต์ศตวรรษที่ 20 (ค.ศ. 1940 – ค.ศ. 1945) แรกเริ่มนั้น คอมพิวเตอร์มีขนาดเท่ากับห้องขนาดใหญ่ ซึ่งใช้พลังงานมากเท่ากับเครื่องคอมพิวเตอร์ส่วนบุคคล (พีซี) สมัยใหม่หลายร้อยเครื่องรวมกัน[4]\n\nคอมพิวเตอร์ในสมัยใหม่นี้ผลิตขึ้นโดยใช้วงจรรวม หรือวงจรไอซี (Integrated circuit) โดยมีความจุมากกว่าสมัยก่อนล้านถึงพันล้านเท่า และขนาดของตัวเครื่องใช้พื้นที่เพียงเศษส่วนเล็กน้อยเท่านั้น คอมพิวเตอร์อย่างง่ายมีขนาดเล็กพอที่จะถูกบรรจุไว้ในอุปกรณ์โทรศัพท์มือถือ และคอมพิวเตอร์มือถือนี้ใช้พลังงานจากแบตเตอรี่ขนาดเล็ก และหากจะมีคนพูดถึงคำว่า 'คอมพิวเตอร์' มักจะหมายถึงคอมพิวเตอร์ส่วนบุคคลซึ่งถือเป็นสัญลักษณ์ของยุคสารสนเทศ อย่างไรก็ดี ยังมีคอมพิวเตอร์ชนิดฝังอีกมากมายที่พบได้ตั้งแต่ในเครื่องเล่นเอ็มพีสามจนถึงเครื่องบินบังคับ และของเล่นชนิดต่าง ๆ จนถึงหุ่นยนต์อุตสาหกรรม"
	},
	
	{
		"title":"Flutter คือ?",
		"subtitle":"Tools สำหรับออกแบบ UI ของ google",
		"image_url":"https://cdn.pixabay.com/photo/2015/04/23/22/05/hummingbird-736890__340.jpg",
		"detail":"Flutter คือ Cross-Platform Framework ที่ใช้ในการพัฒนา Native Mobile Application (Android/iOS) พัฒนาโดยบริษัท Google Inc. โดยใช้ภาษา Dart ในการพัฒนา ที่มีความคล้ายกับภาษา C# และ Java\n\nอีกหนึ่งจุดเด่นของ Flutter คือ การปรับแต่ง UI (User Interface) ที่มีความยืนหยุ่น แยกการออกแบบเพื่อเน้นไปที่ประสบการณ์ของผู้ใช้งาน UX (User Experience) โดย UI จะใกล้เคียงกับ Native และตรงตาม Design Guideline ที่ถูกต้อง และมีความสามารถในการทำ Hot Reload ที่ทำให้การแก้ไขโค้ดสามารถแสดงผลได้ทันทีในระหว่างที่รันแอปพลิเคชัน และยังรวมไปถึงมี Widget ที่พร้อมให้เลือกใช้มากมาย ทำให้พัฒนาแอปพลิเคชันได้ไวเหมาะสำหรับองค์กรที่ต้องการแอปที่สวยงามและมีประสิทธิภาพ"
	},
	{
		"title":"Python คือ?",
		"subtitle":"เป็นภาษาการเขียนโปรแกรมระดับสูงเรียนรู้ได้ง่าย และมีไวยากรณ์ที่ช่วยให้เขียนโค้ดสั้นกว่าภาษาอื่นๆ",
		"image_url":"https://cms-assets.skooldio.com/blog/wp-content/uploads/2021/05/25135717/178078282_301859104824700_8883068297885979344_n.jpeg",
		"detail":"ภาษาไพธอน (Python) เป็นภาษาการเขียนโปรแกรมระดับสูง ที่นำข้อดีของภาษาต่างๆ มารวมไว้ด้วยกัน ถูกออกแบบมาให้เรียนรู้ได้ง่าย และมีไวยากรณ์ที่ช่วยให้เขียนโค้ดสั้นกว่าภาษาอื่นๆ มีความสามารถใช้ชนิดข้อมูลแบบไดนามิก จัดการหน่วยความจำอัตโนมัติ สนับสนุนกระบวนทัศน์การเขียนโปรแกรม (Programming paradigms) ประกอบด้วย การเขียนโปรแกรมเชิงวัตถุ (OOP : Object Oriented Programming) การเขียนโปรแกรมเชิงคำสั่ง (Imperative Programming) การเขียนโปรแกรมเชิงฟังก์ชั่น (Functional)\n\nและการเขียนโปรแกรมเชิงกระบวนการ มีลักษณะเป็นภาษาสคริปต์ที่ทำงานร่วมกับภาษาอื่นได้ มีไลบรารี่มาตรฐานมากมาย และใช้อินเตอร์พรีเตอร์แปลภาษาโปรแกรมให้ทำงานบนระบบปฎิบัติการได้หลากหลาย ทั้งบน Windows, MAC, Linux และ Unix นอกจากนั้นยังเป็นโปรแกรมแบบ Oepn source ที่นำใช้ได้ฟรี เหมาะสำหรับโปรแกรมทั้งขนาดเล็กแบะขนาดใหญ่ เช่น การสร้างเกม เฟรมเวิร์กพัฒนาเว็บ โปรแกรมที่ใช้กราฟิกติดต่อกับผู้ใช้งาน (GUI) งานคำนวนทางวิทยาศาสตร์และสถิติ งานพัฒนาซอฟแวร์ และซอฟแวร์ควบคุมระบบ เป็นต้น"
	},
	
	],

def Home(request):
	return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
