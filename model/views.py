from ast import pattern
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from model import models
import re

class home(View):
    def get(self,request):
        all_img=models.PJ.objects.all()
        return render(request,'home.html',{'all_img':all_img})
    def post(self,request):
        l1=["3dmf","3dm","3mf","3ds","ac","an8","aoi","asm","b3d","blend","block","bmd","bdl","brres","c4d","cal3d","cfl","cob","core3d","ctm","dae","dpm","dts","fac","fbx","g","glb","glm","gltf","iob","jas","lwo","lws","lxf","lxo","ma","max","mb","md2","md3","md5","mdx","m","mesh","mm3d","nif","obj","off","ogex","ply","prt","pov","r3d","rwx","sia","sib","skp","sldasm","sldprt","smd","u3d","usd","usda","usdc","usdz","vimproj","wrl","vue","vwx","wings","w3d","x","x3d","z3d"]
        try:
            img=request.FILES['image']
            s=str(img)
            l=s.split(".")
            if l[-1] in l1:
                c=models.PJ(img=img)
                c.save()
                return redirect('/')
            else:
                error="Please select a valid  file"
                all_img=models.PJ.objects.all()
                return render(request,'home.html',{'all_img':all_img,'error':error})

        except:
            error="Please select a file"
            all_img=models.PJ.objects.all()
            return render(request,'home.html',{'all_img':all_img,'error':error})
class about(View):
    def get(self,request,id):
        c=models.PJ.objects.get(id=id)
        return render(request,'m.html',{'p':c.img,'id':id})
    def post(self,request,id):
        all_img=models.PJ.objects.all()
        return redirect('/')





